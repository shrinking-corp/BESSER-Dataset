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
    BasicType,
    CollectionType,
    MAssociation,
    MClass,
    MModelElement,
    MModelElementEx,
    Type,
    abstractmethod,
    date,
    datetime,
    model_BagType,
    model_BasicType,
    model_BooleanType,
    model_CollectionType,
    model_Comparable,
    model_EnumType,
    model_Expression,
    model_IntegerType,
    model_MAggregationKind,
    model_MAssociation,
    model_MAssociationClass,
    model_MAssociationEnd,
    model_MAttribute,
    model_MClass,
    model_MClassInvariant,
    model_MMVisitor,
    model_MModel,
    model_MModelElement,
    model_MModelElementEx,
    model_MMultiplicity,
    model_MNavigableElement,
    model_MOperation,
    model_MPrePostCondition,
    model_MRange,
    model_ObjectType,
    model_OclAnyType,
    model_OrderedSetType,
    model_Part,
    model_RealType,
    model_SequenceType,
    model_SetType,
    model_StringType,
    model_TupleType,
    model_Type,
    model_VarDecl,
    model_VarDeclList,
    model_VoidType,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = "tOh[?hiJ{tn@l["
    var_1 = python_code_.model_TupleType(parts=var_0)
    assert isinstance(var_1, python_code_.model_TupleType)
    var_4 = lambda *args, **kwargs: 781
    var_6 = python_code_.model_Type(
        typeName="G\ri/\x0bRv'VyLHPg{c<A", typeId=-1, model_Type27=var_4
    )
    python_code_.model_Part(name=var_0, model_Part=var_6)


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = python_code_.model_MModel(model_MModel19=set())
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation=var_1)
    assert isinstance(var_2, python_code_.model_MAssociation)
    var_2.processWithVisitor(model_v=var_0)
    var_4 = python_code_.model_MModelElement()
    var_4.name()
    var_6 = -405
    python_code_.model_MRange(lower=-949, upper=var_6)
    var_8 = dict
    var_4.processWithVisitor(model_v=var_8)
    var_14 = var_0.processWithVisitor(model_v=var_8)
    var_15 = "G}'A5I1zt"
    var_16 = python_code_.model_MClassInvariant(
        positionInModel=var_14,
        name=var_15,
        model_MClassInvariant65=var_8,
        model_MClassInvariant60=[-1555.4],
    )
    assert isinstance(var_16, python_code_.model_MClassInvariant)
    python_code_.model_MAssociationClass()
    python_code_.model_MModel()
    var_48 = python_code_.model_EnumType(
        name=complex(-1162.3, 414.69724), literals=var_15
    )
    assert isinstance(var_48, python_code_.model_EnumType)
    var_48.addLiteral(model_literal=var_8)
    python_code_.model_MNavigableElement(
        nameAsRolename=var_8,
        model_MNavigableElement=var_8,
        model_MNavigableElement57=var_2,
    )


def test_2():
    var_1 = "\nI#"
    var_2 = python_code_.model_EnumType(name=("4N\x0c;6|(D", 1157.86), literals=var_1)
    assert isinstance(var_2, python_code_.model_EnumType)
    python_code_.model_MAttribute()
    var_48 = abs
    var_49 = python_code_.model_MNavigableElement(
        nameAsRolename=var_48,
        model_MNavigableElement={
            "\\mg=": -1124,
            "model_VarDecl": True,
            "model_MClass13": -1879,
        },
    )
    assert isinstance(var_49, python_code_.model_MNavigableElement)


@pytest.mark.xfail(strict=True)
def test_3():
    var_60 = "Lb\x0b@zKDZ3y#S<"
    var_62 = python_code_.model_MNavigableElement(
        nameAsRolename=var_60, model_MNavigableElement=None
    )
    python_code_.model_MClass(
        model_MClass4="", model_MClass46=var_62, model_MClass55=var_62
    )


def test_4():
    var_6 = -412
    python_code_.model_MRange(
        lower=var_6,
        upper={
            "_model_MAssociation__model_MAssociation38:model_VarDecl": "G7s3Q.s'*3k}b",
            "model_Expression74,_model_MClassInvariant__model_MClassInvariant65,_model_MOperation__model_MOperation": 1361,
        },
    )
    var_75 = python_code_.model_MMultiplicity()
    assert isinstance(var_75, python_code_.model_MMultiplicity)
    var_75.addRange(model_r=None)
    python_code_.model_MNavigableElement(nameAsRolename=872.19)


def test_5():
    python_code_.model_MModelElement()
    var_6 = -412
    python_code_.model_MRange(
        lower=var_6,
        upper={
            "_model_MAssociation__model_MAssociation38:model_VarDecl": "G7s3Q.s'*3k}b",
            "model_Expression74,_model_MClassInvariant__model_MClassInvariant65,_model_MOperation__model_MOperation": 1361,
        },
    )


def test_6():
    python_code_.model_MModelElement()
    var_66 = python_code_.model_MMultiplicity()
    assert isinstance(var_66, python_code_.model_MMultiplicity)


@pytest.mark.xfail(strict=True)
def test_7():
    var_2 = "\x0bW:1o1T"
    python_code_.model_MAggregationKind(kind=complex(577.782, -692.830107), name=True)
    var_4 = python_code_.model_MAssociationEnd(
        mClassName=var_2, model_MAssociationEnd50=None
    )
    assert isinstance(var_4, python_code_.model_MAssociationEnd)
    python_code_.model_MMultiplicity(model_MMultiplicity=var_4)


def test_8():
    var_3 = -264
    var_4 = python_code_.model_MPrePostCondition(
        positionInModel=var_3, model_MPrePostCondition73=var_3
    )
    assert isinstance(var_4, python_code_.model_MPrePostCondition)
    var_4.getIsPre()
    var_7 = -1439
    var_8 = "U6\\"
    python_code_.model_MAggregationKind(kind=var_7, name=var_8)


@pytest.mark.xfail(strict=True)
def test_9():
    var_30 = "^sG6f!&7EbHJnx"
    var_37 = -1896
    var_38 = python_code_.model_MAggregationKind(kind=var_37, name=-782.64)
    var_39 = python_code_.model_MAssociationEnd(mClassName=var_30)
    assert isinstance(var_39, python_code_.model_MAssociationEnd)
    python_code_.model_MAssociation(
        model_MAssociation40=var_38, model_MAssociation43=var_39
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_3 = -264
    var_4 = python_code_.model_MPrePostCondition(
        positionInModel=var_3, model_MPrePostCondition73=var_3
    )
    assert isinstance(var_4, python_code_.model_MPrePostCondition)
    var_4.getIsPre()
    var_7 = -1439
    var_8 = "U6\\"
    var_9 = python_code_.model_MAggregationKind(kind=var_7, name=var_8)
    python_code_.model_MAssociationEnd(
        mClassName="_model_MClass__model_MClass13", model_MAssociationEnd50=var_9
    )


def test_11():
    var_75 = python_code_.model_IntegerType
    var_76 = python_code_.model_MAssociationClass()
    var_76.processWithVisitor(model_v=var_76)
    python_code_.model_MAggregationKind(
        kind=var_75,
        name=None,
        model_MAggregationKind51={2725.26, "m;$^%RuS7gj\tMW(\nDa"},
    )


def test_12():
    var_2 = "n"
    var_5 = 2594
    var_6 = python_code_.model_MClassInvariant(positionInModel=var_5, name=var_2)
    assert isinstance(var_6, python_code_.model_MClassInvariant)
    var_6.getHasVars()


def test_13():
    var_1 = 1269
    var_2 = python_code_.model_MClassInvariant(
        positionInModel=var_1,
        name=b"&\xb3\xdc\x8a]9\xe8\xd4`\xb6x1\xd5\x08,\xca\xe1HR",
        model_MClassInvariant65=var_1,
    )
    assert isinstance(var_2, python_code_.model_MClassInvariant)


def test_14():
    var_98 = python_code_.BasicType()
    var_101 = -226
    var_102 = python_code_.model_MClassInvariant(
        positionInModel=var_101,
        name="",
        model_MClassInvariant=None,
        model_MClassInvariant60=var_98,
    )
    assert isinstance(var_102, python_code_.model_MClassInvariant)


def test_15():
    var_0 = python_code_.model_VoidType()
    var_1 = python_code_.model_MMultiplicity()
    assert isinstance(var_1, python_code_.model_MMultiplicity)
    var_2 = python_code_.model_CollectionType()
    python_code_.model_Type(
        typeName=var_0, typeId=False, model_Type32=-1405.74, model_Type34=var_2
    )


def test_16():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass=var_0,
        model_MClass7={var_0},
        model_MClass4={var_0, var_0},
        model_MClass12=None,
        model_MClass24=None,
        model_MClass17=None,
        model_MClass46=None,
        model_MClass55=None,
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_59 = python_code_.model_MModelElement()
    var_66 = "1QM+-yM"
    python_code_.model_Type(
        typeName=var_66,
        typeId=complex(-158.802135, -676.0),
        model_Type27=complex(3723.972836, 1523.887925),
        model_Type76=var_59,
    )
    var_68 = python_code_.model_MOperation(model_MOperation26={-1058.96})
    assert isinstance(var_68, python_code_.model_MOperation)
    var_68.addVarDecl(model_vd=var_1)


def test_17():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)


@pytest.mark.xfail(strict=True)
def test_18():
    var_1 = "\nI#"
    var_2 = python_code_.model_EnumType(name=("4N\x0c;6|(D", 1157.86), literals=var_1)
    assert isinstance(var_2, python_code_.model_EnumType)
    var_3 = dict
    var_4 = var_2.addLiteral(model_literal=var_3)
    var_5 = python_code_.model_ObjectType()
    var_6 = python_code_.model_MClass(
        model_MClass10={
            'Pcg="|.g:[\x0c83Z': True,
            "@qS`XU`*\x0b3;(%^": -1015,
            "\ni": "",
        },
        model_MClass15=-9.42,
        model_MClass17=set(),
        model_MClass36=var_5,
    )
    assert isinstance(var_6, python_code_.model_MClass)
    var_7 = python_code_.model_MOperation(
        model_MOperation26=None, model_MOperation71=var_3
    )
    assert isinstance(var_7, python_code_.model_MOperation)
    var_9 = var_6.processWithVisitor(model_v=-482)
    python_code_.model_MClass(
        model_MClass7=var_4,
        model_MClass4=var_9,
        model_MClass10=b"\x0e\xc6\xde\x02\xc9z\xd3\xb1\xc2\xcf\x1e\x9c",
    )
    var_11 = python_code_.model_MNavigableElement(
        nameAsRolename=complex(-2486.47, 164.54904)
    )
    python_code_.model_MClass(
        model_MClass4={
            "_model_MAggregationKind__model_MAggregationKind51,_model_Type__model_Type32,model_MClassInvariant,model_Type76",
            "_model_MModel__model_MModel19",
            "?D=W(2,XlO/zmQ|'`6/",
        },
        model_MClass12=var_6,
        model_MClass10=var_5,
        model_MClass24=var_7,
        model_MClass55=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_19():
    var_2 = "pn"
    python_code_.model_MAssociationClass()
    var_14 = python_code_.model_MModel()
    var_28 = python_code_.model_MOperation()
    python_code_.model_MClass(
        model_MClass12={"0YI71KJ{0\\": -5083.9},
        model_MClass15=var_14,
        model_MClass24=var_28,
        model_MClass17=var_2,
    )


def test_20():
    python_code_.model_MModelElement()
    var_98 = python_code_.model_VarDecl
    var_100 = python_code_.MClass()
    var_102 = python_code_.model_MClass(model_MClass36=var_98)
    assert isinstance(var_102, python_code_.model_MClass)
    var_104 = python_code_.model_MAssociation(
        model_MAssociation=None, model_MAssociation58=None
    )
    assert isinstance(var_104, python_code_.model_MAssociation)
    var_106 = python_code_.model_MAssociationEnd(
        mClassName=var_100, model_MAssociationEnd45=var_98
    )
    assert isinstance(var_106, python_code_.model_MAssociationEnd)


def test_21():
    var_16 = python_code_.model_MClass(model_MClass13=())
    assert isinstance(var_16, python_code_.model_MClass)
    var_16.addParent(model_c=None)


def test_22():
    var_0 = python_code_.model_MModel()
    var_1 = python_code_.model_MClass(
        model_MClass12=var_0,
        model_MClass15=None,
        model_MClass46=var_0,
        model_MClass55=var_0,
        model_MClass63=None,
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation43=var_0)
    assert isinstance(var_2, python_code_.model_MAssociation)


def test_23():
    var_70 = python_code_.model_MModel(model_MModel19=set())
    assert isinstance(var_70, python_code_.model_MModel)
    var_70.addClassInvariant(
        model_inv="model_MAssociationEnd50:model_MClass7:_model_MClassInvariant__model_MClassInvariant"
    )
    var_76 = python_code_.model_MAssociationEnd(mClassName={True, False})
    assert isinstance(var_76, python_code_.model_MAssociationEnd)
    var_78 = python_code_.model_MPrePostCondition
    var_79 = python_code_.model_MAssociation(model_MAssociation58=var_78)
    assert isinstance(var_79, python_code_.model_MAssociation)


def test_24():
    var_81 = python_code_.model_MModelElement()
    var_81.name()
    var_84 = dict
    var_85 = python_code_.model_MAssociationEnd(
        mClassName=b"\xd5\xc2*\x18\n\x94\x13\xd8T",
        model_MAssociationEnd45=var_84,
        model_MAssociationEnd48=var_81,
    )
    assert isinstance(var_85, python_code_.model_MAssociationEnd)
    var_86 = var_85.getNavigation()
    var_81.processWithVisitor(model_v=var_84)
    var_89 = python_code_.model_MMultiplicity(model_MMultiplicity=var_86)
    assert isinstance(var_89, python_code_.model_MMultiplicity)


def test_25():
    var_4 = lambda *args, **kwargs: 781
    var_12 = python_code_.model_MAssociationEnd(
        mClassName=set(),
        model_MAssociationEnd42=var_4,
        model_MAssociationEnd50=complex(-688.37, -1507.1),
    )
    assert isinstance(var_12, python_code_.model_MAssociationEnd)
    python_code_.model_MNavigableElement(nameAsRolename=[])
    var_12.getOrdered()


def test_26():
    var_28 = python_code_.model_MPrePostCondition
    var_29 = python_code_.model_MAssociation(model_MAssociation58=var_28)
    assert isinstance(var_29, python_code_.model_MAssociation)


def test_27():
    var_0 = python_code_.model_MModel(
        model_MModel=set(),
        model_MModel19={-4190.4},
        model_MModel21={152.11, -1656.7, "T$e"},
    )
    assert isinstance(var_0, python_code_.model_MModel)
    var_2 = python_code_.model_MAssociation(model_MAssociation43=var_0)
    assert isinstance(var_2, python_code_.model_MAssociation)
    var_61 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_61, python_code_.model_MClass)
    python_code_.model_MAssociation(model_MAssociation=var_61)
    var_65 = python_code_.model_MModelElement()
    var_65.name()


def test_28():
    python_code_.model_MModel()


def test_29():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)


def test_30():
    python_code_.model_MOperation()


def test_31():
    var_2 = "n"
    var_4 = python_code_.model_EnumType(name=var_2, literals=":3dWk")
    assert isinstance(var_4, python_code_.model_EnumType)
    var_8 = python_code_.model_MOperation(model_MOperation26={-1058.96})
    assert isinstance(var_8, python_code_.model_MOperation)


def test_32():
    "pn"


def test_33():
    python_code_.model_MAssociationClass()
    python_code_.model_MModelElement()
    var_36 = python_code_.model_MMultiplicity()
    assert isinstance(var_36, python_code_.model_MMultiplicity)
    python_code_.model_VarDecl(var=var_36)


def test_34():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_4 = python_code_.model_MModelElement()
    var_4.name()


def test_35():
    var_0 = python_code_.model_MModel(model_MModel19=set())
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation=var_1)
    assert isinstance(var_2, python_code_.model_MAssociation)
    var_2.processWithVisitor(model_v=var_0)
    var_4 = python_code_.model_MModelElement()
    var_4.name()
    var_6 = -405
    python_code_.model_MRange(lower=-949, upper=var_6)
    var_8 = dict
    var_4.processWithVisitor(model_v=var_8)
    var_14 = var_0.processWithVisitor(model_v=var_8)
    var_15 = "G}'A5I1zt"
    var_16 = python_code_.model_MClassInvariant(
        positionInModel=var_14,
        name=var_15,
        model_MClassInvariant65=var_8,
        model_MClassInvariant60=[-1555.4],
    )
    assert isinstance(var_16, python_code_.model_MClassInvariant)
    var_17 = python_code_.model_MAssociationClass()
    python_code_.model_MModel()
    var_48 = python_code_.model_EnumType(
        name=complex(-1162.3, 414.69724), literals=var_15
    )
    assert isinstance(var_48, python_code_.model_EnumType)
    var_48.addLiteral(model_literal=var_8)
    var_55 = python_code_.model_MNavigableElement(nameAsRolename=var_15)
    var_55.getType(model_src="Wgr3VoW,124!")
    var_17.processWithVisitor(model_v="model_MClassInvariant")


def test_36():
    var_0 = python_code_.model_MModel(
        model_MModel=set(),
        model_MModel19={-4190.4},
        model_MModel21={152.11, -1656.7, "T$e"},
    )
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass12=var_0,
        model_MClass15=None,
        model_MClass46=var_0,
        model_MClass55=var_0,
        model_MClass63=None,
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation43=var_0)
    assert isinstance(var_2, python_code_.model_MAssociation)
    var_2.processWithVisitor(model_v=var_0)
    python_code_.model_MModelElement()
    var_61 = python_code_.model_MMultiplicity()
    assert isinstance(var_61, python_code_.model_MMultiplicity)
    python_code_.model_VarDecl(var=var_61)


@pytest.mark.xfail(strict=True)
def test_37():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_4 = python_code_.model_MModelElement()
    var_4.name()
    var_8 = dict
    var_9 = python_code_.model_MAssociationEnd(
        mClassName=b"\xd5\xc2*\x18\n\x94\x13\xd8T",
        model_MAssociationEnd45=var_8,
        model_MAssociationEnd48=var_4,
    )
    assert isinstance(var_9, python_code_.model_MAssociationEnd)
    var_49 = python_code_.model_MModel()
    var_49.addClass(model_cls=var_8)
    var_53 = python_code_.model_ObjectType()
    var_58 = python_code_.model_MAttribute()
    python_code_.model_MClass(
        model_MClass=var_58,
        model_MClass9=b"{\xbai\xde\x82\x86\xaf\x90\x95C",
        model_MClass12=var_53,
        model_MClass24=var_9,
        model_MClass17=var_49,
        model_MClass36=None,
        model_MClass46=var_58,
    )


def test_38():
    var_0 = python_code_.model_OrderedSetType()
    var_1 = "W3GT"
    var_2 = python_code_.model_MAggregationKind(
        kind=b"\x84\xe0\xab\xefo", name=var_1, model_MAggregationKind=var_1
    )
    assert isinstance(var_2, python_code_.model_MAggregationKind)
    var_3 = python_code_.model_MAssociationEnd(
        mClassName=var_1, model_MAssociationEnd42=var_0
    )
    assert isinstance(var_3, python_code_.model_MAssociationEnd)
    var_29 = python_code_.model_MOperation(
        model_MOperation23=var_1, model_MOperation26=var_2
    )
    assert isinstance(var_29, python_code_.model_MOperation)
    var_29.addVarDecl(model_vd=[299])


def test_39():
    var_9 = python_code_.model_VarDeclList()
    var_11 = 2857
    var_12 = python_code_.model_MPrePostCondition(
        positionInModel=var_11, model_MPrePostCondition70=var_9
    )
    assert isinstance(var_12, python_code_.model_MPrePostCondition)
    var_12.getIsPre()


@pytest.mark.xfail(strict=True)
def test_40():
    var_1 = "\nI#"
    var_2 = python_code_.model_EnumType(name=("4N\x0c;6|(D", 1157.86), literals=var_1)
    assert isinstance(var_2, python_code_.model_EnumType)
    var_3 = float
    var_11 = python_code_.model_MNavigableElement(
        nameAsRolename=complex(-2486.47, 164.54904)
    )
    var_13 = python_code_.model_MMVisitor()
    var_14 = 560
    var_15 = "\tZ6}\t\\I"
    var_16 = python_code_.model_MClassInvariant(
        positionInModel=var_14,
        name=var_15,
        model_MClassInvariant65=var_11,
        model_MClassInvariant62=var_3,
    )
    assert isinstance(var_16, python_code_.model_MClassInvariant)
    var_20 = python_code_.model_MPrePostCondition
    var_21 = python_code_.model_MAssociation(model_MAssociation58=var_20)
    assert isinstance(var_21, python_code_.model_MAssociation)
    var_22 = python_code_.model_MModelElementEx(name=var_13)
    assert isinstance(var_22, python_code_.model_MModelElementEx)
    var_22.processWithVisitor(model_v=720.9)
    python_code_.model_MOperation(model_MOperation71=var_14, model_MOperation29=var_11)


def test_41():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass=var_0,
        model_MClass7={var_0},
        model_MClass4={var_0, var_0},
        model_MClass12=None,
        model_MClass24=None,
        model_MClass17=None,
        model_MClass46=None,
        model_MClass55=None,
    )
    assert isinstance(var_1, python_code_.model_MClass)
    python_code_.model_MModelElement()
    var_61 = -700
    var_66 = "l1QM+-yM"
    var_70 = python_code_.model_MClassInvariant(positionInModel=var_61, name=var_66)
    assert isinstance(var_70, python_code_.model_MClassInvariant)
    var_70.getHasVars()


@pytest.mark.xfail(strict=True)
def test_42():
    var_13 = python_code_.model_MAssociationClass()
    var_14 = python_code_.model_MModel(model_MModel19=set(), model_MModel21=set())
    assert isinstance(var_14, python_code_.model_MModel)
    var_15 = python_code_.model_ObjectType()
    var_28 = python_code_.model_CollectionType()
    var_29 = var_13.processWithVisitor(model_v=var_15)
    var_33 = -226
    var_34 = python_code_.model_MClassInvariant(
        positionInModel=var_33, name=set(), model_MClassInvariant=var_14
    )
    assert isinstance(var_34, python_code_.model_MClassInvariant)
    python_code_.model_MClass(
        model_MClass9=var_14, model_MClass10=var_29, model_MClass36=var_28
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = python_code_.model_MMultiplicity()
    assert isinstance(var_0, python_code_.model_MMultiplicity)
    var_2 = "_model_MAssociationEnd__model_MAssociationEnd48"
    var_3 = python_code_.model_EnumType(name=var_2, literals=var_2)
    assert isinstance(var_3, python_code_.model_EnumType)
    var_4 = var_3.addLiteral(
        model_literal=lambda *args, **kwargs: "_model_MAssociation__model_MAssociation58"
    )
    var_5 = python_code_.model_MClass(model_MClass7=var_4)
    assert isinstance(var_5, python_code_.model_MClass)
    python_code_.model_MAssociationEnd(mClassName=var_0, model_MAssociationEnd45=var_5)


def test_44():
    var_60 = "Lb\x0b@zKDZ3y#S<"
    var_61 = python_code_.model_MModel(model_MModel19={253.15})
    assert isinstance(var_61, python_code_.model_MModel)
    var_62 = python_code_.model_MNavigableElement(
        nameAsRolename=var_60, model_MNavigableElement57=None
    )
    var_86 = python_code_.model_MModelElement
    var_88 = python_code_.model_MAssociationEnd(
        mClassName=var_60, model_MAssociationEnd=var_62
    )
    assert isinstance(var_88, python_code_.model_MAssociationEnd)
    var_88.getExplicitNavigation()
    var_87 = python_code_.model_MClassInvariant(positionInModel=var_86, name=var_60)
    assert isinstance(var_87, python_code_.model_MClassInvariant)
    var_63 = var_87.getIsExistential()
    var_81 = -412
    python_code_.model_MRange(lower=var_81, upper=var_63)


def test_45():
    var_7 = python_code_.model_MOperation(
        model_MOperation71={
            " v%<A>`O#e?": False,
            "model_ObjectTypemodel_MAttribute2_model_VarDecl__model_VarDecl_model_MClass__model_MClass12": 36,
        }
    )
    assert isinstance(var_7, python_code_.model_MOperation)


def test_46():
    var_3 = float
    var_44 = python_code_.model_MAttribute(
        model_MAttribute2=None, model_MAttribute5=var_3
    )
    assert isinstance(var_44, python_code_.model_MAttribute)


@pytest.mark.xfail(strict=True)
def test_47():
    var_75 = python_code_.model_IntegerType
    var_76 = python_code_.model_MAssociationClass()
    var_76.processWithVisitor(model_v=var_76)
    python_code_.model_MAggregationKind(
        kind=var_75,
        name=None,
        model_MAggregationKind51={2725.26, "m;$^%RuS7gj\tMW(\nDa"},
    )
    python_code_.model_MAttribute()
    var_87 = python_code_.model_MPrePostCondition(
        positionInModel=(), model_MPrePostCondition73=(2848.87, -2942)
    )
    assert isinstance(var_87, python_code_.model_MPrePostCondition)
    var_88 = var_87.setPre(model_b=-3131.89)
    var_89 = python_code_.model_MAssociation(model_MAssociation38=var_88)
    assert isinstance(var_89, python_code_.model_MAssociation)
    var_90 = var_89.addAssociationEnd(model_ae=None)
    var_91 = python_code_.model_MModel()
    var_92 = python_code_.model_ObjectType()
    var_93 = python_code_.model_MClass(
        model_MClass9=var_90,
        model_MClass17=var_91,
        model_MClass36=var_92,
        model_MClass55=[],
    )
    assert isinstance(var_93, python_code_.model_MClass)
    var_93.addOperation(model_op={"e:rt&D]l'Txv<0{fBY", -51})
    var_95 = var_87.getIsPre()
    var_96 = python_code_.model_MMultiplicity(model_MMultiplicity53=var_95)
    assert isinstance(var_96, python_code_.model_MMultiplicity)
    python_code_.model_MAssociationEnd(mClassName=-996, model_MAssociationEnd48=var_96)


@pytest.mark.xfail(strict=True)
def test_48():
    var_1 = lambda *args, **kwargs: True
    var_4 = "5~kZj2=5[{+#>=q"
    var_7 = "q9n5(At(#h|Q;^]"
    var_8 = "model_MAttribute2-_model_VarDecl__model_VarDecl31-_model_MAssociationEnd__model_MAssociationEnd45"
    var_9 = python_code_.model_EnumType(name=var_7, literals=var_8)
    assert isinstance(var_9, python_code_.model_EnumType)
    python_code_.model_MAttribute()
    var_16 = "%VJ>aCtXs=F"
    var_17 = 1
    var_18 = python_code_.model_MAggregationKind(
        kind=var_17, name=var_4, model_MAggregationKind51=var_1
    )
    python_code_.model_MAssociationEnd(
        mClassName=var_16,
        model_MAssociationEnd=var_9,
        model_MAssociationEnd42=var_16,
        model_MAssociationEnd50=var_18,
    )


@pytest.mark.xfail(strict=True)
def test_49():
    var_1 = "W3GT"
    var_2 = python_code_.model_MAggregationKind(
        kind=b"\x84\xe0\xab\xefo", name=var_1, model_MAggregationKind=var_1
    )
    assert isinstance(var_2, python_code_.model_MAggregationKind)
    python_code_.model_MAssociationClass()
    var_41 = -700
    var_42 = python_code_.model_MOperation()
    python_code_.model_MPrePostCondition(
        positionInModel=var_41, model_MPrePostCondition70=var_42
    )


def test_50():
    var_52 = lambda *args, **kwargs: True
    var_89 = python_code_.model_BagType()
    var_90 = python_code_.model_MAssociationClass()
    var_90.processWithVisitor(model_v="model_MClassInvariant")
    var_96 = python_code_.model_MAssociation(
        model_MAssociation=None, model_MAssociation43=None, model_MAssociation58=var_52
    )
    assert isinstance(var_96, python_code_.model_MAssociation)
    var_96.addAssociationEnd(model_ae=var_89)


@pytest.mark.xfail(strict=True)
def test_51():
    python_code_.model_MModelElement()
    var_2 = python_code_.model_MModel()
    var_3 = lambda *args, **kwargs: "model_MClass_model_Part__model_Part"
    var_2.addClass(model_cls=var_3)
    var_8 = 871
    var_9 = python_code_.model_MClassInvariant(positionInModel=var_8, name=var_3)
    assert isinstance(var_9, python_code_.model_MClassInvariant)
    python_code_.model_MMultiplicity(model_MMultiplicity53=var_9)


@pytest.mark.xfail(strict=True)
def test_52():
    var_1 = 1269
    var_2 = python_code_.model_MClassInvariant(
        positionInModel=var_1,
        name=b"&\xb3\xdc\x8a]9\xe8\xd4`\xb6x1\xd5\x08,\xca\xe1HR",
        model_MClassInvariant65=var_1,
    )
    assert isinstance(var_2, python_code_.model_MClassInvariant)
    var_3 = "L~l0"
    var_4 = python_code_.model_MModelElementEx(name=var_3)
    assert isinstance(var_4, python_code_.model_MModelElementEx)
    var_5 = python_code_.CollectionType
    var_6 = var_4.processWithVisitor(model_v=var_5)
    var_7 = python_code_.model_MClassInvariant(
        positionInModel=var_3, name=var_3, model_MClassInvariant65=var_3
    )
    python_code_.model_MClass(model_MClass4=var_6, model_MClass63=var_7)


def test_53():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    python_code_.model_MModelElement()
    var_1.getAbstract()
    var_0.addClassInvariant(model_inv=True)
    var_54 = python_code_.model_MPrePostCondition
    var_55 = python_code_.model_MAssociation(model_MAssociation58=var_54)
    assert isinstance(var_55, python_code_.model_MAssociation)
    python_code_.model_MAssociationClass()
    var_60 = python_code_.model_MAttribute(
        model_MAttribute2="_model_MAssociation__model_MAssociation38"
    )
    assert isinstance(var_60, python_code_.model_MAttribute)
    var_60.processWithVisitor(model_v=var_54)


@pytest.mark.xfail(strict=True)
def test_54():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation=var_1)
    assert isinstance(var_2, python_code_.model_MAssociation)
    var_2.processWithVisitor(model_v=var_0)
    var_4 = python_code_.model_MModelElement()
    var_4.name()
    var_6 = -412
    python_code_.model_MRange(lower=var_6, upper=var_1)
    var_8 = dict
    var_9 = python_code_.model_MAssociationEnd(
        mClassName=b"\xd5\xc2*\x18\n\x94\x13\xd8T",
        model_MAssociationEnd45=var_8,
        model_MAssociationEnd48=var_4,
    )
    assert isinstance(var_9, python_code_.model_MAssociationEnd)
    var_10 = var_9.getNavigation()
    var_4.processWithVisitor(model_v=var_8)
    var_13 = python_code_.model_MMultiplicity(model_MMultiplicity=var_10)
    assert isinstance(var_13, python_code_.model_MMultiplicity)
    var_14 = var_0.processWithVisitor(model_v=var_8)
    var_15 = "G}'A5I1Tzt"
    var_16 = python_code_.model_MClassInvariant(
        positionInModel=var_14,
        name=var_15,
        model_MClassInvariant65=var_8,
        model_MClassInvariant60=[-1555.4],
    )
    assert isinstance(var_16, python_code_.model_MClassInvariant)
    python_code_.model_MAssociationClass()
    var_39 = python_code_.model_MModel()
    var_40 = var_39.addClass(model_cls=var_8)
    var_41 = var_1.getAbstract()
    var_42 = python_code_.model_MModel(model_MModel=var_40, model_MModel21=var_41)
    var_44 = -700
    python_code_.model_MClassInvariant(
        positionInModel=var_44,
        name=var_42,
        model_MClassInvariant=var_8,
        model_MClassInvariant62=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_55():
    var_35 = "model_Expression _model_MClass__model_MClass55"
    var_47 = python_code_.model_VarDecl(var=var_35)
    python_code_.model_Type(
        typeName=[], typeId=set(), model_Type32=var_47, model_Type34={1016}
    )


@pytest.mark.xfail(strict=True)
def test_56():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation=var_1)
    assert isinstance(var_2, python_code_.model_MAssociation)
    python_code_.model_MModelElement()
    var_64 = python_code_.model_MOperation(
        model_MOperation71={
            " v%<A>`O#e?": False,
            "model_ObjectTypemodel_MAttribute2_model_VarDecl__model_VarDecl_model_MClass__model_MClass12": 36,
        }
    )
    assert isinstance(var_64, python_code_.model_MOperation)
    var_70 = int
    python_code_.model_MOperation(model_MOperation=var_0, model_MOperation29=var_70)


@pytest.mark.xfail(strict=True)
def test_57():
    python_code_.model_MAssociationClass()
    var_28 = python_code_.model_MModelElement()
    var_4 = var_28.name()
    var_5 = tuple
    python_code_.model_Type(typeName=var_4, typeId=var_5)
    python_code_.model_MNavigableElement(nameAsRolename=complex(-264.0, -1625.932))
    var_33 = "_model_MAttribute__model_MAttribute2"
    var_34 = python_code_.model_CollectionType()
    var_35 = python_code_.model_Type(
        typeName=var_33, typeId=var_5, model_Type27=var_5, model_Type34=var_34
    )
    python_code_.model_MAttribute(model_MAttribute=var_5, model_MAttribute2=var_35)


@pytest.mark.xfail(strict=True)
def test_58():
    var_0 = python_code_.model_MAssociation(model_MAssociation=None)
    assert isinstance(var_0, python_code_.model_MAssociation)
    var_51 = python_code_.Type()
    var_53 = python_code_.model_MAttribute()
    var_54 = python_code_.model_MClass(model_MClass13=())
    assert isinstance(var_54, python_code_.model_MClass)
    var_55 = lambda *args, **kwargs: [False]
    var_56 = var_54.addChild(model_c=var_55)
    var_57 = python_code_.model_ObjectType()
    var_58 = python_code_.model_MAssociationEnd(mClassName=var_51)
    assert isinstance(var_58, python_code_.model_MAssociationEnd)
    python_code_.model_MClass(
        model_MClass=var_53,
        model_MClass4=var_56,
        model_MClass36=var_57,
        model_MClass46=var_58,
    )


def test_59():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_2 = python_code_.model_MAssociation(model_MAssociation=var_1)
    assert isinstance(var_2, python_code_.model_MAssociation)
    python_code_.model_MModelElement()
    var_48 = lambda *args, **kwargs: 781
    var_49 = python_code_.model_MMVisitor
    var_54 = python_code_.model_MAssociationEnd(
        mClassName=set(),
        model_MAssociationEnd42=var_48,
        model_MAssociationEnd50=complex(-688.37, -1507.1),
    )
    assert isinstance(var_54, python_code_.model_MAssociationEnd)
    python_code_.model_MNavigableElement(nameAsRolename=[])
    var_54.getOrdered()
    var_59 = python_code_.model_MModel(
        model_MModel=set(),
        model_MModel19={False, -967, "_model_MModel__model_MModel19"},
        model_MModel21={False, var_1},
    )
    var_59.addPrePostCondition(model_ppc=var_49)
    python_code_.model_MOperation()


def test_60():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_4 = python_code_.model_MModelElement()
    var_4.name()
    var_6 = -412
    python_code_.model_MRange(lower=var_6, upper=var_1)
    var_58 = python_code_.model_MAssociation(model_MAssociation38={True})
    assert isinstance(var_58, python_code_.model_MAssociation)
    var_59 = sorted
    var_58.addAssociationEnd(model_ae=var_59)


def test_61():
    var_75 = python_code_.model_IntegerType
    python_code_.model_MAggregationKind(
        kind=var_75,
        name=None,
        model_MAggregationKind51={2725.26, "m;$^%RuS7gj\tMW(\nDa"},
    )
    python_code_.model_MAssociationClass()
    var_92 = python_code_.model_MAttribute(
        model_MAttribute=None, model_MAttribute5=var_75
    )
    assert isinstance(var_92, python_code_.model_MAttribute)
    var_92.processWithVisitor(model_v=var_75)


@pytest.mark.xfail(strict=True)
def test_62():
    python_code_.model_MAssociation()
    var_44 = -700
    var_45 = python_code_.model_MOperation()
    python_code_.model_MPrePostCondition(
        positionInModel=var_44, model_MPrePostCondition70=var_45
    )


def test_63():
    var_1 = "\nI#"
    var_2 = python_code_.model_EnumType(name=("4N\x0c;6|(D", 1157.86), literals=var_1)
    assert isinstance(var_2, python_code_.model_EnumType)
    var_13 = python_code_.model_MMVisitor()
    var_22 = python_code_.model_MModelElementEx(name=var_13)
    assert isinstance(var_22, python_code_.model_MModelElementEx)
    var_44 = python_code_.model_MAssociation()
    var_44.processWithVisitor(model_v=2)


@pytest.mark.xfail(strict=True)
def test_64():
    var_4 = python_code_.model_MModelElement()
    var_69 = python_code_.model_MModel()
    var_71 = -700
    python_code_.model_MAttribute()
    var_73 = python_code_.model_MNavigableElement(nameAsRolename=[])
    var_73.getType(model_src={214.05, True, "5kDd!=$;SOYcS\x0bG'|JF"})
    var_4.name()
    var_76 = python_code_.model_MClass(
        model_MClass4=None, model_MClass10=None, model_MClass46=var_71
    )
    assert isinstance(var_76, python_code_.model_MClass)
    var_77 = lambda *args, **kwargs: True
    var_78 = var_76.addAttribute(model_attr=var_77)
    var_79 = var_76.addAttribute(model_attr=var_77)
    python_code_.model_MClass(
        model_MClass=None,
        model_MClass9=var_78,
        model_MClass4=var_79,
        model_MClass10=var_76,
        model_MClass17=var_69,
        model_MClass46=var_77,
        model_MClass63=var_73,
    )


@pytest.mark.xfail(strict=True)
def test_65():
    var_2 = "pn"
    python_code_.model_MAssociationClass()
    python_code_.model_MModel()
    python_code_.model_MModelElement()
    var_18 = python_code_.model_StringType()
    var_20 = python_code_.model_VarDecl(var=var_2, model_VarDecl31=var_18)
    python_code_.model_Type(
        typeName=[], typeId=set(), model_Type32=var_20, model_Type34={1016}
    )


@pytest.mark.xfail(strict=True)
def test_66():
    var_20 = -412
    var_22 = python_code_.model_MModelElement
    var_23 = python_code_.model_IntegerType
    var_28 = "_model_MMultiplicity__model_MMultiplicity53,_model_MAssociationEnd__model_MAssociationEnd,model_MAssociationEnd50"
    var_29 = python_code_.model_Expression()
    var_30 = python_code_.model_MClassInvariant(
        positionInModel=var_20,
        name=var_28,
        model_MClassInvariant65=var_29,
        model_MClassInvariant67=var_22,
    )
    assert isinstance(var_30, python_code_.model_MClassInvariant)
    python_code_.model_MModel()
    python_code_.model_MClass(model_MClass46=var_23, model_MClass63=var_30)


@pytest.mark.xfail(strict=True)
def test_67():
    var_13 = python_code_.model_MAssociationClass()
    var_13.processWithVisitor(model_v=var_13)
    var_44 = "\\^.al#9;w/a\rk"
    var_45 = python_code_.model_MMultiplicity(model_MMultiplicity=b"\x8f}\x13\x85")
    assert isinstance(var_45, python_code_.model_MMultiplicity)
    python_code_.model_MAssociationEnd(
        mClassName=var_44, model_MAssociationEnd48=var_45
    )


@pytest.mark.xfail(strict=True)
def test_68():
    var_1 = "\nI#"
    var_2 = python_code_.model_EnumType(name=("4N\x0c;6|(D", 1157.86), literals=var_1)
    assert isinstance(var_2, python_code_.model_EnumType)
    var_3 = float
    python_code_.model_MNavigableElement(nameAsRolename=complex(-2486.47, 164.54904))
    var_47 = python_code_.model_MModelElementEx(name={-442.67, 997})
    assert isinstance(var_47, python_code_.model_MModelElementEx)
    var_47.processWithVisitor(model_v=())
    var_63 = python_code_.model_MAssociation(model_MAssociation58=var_3)
    assert isinstance(var_63, python_code_.model_MAssociation)
    var_52 = python_code_.model_MAttribute(model_MAttribute=var_3)
    assert isinstance(var_52, python_code_.model_MAttribute)
    var_53 = python_code_.model_MModelElement()
    var_54 = var_53.name()
    var_55 = lambda *args, **kwargs: "_model_MClass__model_MClass63"
    python_code_.model_MClass(
        model_MClass=var_52,
        model_MClass10=var_54,
        model_MClass36=var_55,
        model_MClass46=-245.06,
    )


def test_69():
    var_0 = python_code_.model_MModel(model_MModel={True})
    assert isinstance(var_0, python_code_.model_MModel)
    var_50 = python_code_.model_MModelElement()
    var_50.name()
    var_56 = python_code_.model_MPrePostCondition(
        positionInModel="uO6RQ&m", model_MPrePostCondition=var_0
    )
    assert isinstance(var_56, python_code_.model_MPrePostCondition)


def test_70():
    var_52 = lambda *args, **kwargs: True
    var_74 = "5~kZj2=5[{+#>=q"
    python_code_.model_MAttribute()
    var_77 = 1
    python_code_.model_MAggregationKind(
        kind=var_77, name=var_74, model_MAggregationKind51=var_52
    )
    var_79 = python_code_.model_MMultiplicity()
    assert isinstance(var_79, python_code_.model_MMultiplicity)
    var_80 = python_code_.model_MPrePostCondition(
        positionInModel=-225,
        model_MPrePostCondition=var_52,
        model_MPrePostCondition70=None,
        model_MPrePostCondition73=None,
    )
    assert isinstance(var_80, python_code_.model_MPrePostCondition)
    python_code_.model_MAssociationClass()


@pytest.mark.xfail(strict=True)
def test_71():
    var_2 = "pn"
    var_13 = python_code_.model_MAssociationClass()
    var_14 = python_code_.model_MModel(model_MModel19=set(), model_MModel21=set())
    assert isinstance(var_14, python_code_.model_MModel)
    var_15 = python_code_.model_ObjectType()
    var_26 = python_code_.model_ObjectType()
    var_28 = python_code_.model_CollectionType()
    var_13.processWithVisitor(model_v=True)
    var_33 = -226
    var_34 = python_code_.model_MClassInvariant(positionInModel=3900, name=var_2)
    assert isinstance(var_34, python_code_.model_MClassInvariant)
    var_30 = python_code_.model_MClass(
        model_MClass=None,
        model_MClass7=set(),
        model_MClass9={False, -1220},
        model_MClass10=set(),
        model_MClass15=var_26,
        model_MClass24=var_33,
        model_MClass36=var_26,
        model_MClass55=var_15,
    )
    assert isinstance(var_30, python_code_.model_MClass)
    var_31 = lambda *args, **kwargs: -1160
    var_30.addParent(model_c=var_28)
    var_42 = python_code_.model_MPrePostCondition(positionInModel=None)
    assert isinstance(var_42, python_code_.model_MPrePostCondition)
    var_42.getIsPre()
    var_35 = python_code_.model_MAttribute()
    var_36 = python_code_.model_MAssociation()
    var_37 = tuple
    var_38 = var_36.addAssociationEnd(model_ae=var_37)
    var_39 = abs
    var_40 = python_code_.model_MNavigableElement(
        nameAsRolename=var_39,
        model_MNavigableElement={
            "\\mg=": -1124,
            "model_VarDecl": True,
            "model_MClass13": -1879,
        },
    )
    assert isinstance(var_40, python_code_.model_MNavigableElement)
    python_code_.model_MClass(
        model_MClass=var_35,
        model_MClass7=var_31,
        model_MClass10=var_38,
        model_MClass15=var_30,
        model_MClass36=var_2,
        model_MClass55=var_40,
    )


@pytest.mark.xfail(strict=True)
def test_72():
    var_1 = python_code_.model_OrderedSetType()
    var_3 = python_code_.model_ObjectType()
    var_5 = repr
    var_6 = python_code_.model_MClass(
        model_MClass12=True, model_MClass15=var_3, model_MClass36=var_5
    )
    assert isinstance(var_6, python_code_.model_MClass)
    var_6.getAbstract()
    var_6.addAttribute(model_attr=var_1)
    var_10 = python_code_.model_Part(name=var_1, model_Part=var_5)
    assert isinstance(var_10, python_code_.model_Part)
    var_6.setAbstract(model_b=var_5)
    python_code_.model_MAttribute(model_MAttribute=var_6, model_MAttribute5=var_6)


@pytest.mark.xfail(strict=True)
def test_73():
    var_0 = "tOh[?hiJ[${tn@l["
    var_1 = python_code_.model_TupleType(parts=var_0)
    assert isinstance(var_1, python_code_.model_TupleType)
    var_28 = -194
    var_29 = python_code_.model_Expression()
    var_30 = python_code_.model_MClassInvariant(
        positionInModel=4477, name=var_0, model_MClassInvariant62=var_28
    )
    assert isinstance(var_30, python_code_.model_MClassInvariant)
    var_30.getIsExistential()
    var_32 = python_code_.model_MModel()
    var_33 = python_code_.model_MNavigableElement(
        nameAsRolename=var_0, model_MNavigableElement57=var_29
    )
    python_code_.model_MClass(
        model_MClass4=[],
        model_MClass17=var_32,
        model_MClass55=var_33,
        model_MClass63=[False],
    )


@pytest.mark.xfail(strict=True)
def test_74():
    var_0 = "#L+a%6%cDxEI2]"
    var_3 = -264
    var_4 = python_code_.model_MPrePostCondition(
        positionInModel=var_3, model_MPrePostCondition73=var_3
    )
    assert isinstance(var_4, python_code_.model_MPrePostCondition)
    var_4.getIsPre()
    var_27 = python_code_.model_Comparable()
    var_33 = len
    var_34 = python_code_.model_MAssociationEnd(
        mClassName=var_33,
        model_MAssociationEnd45=var_27,
        model_MAssociationEnd48=b"Hr\\\xc8",
    )
    assert isinstance(var_34, python_code_.model_MAssociationEnd)
    var_35 = var_34.getExplicitNavigation()
    var_36 = python_code_.model_MClass(model_MClass7=var_35, model_MClass63=var_0)
    assert isinstance(var_36, python_code_.model_MClass)
    var_37 = python_code_.model_MOperation(model_MOperation71=False)
    assert isinstance(var_37, python_code_.model_MOperation)
    var_38 = python_code_.model_ObjectType()
    python_code_.model_MClass(
        model_MClass12=var_36,
        model_MClass24=var_37,
        model_MClass36=var_38,
        model_MClass46=var_34,
    )


@pytest.mark.xfail(strict=True)
def test_75():
    var_0 = 460
    var_1 = python_code_.model_MRange(lower=var_0, upper=4506, model_MRange=var_0)
    assert isinstance(var_1, python_code_.model_MRange)
    var_2 = "\x0bW:1o1T"
    python_code_.model_MAggregationKind(kind=complex(577.782, -692.830107), name=True)
    var_4 = python_code_.model_MAssociationEnd(
        mClassName=var_2, model_MAssociationEnd48=None
    )
    assert isinstance(var_4, python_code_.model_MAssociationEnd)
    python_code_.model_MMultiplicity(model_MMultiplicity=var_4)


def test_76():
    var_0 = python_code_.model_MModel(model_MModel21=[])
    assert isinstance(var_0, python_code_.model_MModel)
    var_1 = python_code_.model_MClass(
        model_MClass15=[False, 247.21], model_MClass17=var_0, model_MClass63=var_0
    )
    assert isinstance(var_1, python_code_.model_MClass)
    var_4 = python_code_.model_MModelElement()
    var_4.name()
    var_56 = python_code_.model_MPrePostCondition(
        positionInModel="uO6RQ&m", model_MPrePostCondition=var_0
    )
    assert isinstance(var_56, python_code_.model_MPrePostCondition)


@pytest.mark.xfail(strict=True)
def test_77():
    var_3 = -264
    var_4 = python_code_.model_MPrePostCondition(
        positionInModel=var_3, model_MPrePostCondition73=var_3
    )
    assert isinstance(var_4, python_code_.model_MPrePostCondition)
    var_4.getIsPre()
    var_27 = python_code_.model_MMVisitor()
    var_31 = python_code_.model_MAssociation(model_MAssociation38=set())
    assert isinstance(var_31, python_code_.model_MAssociation)
    var_32 = python_code_.model_MModelElementEx(name=var_27)
    assert isinstance(var_32, python_code_.model_MModelElementEx)
    var_32.processWithVisitor(model_v=720.9)
    var_34 = python_code_.Type()
    var_39 = python_code_.model_MAssociationEnd(
        mClassName=var_34, model_MAssociationEnd=var_31
    )
    assert isinstance(var_39, python_code_.model_MAssociationEnd)
    python_code_.model_MMultiplicity(model_MMultiplicity=var_39)
