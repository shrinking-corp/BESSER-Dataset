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
    Abstraction,
    Arg,
    BeginBody,
    Body,
    BoolLiteralEnum,
    Condition,
    Enum,
    Expr,
    FinalExpr,
    InequalityOp,
    LogicalExpr,
    PrimitiveTypeEnum,
    PropertyExpr,
    Return,
    ReturnExpr,
    ReturnTypeExpr,
    Statement,
    Type,
    b_Abstraction,
    b_AndExpr,
    b_Arg,
    b_ArgMinus,
    b_AssertionExpr,
    b_Assertions,
    b_Assign,
    b_Begin,
    b_BeginBody,
    b_Body,
    b_BoolLiteral,
    b_BoolTest,
    b_Call,
    b_Case,
    b_CaseExpr,
    b_ConcreteConstants,
    b_ConcreteVariables,
    b_CondAnd,
    b_CondEq,
    b_CondLessThan,
    b_CondMinus,
    b_CondNeg,
    b_Condition,
    b_ConstantExpr,
    b_Definition,
    b_DefinitionCall,
    b_Definitions,
    b_EObject,
    b_EqualExpr,
    b_Expr,
    b_FinalExpr,
    b_If,
    b_IfCond,
    b_Implementation,
    b_ImplyExpr,
    b_Imports,
    b_InequalityExpr,
    b_Initialisation,
    b_InitialisationExpr,
    b_IntLiteral,
    b_Invariant,
    b_InvariantExpr,
    b_LocalOperations,
    b_LogicalExpr,
    b_Machine,
    b_Neg,
    b_NegExpr,
    b_Operation,
    b_Operations,
    b_Pre,
    b_PreExpr,
    b_PrimitiveType,
    b_Properties,
    b_PropertyExpr,
    b_PropertyRange,
    b_PropertyTyped,
    b_Range,
    b_Ref,
    b_Return,
    b_ReturnExpr,
    b_ReturnOr,
    b_ReturnTuple,
    b_ReturnTypeExpr,
    b_Sees,
    b_Seq,
    b_Set,
    b_Sets,
    b_SimpleCall,
    b_Skip,
    b_Statement,
    b_StringLiteral,
    b_Type,
    b_TypeConstraint,
    b_ValueExpr,
    b_Values,
    b_Var,
    b_Variable,
    date,
    datetime,
    time,
)


def test_0():
    var_6 = python_code_.b_InequalityExpr(op="|M4{ph0Z(9$9< r")
    assert isinstance(var_6, python_code_.b_InequalityExpr)


def test_1():
    var_0 = python_code_.b_Definition(name="", b_Definition78={-2037, False, "E"})
    assert isinstance(var_0, python_code_.b_Definition)


def test_2():
    var_0 = python_code_.b_Definition(name="GREATER_EQ,TRUE")
    assert isinstance(var_0, python_code_.b_Definition)


def test_3():
    var_0 = python_code_.b_Definition(name="*<C2\nsL~", b_Definition83=None)
    assert isinstance(var_0, python_code_.b_Definition)
    var_5 = "b_OpKration100"
    var_6 = python_code_.b_Definition(name=var_5, b_Definition81=True)
    assert isinstance(var_6, python_code_.b_Definition)


def test_4():
    var_13 = "b_Operation100"
    var_16 = python_code_.b_ReturnTuple()
    python_code_.b_Variable(
        name=var_13,
        b_Variable149="b_InitialisationExpr52",
        b_Variable165=None,
        b_Variable219=var_16,
    )


def test_5():
    var_2 = python_code_.b_DefinitionCall()
    var_3 = "lCm9%Lq;MQ"
    var_4 = python_code_.b_LocalOperations()
    var_5 = ",\\[\ttZ\x0clF,"
    var_6 = python_code_.b_PropertyExpr()
    var_7 = python_code_.b_AndExpr
    var_8 = python_code_.b_InitialisationExpr()
    var_9 = python_code_.b_Ref()
    var_10 = python_code_.b_Variable(
        name=var_5,
        b_Variable46=False,
        b_Variable64=var_6,
        b_Variable38=var_7,
        b_Variable71=var_7,
        b_Variable53=var_8,
        b_Variable101=317,
        b_Variable123=var_6,
        b_Variable98=var_2,
        b_Variable168=var_9,
    )
    assert isinstance(var_10, python_code_.b_Variable)
    var_11 = {var_10, var_10, var_10, var_10}
    var_12 = python_code_.b_Operation(
        name=var_3, b_Operation157=None, b_Operation163=var_4, b_Operation97=var_11
    )
    assert isinstance(var_12, python_code_.b_Operation)
    var_14 = python_code_.b_StringLiteral(value=b"\x11\xec\x02")
    assert isinstance(var_14, python_code_.b_StringLiteral)
    var_23 = python_code_.b_Operation(name=var_5, b_Operation103="#pj@HL")
    assert isinstance(var_23, python_code_.b_Operation)


def test_6():
    var_0 = python_code_.b_Definition(
        name="]Wx0XbM", b_Definition78=set(), b_Definition83=None
    )
    assert isinstance(var_0, python_code_.b_Definition)
    var_5 = python_code_.b_Type()
    var_6 = lambda *args, **kwargs: -2002
    var_7 = python_code_.b_Variable(
        name=var_6, b_Variable79=var_5, b_Variable137=(), b_Variable165=var_5
    )
    assert isinstance(var_7, python_code_.b_Variable)


def test_7():
    var_4 = python_code_.b_NegExpr()
    var_5 = python_code_.b_CondAnd
    var_6 = python_code_.b_ReturnTypeExpr()
    var_7 = python_code_.b_TypeConstraint()
    var_8 = python_code_.b_ReturnTuple()
    python_code_.b_Variable(
        name=var_4,
        b_Variable64=True,
        b_Variable="sWf",
        b_Variable38=(),
        b_Variable149=var_4,
        b_Variable71=var_5,
        b_Variable79=var_5,
        b_Variable118=b"O\x07y\xd9^\x1c\xd6E",
        b_Variable123=(True,),
        b_Variable93=var_5,
        b_Variable132=var_6,
        b_Variable195=var_7,
        b_Variable219=var_8,
    )


def test_8():
    var_0 = python_code_.b_CaseExpr()
    var_1 = python_code_.b_Machine()
    var_2 = python_code_.b_If()
    var_4 = python_code_.b_Range(lowerBound=var_1)
    var_6 = lambda *args, **kwargs: []
    var_7 = python_code_.b_Assign()
    var_8 = python_code_.b_Var()
    var_9 = python_code_.b_ReturnTuple()
    python_code_.b_Variable(
        name=var_6,
        b_Variable=var_4,
        b_Variable38=var_6,
        b_Variable149=var_0,
        b_Variable128=var_7,
        b_Variable123=var_8,
        b_Variable98=var_6,
        b_Variable132=var_7,
        b_Variable137=var_2,
        b_Variable142=var_6,
        b_Variable219=var_9,
    )


def test_9():
    var_1 = python_code_.b_Call()
    var_10 = python_code_.b_InvariantExpr()
    var_11 = python_code_.b_Assign()
    var_12 = python_code_.b_Neg
    python_code_.b_Variable(
        name={'y^q~sp"Tf>BNE/jF': "yba0;1", "": 3109.98, "$N5t/": -921.72},
        b_Variable46=var_10,
        b_Variable41=[
            "_b_Definition__b_Definition83:_b_Range__b_Range172:_b_Variable__b_Variable142",
            2,
            '"\r^\rqDuz=l_k]zN=\tX}',
        ],
        b_Variable71=True,
        b_Variable128=var_11,
        b_Variable93=var_12,
        b_Variable98=var_1,
    )
    var_16 = python_code_.b_Operation(
        name="b_CaseExpr-b_Variable98-_b_Variable__b_Variable-_b_Variable__b_Variable128",
        b_Operation=None,
    )
    assert isinstance(var_16, python_code_.b_Operation)


def test_10():
    var_0 = python_code_.b_ConstantExpr(
        constant="b_Variable79 b_Values33 _b_Abstraction__b_Abstraction2"
    )
    assert isinstance(var_0, python_code_.b_ConstantExpr)
    var_1 = lambda *args, **kwargs: "b_CaseExpr141"
    var_11 = ")\\Jq0&gygj5&\t6&"
    var_12 = python_code_.b_Sees()
    python_code_.b_Abstraction(
        name=var_11, b_Abstraction8=var_1, b_Abstraction28=var_12
    )


def test_11():
    var_0 = python_code_.b_Definition(name="*<C2\nsL~", b_Definition83=None)
    assert isinstance(var_0, python_code_.b_Definition)
    var_5 = "b_Operation100"
    var_6 = python_code_.b_Definition(name=var_5, b_Definition81=True)
    assert isinstance(var_6, python_code_.b_Definition)
    var_11 = python_code_.b_Arg
    var_12 = python_code_.b_Properties()
    python_code_.b_Abstraction(name=var_5, b_Abstraction2=var_11, b_Abstraction6=var_12)


def test_12():
    var_0 = python_code_.b_ConstantExpr(
        constant="b_Variable79 b_Values33 _b_Abstraction__b_Abstraction2"
    )
    assert isinstance(var_0, python_code_.b_ConstantExpr)
    var_2 = python_code_.b_InequalityExpr(op="Y+w?`\tPy%r-FVFMN")
    assert isinstance(var_2, python_code_.b_InequalityExpr)
    var_5 = python_code_.b_If()
    var_6 = python_code_.b_ConcreteConstants()
    python_code_.b_Variable(
        name="(",
        b_Variable46=None,
        b_Variable149=var_5,
        b_Variable128=None,
        b_Variable101=None,
        b_Variable123=var_6,
        b_Variable195=None,
        b_Variable165=None,
        b_Variable219=None,
    )
    var_12 = python_code_.b_Sees()
    python_code_.b_Abstraction(
        name="BOOL-_b_Definition__b_Definition81-_b_Variable__b_Variable149",
        b_Abstraction=var_12,
    )


def test_13():
    var_34 = "F/6"
    var_42 = python_code_.b_ReturnTuple()
    python_code_.b_Variable(
        name=var_34,
        b_Variable149="b_InitialisationExpr52",
        b_Variable165=None,
        b_Variable219=var_42,
    )
    var_44 = 'xJ;&WI&,"cHr'
    var_45 = python_code_.b_Definitions()
    var_46 = python_code_.b_Imports()
    python_code_.b_Abstraction(
        name=var_44, b_Abstraction="", b_Abstraction4=var_45, b_Abstraction31=var_46
    )


def test_14():
    python_code_.Condition()


def test_15():
    var_0 = python_code_.b_PrimitiveType(type=2078.1)
    assert isinstance(var_0, python_code_.b_PrimitiveType)


def test_16():
    var_0 = python_code_.b_ConstantExpr(
        constant="b_Variable79 b_Values33 _b_Abstraction__b_Abstraction2"
    )
    assert isinstance(var_0, python_code_.b_ConstantExpr)
    var_4 = python_code_.b_StringLiteral(value=())
    assert isinstance(var_4, python_code_.b_StringLiteral)
    var_7 = python_code_.b_Operations()
    var_9 = python_code_.b_LogicalExpr()
    var_10 = python_code_.b_InequalityExpr(op=var_7, b_InequalityExpr183=var_9)
    assert isinstance(var_10, python_code_.b_InequalityExpr)


def test_17():
    var_5 = "I9JJV(15]82<fe9"
    var_6 = (
        lambda *args, **kwargs: "b_ConcreteConstants40 _b_Abstraction__b_Abstraction31 _b_Abstraction__b_Abstraction28 b_CaseExpr"
    )
    var_7 = python_code_.b_BoolLiteral(value=var_5, constant=var_6)
    assert isinstance(var_7, python_code_.b_BoolLiteral)


def test_18():
    var_0 = python_code_.b_Condition()
    var_2 = "O7.(F* u-\t_\r%f4U{K"
    var_3 = python_code_.b_Case()
    var_4 = python_code_.b_TypeConstraint()
    var_5 = python_code_.b_Ref()
    python_code_.b_Variable(
        name=var_2,
        b_Variable64=var_2,
        b_Variable38=var_2,
        b_Variable41={},
        b_Variable71=var_2,
        b_Variable79=var_2,
        b_Variable128=var_0,
        b_Variable132=var_2,
        b_Variable137=var_3,
        b_Variable195=var_4,
        b_Variable165=var_0,
        b_Variable168=var_5,
    )
    var_17 = python_code_.b_IntLiteral(value=complex(-244.95, 626.877))
    assert isinstance(var_17, python_code_.b_IntLiteral)
    var_46 = python_code_.b_BoolLiteral(
        value=["b_ReturnTypeExpr:b_Definitions76:b_Assign", -2783, -1728],
        constant=var_2,
    )
    assert isinstance(var_46, python_code_.b_BoolLiteral)
    var_50 = "b_Operation100"
    var_51 = python_code_.b_Definition(name=var_50, b_Definition81=True)
    assert isinstance(var_51, python_code_.b_Definition)
    var_53 = python_code_.b_InequalityExpr(op=var_50)
    assert isinstance(var_53, python_code_.b_InequalityExpr)


def test_19():
    var_0 = python_code_.b_ConstantExpr(
        constant="b_Variable79 b_Values33 _b_Abstraction__b_Abstraction2"
    )
    assert isinstance(var_0, python_code_.b_ConstantExpr)
    var_1 = lambda *args, **kwargs: "b_CaseExpr141"
    var_2 = python_code_.b_InequalityExpr(op=var_1)
    assert isinstance(var_2, python_code_.b_InequalityExpr)


def test_20():
    var_0 = python_code_.b_Definition(name="", b_Definition78={-2037, False, "E"})
    assert isinstance(var_0, python_code_.b_Definition)
    var_8 = python_code_.b_Definitions()
    python_code_.b_Definition(
        name=complex(-929.830207, -1303.5896421), b_Definition=var_8
    )


def test_21():
    var_10 = "zA_"
    python_code_.b_ValueExpr(value=var_10, b_ValueExpr=None)


def test_22():
    var_0 = python_code_.b_Definition(name="", b_Definition78={-2037, False, "E"})
    assert isinstance(var_0, python_code_.b_Definition)
    python_code_.b_Definition(name="L\\vZ", b_Definition=None, b_Definition83=var_0)


def test_23():
    var_0 = python_code_.b_Definition(name="*<C2\nsL~", b_Definition83=None)
    assert isinstance(var_0, python_code_.b_Definition)
    var_4 = python_code_.b_LocalOperations()
    var_5 = "b_Operation100"
    var_6 = python_code_.b_Definition(name=var_5, b_Definition81=True)
    assert isinstance(var_6, python_code_.b_Definition)
    python_code_.b_Abstraction(name=var_5, b_Abstraction31=var_4)


def test_24():
    var_0 = python_code_.b_Definition(
        name="LA\nyY:o:B", b_Definition81=None, b_Definition83=None
    )
    assert isinstance(var_0, python_code_.b_Definition)
    var_10 = "zA_"
    var_11 = python_code_.b_LogicalExpr()
    var_12 = python_code_.b_InequalityExpr(op=var_10, b_InequalityExpr=var_11)
    assert isinstance(var_12, python_code_.b_InequalityExpr)
    python_code_.b_ValueExpr(value=[])


@pytest.mark.xfail(strict=True)
def test_25():
    var_4 = python_code_.b_InequalityExpr(op=complex(1783.4, 406.0060428))
    assert isinstance(var_4, python_code_.b_InequalityExpr)
    var_5 = "VJ\tid"
    var_6 = python_code_.b_Values()
    var_7 = python_code_.b_Call()
    var_8 = python_code_.b_Definitions()
    var_9 = python_code_.b_Definition(
        name=complex(-929.830207, -1303.5896421), b_Definition=var_8
    )
    assert isinstance(var_9, python_code_.b_Definition)
    var_10 = lambda *args, **kwargs: []
    var_11 = python_code_.b_Variable(
        name=var_4,
        b_Variable149=var_7,
        b_Variable79=var_9,
        b_Variable137=var_4,
        b_Variable195=(),
        b_Variable165=var_10,
        b_Variable168={644.03, -171},
    )
    assert isinstance(var_11, python_code_.b_Variable)
    python_code_.b_ValueExpr(value=var_5, b_ValueExpr=var_6, b_ValueExpr35=var_11)


def test_26():
    var_0 = python_code_.Expr()
    var_1 = python_code_.b_ReturnExpr()
    var_58 = python_code_.b_Assign()
    var_60 = "b_Operation100"
    var_61 = python_code_.b_Definition(name=var_60, b_Definition81=True)
    assert isinstance(var_61, python_code_.b_Definition)
    var_66 = python_code_.b_Variable(
        name=var_60,
        b_Variable66=None,
        b_Variable38=var_58,
        b_Variable41=None,
        b_Variable79=None,
        b_Variable128=None,
        b_Variable90=None,
        b_Variable98=None,
        b_Variable132=var_60,
        b_Variable137=None,
        b_Variable142=var_1,
    )
    var_67 = python_code_.b_Ref
    python_code_.b_Range(lowerBound=-1, b_Range=None)
    var_71 = {var_66, var_66, var_66}
    var_72 = python_code_.b_Operation(
        name=var_0, b_Operation163=var_67, b_Operation100=var_71
    )
    assert isinstance(var_72, python_code_.b_Operation)


def test_27():
    var_22 = python_code_.b_Operation(
        name="_b_Abstraction__b_Abstraction8:_b_Operation__b_Operation100"
    )
    assert isinstance(var_22, python_code_.b_Operation)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = python_code_.Expr()
    var_1 = python_code_.b_ReturnExpr()
    var_75 = python_code_.b_Assign()
    var_76 = python_code_.b_LocalOperations()
    var_77 = "b_Operation100"
    var_78 = python_code_.b_Definition(name=var_77, b_Definition81=True)
    assert isinstance(var_78, python_code_.b_Definition)
    var_81 = python_code_.b_CondNeg()
    var_83 = python_code_.b_Variable(
        name=var_77,
        b_Variable66=None,
        b_Variable38=var_75,
        b_Variable41=None,
        b_Variable79=None,
        b_Variable128=None,
        b_Variable90=None,
        b_Variable98=None,
        b_Variable132=var_77,
        b_Variable137=None,
        b_Variable142=var_1,
    )
    var_84 = python_code_.b_Ref
    var_85 = python_code_.b_Range(lowerBound=set(), b_Range=var_84, b_Range172={})
    assert isinstance(var_85, python_code_.b_Range)
    var_86 = python_code_.b_ConcreteVariables()
    var_87 = python_code_.b_Set()
    var_88 = {var_83, var_83, var_83}
    var_89 = python_code_.b_Operation(
        name=var_0, b_Operation163=var_84, b_Operation100=var_88
    )
    assert isinstance(var_89, python_code_.b_Operation)
    python_code_.b_Variable(
        name=var_76,
        b_Variable66=var_85,
        b_Variable38=var_86,
        b_Variable79=var_78,
        b_Variable53=var_81,
        b_Variable90=var_87,
        b_Variable98=var_89,
    )


def test_29():
    var_0 = python_code_.b_Definition(name="*<C2\nsL~", b_Definition83=None)
    assert isinstance(var_0, python_code_.b_Definition)
    var_2 = -1155
    python_code_.b_Range(lowerBound=var_2)


def test_30():
    var_0 = python_code_.b_Definition(name="*<C2\nsL~", b_Definition83=None)
    assert isinstance(var_0, python_code_.b_Definition)
    var_2 = -1155
    python_code_.b_Range(lowerBound=var_2, b_Range=var_0, b_Range172=None)


def test_31():
    var_0 = python_code_.b_Definition(
        name="_b_Operation__b_Operation,_b_Variable__b_Variable71,b_Values,LESS"
    )
    assert isinstance(var_0, python_code_.b_Definition)
    var_5 = "b_Operation100>"
    var_6 = python_code_.b_Definition(name=var_5, b_Definition81=True)
    assert isinstance(var_6, python_code_.b_Definition)
    var_11 = python_code_.b_Ref
    var_12 = python_code_.b_Range(lowerBound=set(), b_Range=var_11, b_Range172={})
    assert isinstance(var_12, python_code_.b_Range)


def test_32():
    var_0 = python_code_.b_ConstantExpr(
        constant="b_Variable79 b_Values33 _b_Abstraction__b_Abstraction2"
    )
    assert isinstance(var_0, python_code_.b_ConstantExpr)
    var_18 = python_code_.InequalityOp.GREATER_EQ
    var_21 = "F/#6"
    var_22 = python_code_.b_AssertionExpr()
    var_27 = lambda *args, **kwargs: 668
    var_32 = python_code_.b_AssertionExpr()
    var_52 = python_code_.b_Var()
    var_54 = python_code_.b_BoolLiteral(value=var_21, constant=var_21)
    assert isinstance(var_54, python_code_.b_BoolLiteral)
    var_56 = python_code_.b_Assign()
    var_58 = "bOperation100"
    var_59 = python_code_.b_Definition(
        name=var_58, b_Definition81=var_21, b_Definition83=var_56
    )
    assert isinstance(var_59, python_code_.b_Definition)
    python_code_.b_Abstraction(
        name="4z<A=_UM/3",
        b_Abstraction2=None,
        b_Abstraction6=None,
        b_Abstraction8=None,
        b_Abstraction31=var_32,
    )
    var_66 = python_code_.b_Case()
    python_code_.b_Variable(
        name=3792.76,
        b_Variable66=var_27,
        b_Variable128=var_18,
        b_Variable101=var_22,
        b_Variable123=var_52,
        b_Variable137=var_66,
    )


def test_33():
    var_1 = python_code_.b_ReturnExpr()
    var_70 = python_code_.b_Set()
    python_code_.b_Variable(
        name="1",
        b_Variable46=None,
        b_Variable=None,
        b_Variable53=var_70,
        b_Variable101=var_1,
        b_Variable123=None,
        b_Variable90=None,
        b_Variable137=None,
        b_Variable142=None,
        b_Variable165=None,
        b_Variable168=None,
    )


def test_34():
    var_10 = "z_"
    var_22 = python_code_.b_Operation(
        name="b_Operations95 b_Imports TRUE b_Variable98",
        b_Operation103=None,
        b_Operation97={var_10, True, 240},
    )
    assert isinstance(var_22, python_code_.b_Operation)


@pytest.mark.xfail(strict=True)
def test_35():
    var_29 = python_code_.b_LocalOperations()
    var_30 = python_code_.b_BeginBody
    python_code_.b_Operation(
        name=var_30,
        b_Operation157=complex(-1461.2, 543.7923086),
        b_Operation163=var_29,
        b_Operation97=var_30,
    )


def test_36():
    var_0 = python_code_.b_Definition(name="", b_Definition78={-2037, False, "E"})
    assert isinstance(var_0, python_code_.b_Definition)
    var_5 = python_code_.b_PropertyTyped
    var_6 = python_code_.b_InequalityExpr(op=False, b_InequalityExpr183=var_5)
    assert isinstance(var_6, python_code_.b_InequalityExpr)


def test_37():
    var_17 = "zA_"
    var_18 = python_code_.b_LogicalExpr()
    var_19 = python_code_.b_InequalityExpr(op=var_17, b_InequalityExpr=var_18)
    assert isinstance(var_19, python_code_.b_InequalityExpr)
    python_code_.b_ValueExpr(value=var_17, b_ValueExpr35=var_17)


def test_38():
    var_2 = python_code_.b_DefinitionCall()
    var_3 = "lCm9%Lq;MQ"
    var_4 = python_code_.b_LocalOperations()
    var_5 = ",\\[\ttZ\x0clF,"
    var_6 = python_code_.b_PropertyExpr()
    var_7 = python_code_.b_AndExpr
    var_8 = python_code_.b_InitialisationExpr()
    var_9 = python_code_.b_Ref()
    var_10 = python_code_.b_Variable(
        name=var_5,
        b_Variable46=False,
        b_Variable64=var_6,
        b_Variable38=var_7,
        b_Variable71=var_7,
        b_Variable53=var_8,
        b_Variable101=317,
        b_Variable123=var_6,
        b_Variable98=var_2,
        b_Variable168=var_9,
    )
    assert isinstance(var_10, python_code_.b_Variable)
    var_11 = {var_10, var_10, var_10, var_10}
    var_12 = python_code_.b_Operation(
        name=var_3, b_Operation157=None, b_Operation163=var_4, b_Operation97=var_11
    )
    assert isinstance(var_12, python_code_.b_Operation)
    var_14 = python_code_.b_StringLiteral(value=b"\x11\xec\x02")
    assert isinstance(var_14, python_code_.b_StringLiteral)


def test_39():
    var_4 = python_code_.b_BoolTest()
    var_10 = python_code_.BeginBody
    var_11 = python_code_.b_Operations()
    var_12 = python_code_.b_Operation(
        name=var_10,
        b_Operation163=False,
        b_Operation=var_11,
        b_Operation97={
            "_b_Range__b_Range172-b_Call-_b_Variable__b_Variable53": True,
            "%cT>N\nwLr[&SBxSi": "NAT:_b_Abstraction__b_Abstraction:b_PropertyExpr63",
        },
    )
    assert isinstance(var_12, python_code_.b_Operation)
    var_18 = python_code_.b_DefinitionCall()
    var_19 = set()
    var_20 = python_code_.b_Definition(
        name=var_4, b_Definition78=var_19, b_Definition83=var_18
    )
    assert isinstance(var_20, python_code_.b_Definition)
    var_22 = "r|tV$qwZgPhg<T\x0c2KVY"
    var_23 = python_code_.b_Sees()
    python_code_.b_Abstraction(
        name=var_22,
        b_Abstraction=var_23,
        b_Abstraction6=var_22,
        b_Abstraction28=-647.06,
        b_Abstraction31=var_10,
    )
