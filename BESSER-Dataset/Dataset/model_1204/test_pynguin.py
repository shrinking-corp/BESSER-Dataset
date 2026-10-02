#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    ASTNode,
    CallExp,
    CallOperationAction,
    CollectionKind,
    CollectionLiteralPart,
    CollectionType,
    EClass,
    EClassifier,
    EDataType,
    ENamedElement,
    Enum,
    FeatureCallExp,
    LiteralExp,
    LoopExp,
    NavigationCallExp,
    NumericLiteralExp,
    OCLExpression,
    PrimitiveLiteralExp,
    PrimitiveReal,
    PrimitiveType,
    SendSignalAction,
    TupleLiteralPart,
    TypedElement,
    Variable,
    abstractmethod,
    date,
    datetime,
    expressions_OCLExpression,
    expressions_ocl_EClass,
    expressions_ocl_EClassifier,
    expressions_ocl_EEnumLiteral,
    expressions_ocl_EObject,
    expressions_ocl_EOperation,
    expressions_ocl_EParameter,
    expressions_ocl_EStructuralFeature,
    ocl_expressions_AssociationClassCallExp,
    ocl_expressions_BooleanLiteralExp,
    ocl_expressions_CallExp,
    ocl_expressions_CollectionItem,
    ocl_expressions_CollectionLiteralExp,
    ocl_expressions_CollectionLiteralPart,
    ocl_expressions_CollectionRange,
    ocl_expressions_EnumLiteralExp,
    ocl_expressions_FeatureCallExp,
    ocl_expressions_IfExp,
    ocl_expressions_IntegerLiteralExp,
    ocl_expressions_InvalidLiteralExp,
    ocl_expressions_IterateExp,
    ocl_expressions_IteratorExp,
    ocl_expressions_LetExp,
    ocl_expressions_LiteralExp,
    ocl_expressions_LoopExp,
    ocl_expressions_MessageExp,
    ocl_expressions_NavigationCallExp,
    ocl_expressions_NullLiteralExp,
    ocl_expressions_NumericLiteralExp,
    ocl_expressions_OCLExpression,
    ocl_expressions_OperationCallExp,
    ocl_expressions_PrimitiveLiteralExp,
    ocl_expressions_PropertyCallExp,
    ocl_expressions_RealLiteralExp,
    ocl_expressions_StateExp,
    ocl_expressions_StringLiteralExp,
    ocl_expressions_TupleLiteralExp,
    ocl_expressions_TupleLiteralPart,
    ocl_expressions_TypeExp,
    ocl_expressions_UnspecifiedValueExp,
    ocl_expressions_Variable,
    ocl_expressions_VariableExp,
    ocl_query_Query,
    ocl_types_AnyType,
    ocl_types_BagType,
    ocl_types_CollectionType,
    ocl_types_ElementType,
    ocl_types_InvalidType,
    ocl_types_MessageType,
    ocl_types_OrderedSetType,
    ocl_types_PrimitiveBoolean,
    ocl_types_PrimitiveInteger,
    ocl_types_PrimitiveReal,
    ocl_types_PrimitiveString,
    ocl_types_PrimitiveType,
    ocl_types_SequenceType,
    ocl_types_SetType,
    ocl_types_TupleType,
    ocl_types_TypeType,
    ocl_types_VoidType,
    ocl_uml_CallOperationAction,
    ocl_uml_Constraint,
    ocl_uml_SendSignalAction,
    ocl_uml_TypedElement,
    ocl_utilities_ASTNode,
    ocl_utilities_CallingASTNode,
    ocl_utilities_PredefinedType,
    ocl_utilities_TypedASTNode,
    ocl_utilities_Visitable,
    time,
    types_ocl_EClass,
    types_ocl_EClassifier,
    types_ocl_EOperation,
    uml_TypedElement,
    uml_ocl_EClass,
    uml_ocl_EClassifier,
    uml_ocl_ENamedElement,
    uml_ocl_EOperation,
    utilities_ASTNode,
    utilities_CallingASTNode,
    utilities_PredefinedType,
    utilities_TypedASTNode,
    utilities_Visitable,
)


def test_0():
    python_code_.ocl_query_Query(extentMap="T{")


def test_1():
    var_6 = python_code_.ocl_uml_Constraint(
        instanceVarName="jMS", stereotype="_ocl_query_Query__ocl_query_Query"
    )
    assert isinstance(var_6, python_code_.ocl_uml_Constraint)


def test_2():
    var_6 = python_code_.ocl_uml_Constraint(
        instanceVarName="_Q1t-^4OyyT",
        stereotype='"2#k',
        ocl_uml_Constraint=None,
        ocl_uml_Constraint71=set(),
    )
    assert isinstance(var_6, python_code_.ocl_uml_Constraint)


def test_3():
    var_10 = python_code_.expressions_ocl_EOperation
    var_11 = python_code_.ocl_uml_Constraint(
        instanceVarName=var_10,
        stereotype=complex(428.267, 4258.019),
        ocl_uml_Constraint=var_10,
    )
    assert isinstance(var_11, python_code_.ocl_uml_Constraint)


def test_4():
    var_7 = python_code_.ocl_expressions_CollectionLiteralExp(
        kind="<pr9AQu?qRA(v6a", ocl_expressions_CollectionLiteralExp={"`C"}
    )
    assert isinstance(var_7, python_code_.ocl_expressions_CollectionLiteralExp)


def test_5():
    var_7 = python_code_.ocl_expressions_CollectionLiteralExp(kind="\x0cL1Rj>2")
    assert isinstance(var_7, python_code_.ocl_expressions_CollectionLiteralExp)


def test_6():
    var_12 = python_code_.ocl_types_CollectionType(
        kind="_ocl_uml_Constraint__ocl_uml_Constraint uml_ocl_ENamedElement collection",
        ocl_types_CollectionType=None,
    )
    assert isinstance(var_12, python_code_.ocl_types_CollectionType)


def test_7():
    var_0 = python_code_.ocl_types_CollectionType(
        kind=2098, ocl_types_CollectionType=()
    )
    assert isinstance(var_0, python_code_.ocl_types_CollectionType)


def test_8():
    python_code_.ocl_expressions_EnumLiteralExp()


def test_9():
    var_57 = python_code_.ocl_query_Query(extentMap=b"G", ocl_query_Query=True)
    assert isinstance(var_57, python_code_.ocl_query_Query)
    var_57.evaluate(ocl_objects=False)


def test_10():
    var_10 = bytes
    var_11 = python_code_.ocl_query_Query(extentMap=var_10)
    var_12 = var_11.queryText()
    var_13 = python_code_.ocl_expressions_CollectionLiteralExp(
        kind={-3443, 2570}, ocl_expressions_CollectionLiteralExp=var_12
    )
    assert isinstance(var_13, python_code_.ocl_expressions_CollectionLiteralExp)


def test_11():
    var_11 = python_code_.ocl_query_Query(extentMap=-2698.84)
    var_11.resultType()


def test_12():
    var_14 = python_code_.ocl_uml_Constraint(
        instanceVarName="kHMv\\-:|`',,0oCy",
        stereotype="_ocl_uml_Constraint__ocl_uml_Constraint OCLExpression75 _ocl_expressions_CollectionLiteralExp__ocl_expressions_CollectionLiteralExp uml_ocl_ENamedElement",
    )
    assert isinstance(var_14, python_code_.ocl_uml_Constraint)
    var_15 = "_ocl_expressions_CollectionLiteralExp__ocl_expressions_CollectionyiteralExp OCLExpression collection set"
    var_16 = python_code_.ocl_query_Query(extentMap=var_15)
    var_16.select(ocl_objects=var_14)
    var_18 = python_code_.ocl_expressions_CollectionLiteralExp(kind=var_15)
    assert isinstance(var_18, python_code_.ocl_expressions_CollectionLiteralExp)


def test_13():
    var_63 = "L}i"
    var_64 = python_code_.OCLExpression()
    var_65 = python_code_.ocl_query_Query(extentMap=var_63, ocl_query_Query=var_64)
    var_66 = lambda *args, **kwargs: "bag types_ocl_EClassifier OCLExpression69"
    var_65.reject(ocl_objects=var_66)


def test_14():
    var_0 = lambda *args, **kwargs: [True, -1491.36, 930]
    var_1 = python_code_.ocl_expressions_BooleanLiteralExp(booleanSymbol=var_0)
    assert isinstance(var_1, python_code_.ocl_expressions_BooleanLiteralExp)
    python_code_.ocl_utilities_Visitable()
    var_10 = ""
    var_11 = python_code_.ocl_query_Query(extentMap=var_10)
    var_12 = var_11.check(ocl_objects=complex(1784.2168, 3430.14084))
    var_14 = python_code_.ocl_utilities_PredefinedType()
    var_14.getRelationshipTo(ocl_type=var_14)
    var_11.select(ocl_objects=var_11)
    var_11.queryText()
    var_27 = python_code_.ocl_types_CollectionType(kind=var_12)
    assert isinstance(var_27, python_code_.ocl_types_CollectionType)
    var_33 = "bag.set._ocl_uml_Constraint__ocl_uml_Constraint71._ocl_types_CollectionType__ocl_types_CollectionType"
    var_34 = python_code_.types_ocl_EClassifier()
    python_code_.ocl_types_CollectionType(kind=var_33, ocl_types_CollectionType=var_34)


def test_15():
    python_code_.ocl_utilities_Visitable()


def test_16():
    var_0 = python_code_.ocl_utilities_PredefinedType()
    var_1 = python_code_.CallOperationAction
    var_2 = var_0.getCommonSupertype(ocl_type=var_1)
    var_4 = python_code_.ocl_utilities_Visitable()
    var_4.accept(ocl_v=var_2)
    var_8 = "CollectionLiteralPart"
    var_9 = python_code_.ocl_expressions_BooleanLiteralExp(booleanSymbol=var_8)
    assert isinstance(var_9, python_code_.ocl_expressions_BooleanLiteralExp)
    var_12 = python_code_.ocl_query_Query(extentMap=var_8)
    var_13 = python_code_.ocl_uml_Constraint(
        instanceVarName="n@73Z)#\x0b\ry/f]S)NT", stereotype=var_8
    )
    assert isinstance(var_13, python_code_.ocl_uml_Constraint)
    var_12.check(ocl_objects=var_1)
    var_0.getResultTypeFor(ocl_ownerType=var_9, ocl_opcode=var_0, ocl_args=var_0)
    var_12.select(ocl_objects=var_1)
    var_34 = "bag,_ocl_uml_Constraint__ocl_uml_Constraint,uml_ocl_ENamedElement,uml_ocl_ENamedElement"
    var_35 = python_code_.ocl_expressions_CollectionLiteralExp(kind=var_34)
    assert isinstance(var_35, python_code_.ocl_expressions_CollectionLiteralExp)
    var_12.resultType()


def test_17():
    python_code_.ocl_utilities_PredefinedType()


def test_18():
    var_0 = "OCLExpression75,types_ocl_EClassifier,CollectionLiteralPart,set"
    var_1 = python_code_.ocl_expressions_CollectionLiteralExp(
        kind=var_0, ocl_expressions_CollectionLiteralExp=var_0
    )
    assert isinstance(var_1, python_code_.ocl_expressions_CollectionLiteralExp)
    var_3 = python_code_.ocl_utilities_PredefinedType()
    var_4 = var_3.getOperationCodeFor(ocl_operName=var_1)
    var_3.getResultTypeFor(
        ocl_ownerType=var_4,
        ocl_opcode=complex(-1075.0, -269.06),
        ocl_args=complex(-1018.76, -2042.8118),
    )
    var_8 = python_code_.ocl_query_Query(extentMap=var_0)
    var_8.queryText()
    var_13 = lambda *args, **kwargs: "orderedSet"
    var_8.select(ocl_objects=var_13)


def test_19():
    var_5 = python_code_.ocl_expressions_IfExp()
    var_6 = python_code_.ocl_utilities_PredefinedType()
    var_6.getResultTypeFor(
        ocl_ownerType=None, ocl_opcode=var_5, ocl_args="e)9\x0bR3+#> mQ~hlR]"
    )
    var_11 = python_code_.ocl_types_CollectionType(kind=complex(2420.72668, 2806.20998))
    assert isinstance(var_11, python_code_.ocl_types_CollectionType)
    var_13 = python_code_.uml_ocl_EClass
    var_6.getRelationshipTo(ocl_type=var_13)


def test_20():
    var_8 = python_code_.ocl_utilities_PredefinedType()
    var_8.getOperationNameFor(ocl_opcode=())
    var_22 = "bag.set._ocl_uml_Constraint__ocl_uml_Constraint71._ocl_types_CollectionType__ocl_types_CollectionType"
    var_23 = python_code_.types_ocl_EClassifier()
    var_24 = python_code_.ocl_types_CollectionType(
        kind=var_22, ocl_types_CollectionType=var_23
    )
    assert isinstance(var_24, python_code_.ocl_types_CollectionType)


def test_21():
    var_21 = python_code_.ocl_expressions_IntegerLiteralExp(
        integerSymbol='D\\&5"&Tk6VJO/G<E2'
    )
    assert isinstance(var_21, python_code_.ocl_expressions_IntegerLiteralExp)


def test_22():
    var_65 = python_code_.ocl_expressions_StringLiteralExp(
        stringSymbol=b"^\x03*\xa6\xff9%\xe0EA\xa5&3\xbd\x88\x0e\xe9\xa0&"
    )
    assert isinstance(var_65, python_code_.ocl_expressions_StringLiteralExp)


def test_23():
    var_17 = python_code_.ocl_expressions_BooleanLiteralExp(
        booleanSymbol="_ocl_uml_Constraint__ocl_uml_ConstraintOCLExpressionOCLExpression69"
    )
    assert isinstance(var_17, python_code_.ocl_expressions_BooleanLiteralExp)


def test_24():
    var_10 = python_code_.ocl_types_PrimitiveBoolean
    var_14 = python_code_.ocl_uml_Constraint(
        instanceVarName=">lv\\3UOe",
        stereotype="uml_ocl_ENamedElement",
        ocl_uml_Constraint=var_10,
    )
    assert isinstance(var_14, python_code_.ocl_uml_Constraint)
    var_17 = python_code_.ocl_utilities_PredefinedType()
    var_17.getOperations()


def test_25():
    var_63 = python_code_.ocl_utilities_ASTNode(startPosition=3008, endPosition=0)
    assert isinstance(var_63, python_code_.ocl_utilities_ASTNode)


def test_26():
    var_57 = python_code_.ocl_query_Query(extentMap=b"G", ocl_query_Query=True)
    assert isinstance(var_57, python_code_.ocl_query_Query)


def test_27():
    var_3 = python_code_.ocl_utilities_TypedASTNode(
        typeStartPosition="Qq8@b3?g7'O", typeEndPosition='?y.Bo\x0cs(\t0WA6En"'
    )
    assert isinstance(var_3, python_code_.ocl_utilities_TypedASTNode)


def test_28():
    var_14 = python_code_.ocl_uml_Constraint(
        instanceVarName="_ocl_uml_Constraint__ocl_uml_Constraint",
        stereotype="bag OCLExpression75",
    )
    assert isinstance(var_14, python_code_.ocl_uml_Constraint)
    var_23 = python_code_.ocl_expressions_RealLiteralExp(realSymbol=var_14)
    assert isinstance(var_23, python_code_.ocl_expressions_RealLiteralExp)


def test_29():
    var_45 = -255
    var_0 = python_code_.ocl_utilities_CallingASTNode(
        propertyStartPosition=True, propertyEndPosition=var_45
    )
    assert isinstance(var_0, python_code_.ocl_utilities_CallingASTNode)
    var_1 = python_code_.ocl_query_Query(extentMap=[])
    var_1.queryText()
    var_8 = python_code_.ocl_expressions_IntegerLiteralExp(
        integerSymbol={"z@(YIruP", -217.04}
    )
    assert isinstance(var_8, python_code_.ocl_expressions_IntegerLiteralExp)
    var_12 = ""
    var_13 = python_code_.ocl_uml_Constraint(
        instanceVarName=var_12, stereotype=var_12, ocl_uml_Constraint=var_0
    )
    assert isinstance(var_13, python_code_.ocl_uml_Constraint)
    var_15 = python_code_.ocl_utilities_PredefinedType()
    var_16 = python_code_.ocl_types_SequenceType
    var_15.getOperationNameFor(ocl_opcode=var_16)
    var_42 = "bag.set._ocl_uml_Constraint__ocl_uml_Constraint71._ocl_types_CollectionType__ocl_types_CollectionType"
    var_43 = python_code_.types_ocl_EClassifier()
    var_44 = python_code_.ocl_types_CollectionType(
        kind=var_42, ocl_types_CollectionType=var_43
    )
    assert isinstance(var_44, python_code_.ocl_types_CollectionType)


def test_30():
    var_13 = python_code_.ocl_expressions_FeatureCallExp(markedPre=[])
    assert isinstance(var_13, python_code_.ocl_expressions_FeatureCallExp)
