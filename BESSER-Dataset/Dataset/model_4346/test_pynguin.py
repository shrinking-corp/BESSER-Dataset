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
    ModelElement,
    Object,
    abstractmethod,
    date,
    datetime,
    hutn_AttributeSlot,
    hutn_ClassObject,
    hutn_ClassObjectSlot,
    hutn_ContainmentSlot,
    hutn_EPackage,
    hutn_ModelElement,
    hutn_NsUri,
    hutn_Object,
    hutn_PackageObject,
    hutn_ReferenceSlot,
    hutn_Slot,
    hutn_Spec,
    time,
)


def test_0():
    var_25 = python_code_.hutn_Spec(
        modelFile="l^?;|Z&G\\Cb\x0ch:iY",
        sourceFile="&wx",
        hutn_Spec={True, True},
        hutn_Spec2=set(),
    )
    assert isinstance(var_25, python_code_.hutn_Spec)


def test_1():
    var_25 = python_code_.hutn_Spec(
        modelFile="_hutn_Slot__slots-hutn_Spec2-hutn_Spec-_hutn_PackageObject__hutn_PackageObject6",
        sourceFile="hutn_PackageObject-hutn_PackageObject",
        hutn_Spec2=set(),
    )
    assert isinstance(var_25, python_code_.hutn_Spec)


def test_2():
    var_25 = python_code_.hutn_Spec(modelFile="qan$K", sourceFile="*=")
    assert isinstance(var_25, python_code_.hutn_Spec)


def test_3():
    python_code_.hutn_ClassObject()


def test_4():
    var_25 = python_code_.hutn_ClassObject(
        hutn_ClassObject="c:!zQm]JF%,y`#jn{",
        ClassObject=-3430.68,
        hutn_ClassObject9={
            "hutn_ContainmentSlot": 133,
            "_hutn_ClassObject__hutn_ClassObject._hutn_PackageObject__hutn_PackageObject.slots.ClassObject": "hutn_EPackage,_hutn_PackageObject__hutn_PackageObject6",
            "1'[c!},35'~i": -1,
        },
    )
    assert isinstance(var_25, python_code_.hutn_ClassObject)


def test_5():
    var_18 = python_code_.hutn_ClassObject(
        hutn_ClassObject9={"qb\x0bSe`7.d]": "~\\&-NpT>je0k"}
    )
    assert isinstance(var_18, python_code_.hutn_ClassObject)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = object
    var_1 = python_code_.hutn_ClassObject(hutn_ClassObject={})
    assert isinstance(var_1, python_code_.hutn_ClassObject)
    python_code_.hutn_Slot(feature=True, values=var_0, slots=var_1)


def test_7():
    var_23 = python_code_.hutn_NsUri(value="slots", hutn_NsUri=None)
    assert isinstance(var_23, python_code_.hutn_NsUri)


def test_8():
    var_19 = "rg]wV (9Y~AnHa],R2"
    var_20 = python_code_.hutn_NsUri(value=var_19, hutn_NsUri=0)
    assert isinstance(var_20, python_code_.hutn_NsUri)


def test_9():
    var_0 = lambda *args, **kwargs: "|tH02?"
    var_1 = "0(j0AkrvMP"
    var_2 = python_code_.hutn_Slot(feature=var_0, values=var_1)
    assert isinstance(var_2, python_code_.hutn_Slot)


def test_10():
    var_1 = list
    python_code_.hutn_ClassObjectSlot()
    var_28 = "[J:WTn)'"
    var_29 = python_code_.hutn_Slot(
        feature=var_1,
        values=var_28,
        slots={"hutn_PackageObject:_hutn_Slot__slots:hutn_Slot:hutn_ContainmentSlot"},
    )
    assert var_29.slots == {
        "hutn_PackageObject:_hutn_Slot__slots:hutn_Slot:hutn_ContainmentSlot"
    }
    var_29.multiplicityCompatibleWith(hutn_eStructuralFeature=var_1)


def test_11():
    var_0 = python_code_.hutn_PackageObject()
    assert isinstance(var_0, python_code_.hutn_PackageObject)


def test_12():
    var_25 = python_code_.hutn_Spec(
        modelFile="_hutn_ClassObject__hutn_ClassObject9,_hutn_PackageObject__hutn_PackageObject6,hutn_ClassObject,_hutn_ClassObject__ClassObject",
        sourceFile="$3g)fw@*|N*+Clrg}",
        hutn_Spec={-1169.5},
        hutn_Spec2=set(),
    )
    assert isinstance(var_25, python_code_.hutn_Spec)
    var_31 = python_code_.hutn_PackageObject(hutn_PackageObject=var_25)
    assert isinstance(var_31, python_code_.hutn_PackageObject)


def test_13():
    python_code_.hutn_ClassObjectSlot()


def test_14():
    var_4 = "P>F;uo#&e$S~"
    var_6 = python_code_.hutn_ClassObjectSlot()
    var_6.getClassObjects()
    var_25 = "ClassObject"
    var_26 = python_code_.hutn_Slot(feature=var_25, values=var_4)
    assert isinstance(var_26, python_code_.hutn_Slot)
    var_26.hasEStructuralFeature()


def test_15():
    var_0 = python_code_.hutn_ClassObjectSlot()
    var_1 = list
    var_0.setClassObjects(hutn_classObjects=object)
    var_3 = var_0.addClassObject(hutn_classObject=var_1)
    var_4 = python_code_.hutn_PackageObject(
        hutn_PackageObject=var_1, hutn_PackageObject4=var_3
    )
    assert isinstance(var_4, python_code_.hutn_PackageObject)
    var_5 = python_code_.hutn_ClassObject(hutn_ClassObject=var_4, ClassObject=var_0)
    assert isinstance(var_5, python_code_.hutn_ClassObject)
    var_5.findOrCreateReferenceSlot(hutn_feature=var_1)
    var_14 = "hutn_Containme`ntSlot hutn_EPackage"
    var_15 = python_code_.hutn_NsUri(value=var_14, hutn_NsUri=var_1)
    assert isinstance(var_15, python_code_.hutn_NsUri)


def test_16():
    var_34 = python_code_.hutn_ClassObject(
        hutn_ClassObject=None, hutn_ClassObject9=None
    )
    assert isinstance(var_34, python_code_.hutn_ClassObject)
    var_38 = "s\\pBJ<'\nx35"
    var_39 = "x'c"
    var_40 = python_code_.hutn_Spec(
        modelFile="mF\r}c)].Kq}\rD%-\x0b=", sourceFile=var_39, hutn_Spec=var_38
    )
    assert isinstance(var_40, python_code_.hutn_Spec)
    var_41 = python_code_.hutn_NsUri(value=var_38, hutn_NsUri=var_40)
    assert isinstance(var_41, python_code_.hutn_NsUri)
    var_42 = python_code_.hutn_ClassObjectSlot()
    var_42.addClassObject(hutn_classObject=var_41)


def test_17():
    var_1 = python_code_.hutn_ClassObject()
    var_2 = var_1.typeCompatibleWith(hutn_eClass=lambda *args, **kwargs: True)
    var_4 = "L%,zb\n\x0bbz?s"
    var_5 = python_code_.hutn_PackageObject(hutn_PackageObject=var_4)
    assert isinstance(var_5, python_code_.hutn_PackageObject)
    var_6 = var_5.getAllEClasses()
    var_1.findOrCreateReferenceSlot(hutn_feature=var_2)
    var_9 = python_code_.hutn_NsUri(value=var_6)
    assert isinstance(var_9, python_code_.hutn_NsUri)
    var_10 = python_code_.hutn_ClassObjectSlot()
    var_10.getClassObjects()


def test_18():
    var_25 = python_code_.hutn_Spec(modelFile="qan$K", sourceFile="*=")
    assert isinstance(var_25, python_code_.hutn_Spec)
    var_31 = python_code_.hutn_PackageObject(hutn_PackageObject=var_25)
    assert isinstance(var_31, python_code_.hutn_PackageObject)
    var_32 = python_code_.hutn_ClassObject(hutn_ClassObject=var_31)
    assert isinstance(var_32, python_code_.hutn_ClassObject)
    var_32.findSlot(hutn_feature=complex)


def test_19():
    var_25 = python_code_.hutn_Spec(modelFile="qan$K", sourceFile="*=")
    assert isinstance(var_25, python_code_.hutn_Spec)
    var_29 = "hutn_EPackage"
    var_30 = python_code_.hutn_NsUri(value=var_29, hutn_NsUri=b"n2\xc6=\xa9")
    assert isinstance(var_30, python_code_.hutn_NsUri)
    var_31 = python_code_.hutn_ClassObject(hutn_ClassObject=False)
    assert isinstance(var_31, python_code_.hutn_ClassObject)
    var_31.findOrCreateAttributeSlot(hutn_feature=var_31)


def test_20():
    var_0 = python_code_.hutn_ContainmentSlot()
    var_1 = python_code_.hutn_ClassObject(
        ClassObject=(True, -67.21, True), hutn_ClassObject9=var_0
    )
    assert isinstance(var_1, python_code_.hutn_ClassObject)
    var_1.getPackageObject()
    var_1.findOrCreateAttributeSlot(hutn_feature=var_1)


def test_21():
    var_18 = python_code_.hutn_Slot(
        feature=complex(1219.4029, 67.12194),
        values=(
            False,
            "_hutn_Slot__slots-hutn_PackageObject6-hutn_Spec-_hutn_NsUri__hutn_NsUri",
        ),
    )
    assert isinstance(var_18, python_code_.hutn_Slot)


def test_22():
    var_0 = lambda *args, **kwargs: "|tH02?"
    var_1 = "0(j0AkrvMP"
    var_2 = python_code_.hutn_Slot(feature=var_0, values=var_1)
    assert isinstance(var_2, python_code_.hutn_Slot)
    var_2.compatibleWith(hutn_eStructuralFeature=var_2)


def test_23():
    var_0 = "_hutn_PackageObject__hutn_PackageObject_hutn_ClassObject__hutn_ClassObject_hutn_PackageObject__hutn_PackageObject"
    var_1 = python_code_.hutn_Slot(feature=None, values=var_0)
    assert isinstance(var_1, python_code_.hutn_Slot)
    var_1.multiplicityCompatibleWith(hutn_eStructuralFeature=False)
    var_1.typeCompatibleWith(hutn_eStructuralFeature=(-1072.82, -1923.59, 836))
    var_6 = python_code_.hutn_ClassObjectSlot()
    var_6.getClassObjects()
    var_1.setValues(hutn_values=())
    var_13 = python_code_.hutn_ClassObject()
    var_13.findOrCreateReferenceSlot(hutn_feature=b"\xecr\x88\xfbHAl\xbf")


def test_24():
    var_0 = hash
    var_1 = "1J&xk\rDON]oWNv9$dRS"
    var_2 = python_code_.hutn_Slot(feature=var_1, values=var_1)
    assert isinstance(var_2, python_code_.hutn_Slot)
    var_2.setValues(hutn_values=var_0)
    python_code_.hutn_ClassObject()


def test_25():
    var_8 = python_code_.hutn_PackageObject(
        hutn_PackageObject=None, hutn_PackageObject6=set()
    )
    assert isinstance(var_8, python_code_.hutn_PackageObject)
    var_18 = python_code_.hutn_ClassObject(hutn_ClassObject=var_8, ClassObject=var_8)
    assert isinstance(var_18, python_code_.hutn_ClassObject)


def test_26():
    var_38 = python_code_.hutn_ClassObject(hutn_ClassObject={})
    assert isinstance(var_38, python_code_.hutn_ClassObject)
    var_39 = python_code_.hutn_PackageObject()
    assert isinstance(var_39, python_code_.hutn_PackageObject)
    var_38.findSlot(hutn_feature=[])
    var_41 = "Rn|o"
    var_42 = python_code_.hutn_Slot(feature=0, values=var_41)
    assert isinstance(var_42, python_code_.hutn_Slot)
    var_42.setValues(hutn_values=None)
    var_39.getAllEClasses()
    var_46 = var_38.getEClass()
    var_47 = python_code_.hutn_PackageObject(hutn_PackageObject6=var_46)
    assert isinstance(var_47, python_code_.hutn_PackageObject)
    var_49 = python_code_.hutn_ClassObjectSlot()
    var_49.setClassObjects(hutn_classObjects=var_42)
    var_42.getEStructuralFeature()


def test_27():
    var_8 = python_code_.hutn_PackageObject(
        hutn_PackageObject4={False, True, False},
        hutn_PackageObject6={2529, -116.08, -2455.43},
    )
    assert isinstance(var_8, python_code_.hutn_PackageObject)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = python_code_.hutn_ContainmentSlot()
    var_6 = python_code_.hutn_ClassObject(hutn_ClassObject={})
    assert isinstance(var_6, python_code_.hutn_ClassObject)
    var_9 = "Rn|o"
    var_10 = python_code_.hutn_Slot(feature=0, values=var_9)
    assert isinstance(var_10, python_code_.hutn_Slot)
    var_10.setValues(hutn_values=None)
    var_14 = var_6.getEClass()
    var_15 = python_code_.hutn_PackageObject(hutn_PackageObject6=var_14)
    assert isinstance(var_15, python_code_.hutn_PackageObject)
    var_16 = var_6.getEClass()
    python_code_.hutn_PackageObject(
        hutn_PackageObject4=var_16, hutn_PackageObject6=var_0
    )


def test_29():
    python_code_.hutn_ModelElement(line=3671, col=931)


def test_30():
    var_35 = python_code_.hutn_Object(type=1648.07, identifier=-5735.22)
    assert isinstance(var_35, python_code_.hutn_Object)


def test_31():
    var_21 = "C,CrW"
    var_18 = python_code_.hutn_Slot(feature=var_21, values=False)
    assert isinstance(var_18, python_code_.hutn_Slot)
    var_22 = var_18.hasEStructuralFeature()
    var_23 = python_code_.hutn_PackageObject(hutn_PackageObject4=var_22)
    assert isinstance(var_23, python_code_.hutn_PackageObject)
    var_24 = python_code_.hutn_ClassObjectSlot
    var_25 = "\x0b[h6wWR=aen0[y:q'u"
    var_26 = python_code_.hutn_Spec(modelFile=var_24, sourceFile=var_25)
    assert isinstance(var_26, python_code_.hutn_Spec)
    var_27 = python_code_.hutn_NsUri(value=False, hutn_NsUri=var_26)
    assert isinstance(var_27, python_code_.hutn_NsUri)


def test_32():
    var_8 = python_code_.hutn_PackageObject(
        hutn_PackageObject4=set(), hutn_PackageObject6=set()
    )
    assert isinstance(var_8, python_code_.hutn_PackageObject)
    var_9 = python_code_.hutn_ClassObject(hutn_ClassObject=var_8, ClassObject=var_8)
    assert isinstance(var_9, python_code_.hutn_ClassObject)
    var_9.hasEClass()
    var_15 = "hutn_ContainmentJSlot hutn_EPackage"
    var_16 = python_code_.hutn_Object(type=var_15, identifier=var_15)
    assert isinstance(var_16, python_code_.hutn_Object)


def test_33():
    var_8 = python_code_.hutn_PackageObject(
        hutn_PackageObject4=set(), hutn_PackageObject6=set()
    )
    assert isinstance(var_8, python_code_.hutn_PackageObject)
    var_9 = python_code_.hutn_ClassObject(hutn_ClassObject=var_8, ClassObject=var_8)
    assert isinstance(var_9, python_code_.hutn_ClassObject)
    var_9.hasEClass()
    var_15 = "hutn_Cont,ainmentJSlot hutn_EPacCkage"
    var_16 = python_code_.hutn_Object(type=var_15, identifier=var_15)
    assert isinstance(var_16, python_code_.hutn_Object)
    var_9.findOrCreateContainmentSlot(hutn_feature=complex(1947.125918, -2930.52741))
    var_18 = python_code_.hutn_Slot(feature=[], values=var_15)
    assert isinstance(var_18, python_code_.hutn_Slot)
    var_18.hasEStructuralFeature()


@pytest.mark.xfail(strict=True)
def test_34():
    var_8 = python_code_.hutn_PackageObject(
        hutn_PackageObject4=set(), hutn_PackageObject6=set()
    )
    assert isinstance(var_8, python_code_.hutn_PackageObject)
    var_9 = python_code_.hutn_ClassObject(hutn_ClassObject=var_8, ClassObject=var_8)
    assert isinstance(var_9, python_code_.hutn_ClassObject)
    var_9.hasEClass()
    var_15 = "hutn_ContainmentJSlot hutn_EPackage"
    var_16 = python_code_.hutn_Object(
        type=var_15, identifier="&Wxkr\x0cxbm\x0cjq,M`y.1"
    )
    assert isinstance(var_16, python_code_.hutn_Object)
    python_code_.hutn_Slot(
        feature="4`<jmT3Y", values="ClassObject._hutn_Slot__slots", slots=var_9
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = "/{kKC]Us=d"
    var_1 = python_code_.hutn_Slot(feature=var_0, values=None, slots=var_0)
    assert isinstance(var_1, python_code_.hutn_Slot)
    python_code_.hutn_ClassObject(ClassObject=var_1)
    assert isinstance(var_1.slots, python_code_.hutn_ClassObject)


def test_36():
    var_25 = python_code_.hutn_Spec(
        modelFile="S2", sourceFile="_hutn_Slot__slots", hutn_Spec2=set()
    )
    assert isinstance(var_25, python_code_.hutn_Spec)
    var_36 = python_code_.hutn_NsUri(value='7"hmK\rAC;aA"*z', hutn_NsUri=var_25)
    assert isinstance(var_36, python_code_.hutn_NsUri)


def test_37():
    var_34 = "z\t:NJEX[f`sF_"
    var_35 = "s@'f{kcKis't!B9lR"
    var_36 = python_code_.hutn_Spec(modelFile=var_34, sourceFile=var_35)
    assert isinstance(var_36, python_code_.hutn_Spec)
    var_37 = python_code_.hutn_PackageObject(
        hutn_PackageObject=var_36,
        hutn_PackageObject4=var_35,
        hutn_PackageObject6=b"G\xb4\xb7\xc0\x8b\x16\x11",
    )
    assert isinstance(var_37, python_code_.hutn_PackageObject)
    var_38 = python_code_.hutn_ClassObject(
        hutn_ClassObject=var_37, ClassObject=var_35, hutn_ClassObject9=var_35
    )
    assert isinstance(var_38, python_code_.hutn_ClassObject)
    var_38.findOrCreateAttributeSlot(hutn_feature=True)


def test_38():
    var_31 = python_code_.hutn_PackageObject(
        hutn_PackageObject=None, hutn_PackageObject6={3360, -5083.56}
    )
    assert isinstance(var_31, python_code_.hutn_PackageObject)
    var_38 = "q2T>A:W!@/'tBv?"
    var_39 = python_code_.hutn_Spec(
        modelFile="$q4", sourceFile=var_38, hutn_Spec2="\\r&x5D"
    )
    assert isinstance(var_39, python_code_.hutn_Spec)
    var_40 = python_code_.hutn_PackageObject(
        hutn_PackageObject=var_39, hutn_PackageObject4=var_38
    )
    assert isinstance(var_40, python_code_.hutn_PackageObject)
    python_code_.hutn_ClassObjectSlot()
