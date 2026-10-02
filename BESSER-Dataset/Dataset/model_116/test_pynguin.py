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
    DefaultValue,
    Enum,
    IfStatement,
    Visibility,
    date,
    datetime,
    dsl_AdditiveExpression,
    dsl_AllocationExpression,
    dsl_AndExpression,
    dsl_Annotation,
    dsl_AnnotationTypeBody,
    dsl_AnnotationTypeDeclaration,
    dsl_AnnotationTypeMemberDeclaration,
    dsl_ArgumentList,
    dsl_Arguments,
    dsl_ArrayDimsAndInits,
    dsl_ArrayInitializer,
    dsl_AssertStatement,
    dsl_BaseLiteral,
    dsl_Block,
    dsl_BlockStatement,
    dsl_BooleanLiteral,
    dsl_BreakStatement,
    dsl_CastExpression,
    dsl_CastLookahead,
    dsl_ClassOrInterfaceBody,
    dsl_ClassOrInterfaceBodyDeclaration,
    dsl_ClassOrInterfaceDeclaration,
    dsl_ClassOrInterfaceType,
    dsl_CommonModifier,
    dsl_CompilationUnit,
    dsl_ConditionalAndExpression,
    dsl_ConditionalExpression,
    dsl_ConditionalOrExpression,
    dsl_ContinueStatement,
    dsl_DecimalNumber,
    dsl_DefaultValue,
    dsl_DoStatement,
    dsl_EObject,
    dsl_EnumBody,
    dsl_EnumConstant,
    dsl_EnumDeclaration,
    dsl_EqualityExpression,
    dsl_ExclusiveOrExpression,
    dsl_ExplicitConstructorInvocation,
    dsl_Expression,
    dsl_ExtendsList,
    dsl_FieldDeclaration,
    dsl_FloatLiteral,
    dsl_ForInit,
    dsl_ForStatement,
    dsl_ForUpdate,
    dsl_FormalParameter,
    dsl_FormalParameters,
    dsl_IfStatement,
    dsl_ImplementsList,
    dsl_ImportDeclaration,
    dsl_InclusiveOrExpression,
    dsl_Initializer,
    dsl_InstanceOfExpression,
    dsl_IntegerLiteral,
    dsl_LabeledStatement,
    dsl_Literal,
    dsl_LocalVariableDeclaration,
    dsl_MemberSelector,
    dsl_MemberValue,
    dsl_MemberValueArrayInitializer,
    dsl_MemberValuePair,
    dsl_MemberValuePairs,
    dsl_MethodDeclarator,
    dsl_MethodOrCtorDeclaration,
    dsl_MultiplicativeExpression,
    dsl_Name,
    dsl_NameList,
    dsl_PackageDeclaration,
    dsl_PostfixExpression,
    dsl_PreDecrementExpression,
    dsl_PreIncrementExpression,
    dsl_PrimaryExpression,
    dsl_PrimaryPrefix,
    dsl_PrimarySuffix,
    dsl_ReferenceType,
    dsl_RelationalExpression,
    dsl_ResultType,
    dsl_ReturnStatement,
    dsl_ShiftExpression,
    dsl_SignedIntLiteral,
    dsl_Statement,
    dsl_StatementExpression,
    dsl_StatementExpressionList,
    dsl_SwitchLabel,
    dsl_SwitchStatement,
    dsl_SynchronizedStatement,
    dsl_ThrowStatement,
    dsl_TryStatement,
    dsl_Type,
    dsl_TypeArgument,
    dsl_TypeArguments,
    dsl_TypeBodyModifier,
    dsl_TypeBound,
    dsl_TypeDeclaration,
    dsl_TypeParameter,
    dsl_TypeParameters,
    dsl_UnaryExpression,
    dsl_UnaryExpressionNotPlusMinus,
    dsl_UnsignedIntLiteral,
    dsl_VariableDeclarator,
    dsl_VariableDeclaratorId,
    dsl_VariableInitializer,
    dsl_WhileStatement,
    dsl_WildcardBounds,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_2 = '5-f`B=~k7"B1e"'
    var_3 = python_code_.dsl_MemberValue()
    python_code_.dsl_MemberValuePair(id=var_2, dsl_MemberValuePair455=var_3)
    var_5 = "dsl_ClassOrInterfaceBodyDeclaration72"
    var_6 = python_code_.dsl_AnnotationTypeDeclaration
    var_7 = python_code_.dsl_MethodDeclarator(
        id=var_5, squareBrackets=var_3, dsl_MethodDeclarator=var_6
    )
    var_8 = False
    var_9 = False
    python_code_.dsl_TypeBodyModifier(
        native=var_8,
        transient=(False,),
        volatile=var_8,
        strictfp=None,
        synchronized=var_9,
    )
    var_11 = python_code_.dsl_ConditionalOrExpression()
    var_13 = "_dsl_MethodDeclarator__dsl_MethodDeclarator"
    var_14 = python_code_.dsl_Statement()
    var_15 = python_code_.dsl_ForUpdate()
    var_16 = python_code_.dsl_ForInit()
    var_17 = python_code_.dsl_Expression(
        assignOp=var_7, dsl_Expression157=[], dsl_Expression433=var_11
    )
    assert isinstance(var_17, python_code_.dsl_Expression)
    python_code_.dsl_ForStatement(
        id=var_13,
        dsl_ForStatement=var_14,
        dsl_ForStatement410=var_15,
        dsl_ForStatement399={"ctIkc;0-@": -597.11, "n61U!:><": -1124.14},
        dsl_ForStatement405=var_16,
        dsl_ForStatement407=var_17,
    )


def test_1():
    var_0 = "-e)>kh8.1 R&iYX\t.o"
    var_1 = "L0jdv^7F?i"
    var_2 = python_code_.dsl_BaseLiteral(
        decDigitsUnderscore=var_0,
        hexDigitsUnderscore=var_1,
        binDigitsUnderscore=var_0,
        dsl_BaseLiteral=var_1,
    )
    var_3 = True
    var_4 = python_code_.dsl_AnnotationTypeBody
    python_code_.dsl_TypeBodyModifier(
        native=var_2,
        transient=var_3,
        volatile=var_4,
        strictfp=(-1796.98, 57),
        synchronized=var_1,
        dsl_TypeBodyModifier474=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = "dsl_ImportDeclaration8 dsl_EnumBody42"
    python_code_.dsl_BreakStatement(id=var_1)
    python_code_.dsl_ArrayDimsAndInits(squareBrackets=2682)
    var_10 = "{<cEa=klj-J\\k&'"
    var_11 = "dsl_TypeArgument136"
    var_12 = python_code_.dsl_BooleanLiteral(truthiness=var_11)
    python_code_.dsl_Literal(
        charLit=complex(2239.0253206, -488.27),
        stringLit=var_10,
        nullLit=var_1,
        dsl_Literal280=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = python_code_.dsl_InstanceOfExpression()
    python_code_.dsl_VariableDeclaratorId(
        id=var_0, squareBrackets=complex(2657.035, -1122.48)
    )
    var_3 = python_code_.dsl_PackageDeclaration()
    var_4 = "9&+A"
    var_5 = "_dsl_ContinueStatement__dsl_ContinueStatement.dsl_UnsignedIntLiteral260._dsl_ClassOrInterfaceDeclaration__dsl_ClassOrInterfaceDeclaration27"
    var_6 = python_code_.dsl_PreIncrementExpression()
    var_7 = python_code_.dsl_PreDecrementExpression()
    var_8 = python_code_.dsl_PrimaryExpression()
    python_code_.dsl_StatementExpression(
        plusOp=var_4,
        minOp=var_5,
        assignOp=var_4,
        dsl_StatementExpression364=var_6,
        dsl_StatementExpression367=var_7,
        dsl_StatementExpression370=var_8,
    )
    var_10 = python_code_.dsl_UnaryExpression(
        sign=-44.16,
        dsl_UnaryExpression=var_6,
        dsl_UnaryExpression194=["I;uN~#OcE28JdX!x"],
        dsl_UnaryExpression209=var_3,
        dsl_UnaryExpression196=var_6,
    )
    python_code_.dsl_UnaryExpressionNotPlusMinus(
        negOp=set(),
        dsl_UnaryExpressionNotPlusMinus=var_10,
        dsl_UnaryExpressionNotPlusMinus211=var_10,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.dsl_ImportDeclaration()
    var_1 = python_code_.dsl_ForInit()
    var_2 = "/$\nrbI|LgGqR"
    var_3 = '"1|/2dAt!h%?JB9]j6E'
    python_code_.dsl_BaseLiteral(
        decDigitsUnderscore=complex(3775.6143, -1417.50994),
        hexDigitsUnderscore=var_2,
        binDigitsUnderscore=var_3,
    )
    var_6 = "dsl_AnnotationTypeMemberDeclaration481.dsl_TypeDeclaration19"
    python_code_.dsl_VariableDeclaratorId(id=var_6, squareBrackets="oijm'{a!V]XN4")
    python_code_.dsl_ArrayDimsAndInits(
        squareBrackets=var_1, dsl_ArrayDimsAndInits301=var_0
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "LVLy(eAKNT#MV4Q\rG"
    var_1 = python_code_.dsl_FormalParameters()
    python_code_.dsl_MethodDeclarator(
        id=var_0,
        squareBrackets=var_0,
        dsl_MethodDeclarator=var_0,
        dsl_MethodDeclarator108=var_1,
    )
    var_3 = lambda *args, **kwargs: []
    var_4 = python_code_.dsl_BaseLiteral(
        decDigitsUnderscore=var_3,
        hexDigitsUnderscore={},
        binDigitsUnderscore=var_0,
        dsl_BaseLiteral=None,
    )
    python_code_.dsl_SignedIntLiteral(bitWidth=var_3, dsl_SignedIntLiteral=var_4)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.dsl_TypeArguments()
    python_code_.dsl_AllocationExpression(
        primType=(2036.34, 3, False),
        dsl_AllocationExpression292=var_0,
        dsl_AllocationExpression295=complex(-1591.0, -1884.22),
    )
    var_6 = "E<:J."
    var_7 = "E'\"zA%kK@3g>7"
    var_8 = python_code_.dsl_SignedIntLiteral(bitWidth={})
    python_code_.dsl_BaseLiteral(
        decDigitsUnderscore=(),
        hexDigitsUnderscore=var_6,
        binDigitsUnderscore=var_7,
        dsl_BaseLiteral262=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.dsl_ArgumentList()
    var_2 = python_code_.dsl_ExclusiveOrExpression()
    var_3 = False
    var_4 = python_code_.dsl_ImplementsList
    python_code_.dsl_Initializer(static=var_3, dsl_Initializer=var_4)
    var_6 = python_code_.dsl_IfStatement()
    var_7 = python_code_.dsl_PackageDeclaration()
    var_9 = python_code_.dsl_AnnotationTypeBody()
    var_10 = "dsl_EnumDeclaration"
    var_11 = python_code_.dsl_Expression(
        assignOp=var_10,
        dsl_Expression150=var_4,
        dsl_Expression157=621,
        dsl_Expression163="O\\\\0\r8uQ%0",
        dsl_Expression=var_6,
        dsl_Expression339=var_4,
        dsl_Expression374=var_2,
        dsl_Expression377=var_4,
        dsl_Expression238=var_7,
        dsl_Expression433=1549.49,
    )
    assert isinstance(var_11, python_code_.dsl_Expression)
    python_code_.dsl_MemberSelector(id=var_3)
    python_code_.dsl_MultiplicativeExpression(ops=var_10)
    var_18 = "'_2EHMw(C@jT="
    var_19 = python_code_.dsl_UnaryExpression(sign=var_11, dsl_UnaryExpression=var_9)
    var_20 = {var_19, var_19, var_19}
    python_code_.dsl_MultiplicativeExpression(
        ops=var_18, dsl_MultiplicativeExpression191=var_20
    )
    var_23 = ">["
    var_24 = python_code_.dsl_CastLookahead(
        primType=var_10,
        bitNegOp=var_6,
        negOp=var_20,
        openBracket="Mu.7M5DiXz{r*hM$pN",
        id=var_0,
        thisOp=b"\xb0B&\xed",
        superOp=var_10,
        newOp=var_4,
    )
    python_code_.dsl_Type(primType=var_23, dsl_Type218=var_24)


@pytest.mark.xfail(strict=True)
def test_8():
    var_4 = python_code_.dsl_BreakStatement
    python_code_.dsl_DecimalNumber(
        decDigits=var_4,
        decDigitsUnderscore=(
            "_dsl_UnaryExpression__dsl_UnaryExpression.dsl_PrimaryPrefix245._dsl_Expression__dsl_Expression155",
        ),
        dsl_DecimalNumber269=var_4,
    )
    var_7 = "V_jHw5\r5KyC"
    python_code_.dsl_ShiftExpression(ops=var_7)
    var_11 = "E<:J."
    var_12 = "E'\"zA%kK@3g>7"
    var_13 = python_code_.dsl_SignedIntLiteral(bitWidth={})
    python_code_.dsl_BaseLiteral(
        decDigitsUnderscore=(),
        hexDigitsUnderscore=var_11,
        binDigitsUnderscore=var_12,
        dsl_BaseLiteral262=var_13,
    )


def test_9():
    var_0 = python_code_.dsl_TypeArguments()
    python_code_.dsl_AllocationExpression(
        primType=(2036.34, 3, False),
        dsl_AllocationExpression292=var_0,
        dsl_AllocationExpression295=complex(-1591.0, -1884.22),
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = python_code_.dsl_FormalParameter(final=set())
    var_3 = python_code_.dsl_AnnotationTypeDeclaration(
        id=var_0, dsl_AnnotationTypeDeclaration488={}
    )
    var_6 = "_dsl_BaseLiteral__dsl_BaseLiteral262"
    var_7 = python_code_.dsl_MethodDeclarator
    var_8 = python_code_.dsl_UnaryExpressionNotPlusMinus(
        negOp=var_6, dsl_UnaryExpressionNotPlusMinus=var_3
    )
    python_code_.dsl_UnaryExpression(
        sign=var_6,
        dsl_UnaryExpression194=var_7,
        dsl_UnaryExpression192={
            "_dsl_ForStatement__dsl_ForStatement412,dsl_ClassOrInterfaceBodyDeclaration63,_dsl_MemberValuePair__dsl_MemberValuePair,_dsl_Type__dsl_Type400": -2945
        },
        dsl_UnaryExpression200=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_1 = python_code_.dsl_ForInit()
    var_2 = "/$\nrbI|L^GqR"
    var_3 = '"1|/2dA?!h%?JB9]j6E'
    python_code_.dsl_BaseLiteral(
        decDigitsUnderscore=complex(3775.6143, -1417.50994),
        hexDigitsUnderscore=var_2,
        binDigitsUnderscore=var_3,
    )
    var_5 = python_code_.dsl_ConditionalOrExpression()
    var_6 = "dsl_AnnotationTypeMemberDeclaration481.dsl_TypeDeclaration19"
    var_7 = python_code_.dsl_VariableDeclaratorId(
        id=var_6,
        squareBrackets="KqpSHM.Yp5- 4Q].sPQ",
        dsl_VariableDeclaratorId117=var_5,
    )
    var_9 = python_code_.dsl_ExtendsList()
    var_10 = python_code_.dsl_ClassOrInterfaceBodyDeclaration()
    python_code_.dsl_MethodOrCtorDeclaration(
        id=var_2,
        dsl_MethodOrCtorDeclaration=var_10,
        dsl_MethodOrCtorDeclaration96=481.02,
    )
    var_12 = True
    python_code_.dsl_FormalParameter(
        final=var_12, dsl_FormalParameter=var_7, dsl_FormalParameter113=[]
    )
    var_16 = lambda *args, **kwargs: 2071
    var_17 = "|_9d5HAkD0PcjOr"
    var_18 = python_code_.dsl_ImplementsList()
    var_19 = python_code_.dsl_ClassOrInterfaceType(
        ids=var_17, dsl_ClassOrInterfaceType32=var_9, dsl_ClassOrInterfaceType35=var_18
    )
    var_20 = python_code_.dsl_TypeArguments()
    python_code_.dsl_AllocationExpression(
        primType=var_16,
        dsl_AllocationExpression289=var_19,
        dsl_AllocationExpression292=var_20,
        dsl_AllocationExpression295=var_1,
    )
