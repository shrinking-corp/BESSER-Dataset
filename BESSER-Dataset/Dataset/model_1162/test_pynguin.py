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
    ATL_ActionBlock,
    ATL_Binding,
    ATL_BindingStat,
    ATL_CalledRule,
    ATL_ExpressionStat,
    ATL_ForEachOutPatternElement,
    ATL_ForStat,
    ATL_Helper,
    ATL_IfStat,
    ATL_InPattern,
    ATL_InPatternElement,
    ATL_LazyMatchedRule,
    ATL_Library,
    ATL_LibraryRef,
    ATL_LocatedElement,
    ATL_MatchedRule,
    ATL_Module,
    ATL_ModuleElement,
    ATL_OutPattern,
    ATL_OutPatternElement,
    ATL_PatternElement,
    ATL_Query,
    ATL_Rule,
    ATL_RuleVariableDeclaration,
    ATL_SimpleInPatternElement,
    ATL_SimpleOutPatternElement,
    ATL_Statement,
    ATL_Unit,
    ActionBlock,
    Attribute,
    Binding,
    CollectionExp,
    CollectionType,
    Helper,
    IfExp,
    InPattern,
    InPatternElement,
    IterateExp,
    Iterator,
    LetExp,
    Library,
    LibraryRef,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
    MatchedRule,
    Module,
    ModuleElement,
    NumericExp,
    NumericType,
    OCL_Attribute,
    OCL_BagExp,
    OCL_BagType,
    OCL_BooleanExp,
    OCL_BooleanType,
    OCL_CollectionExp,
    OCL_CollectionOperationCallExp,
    OCL_CollectionType,
    OCL_EnumLiteralExp,
    OCL_IfExp,
    OCL_IntegerExp,
    OCL_IntegerType,
    OCL_IterateExp,
    OCL_Iterator,
    OCL_IteratorExp,
    OCL_LetExp,
    OCL_LoopExp,
    OCL_MapElement,
    OCL_MapExp,
    OCL_MapType,
    OCL_NavigationOrAttributeCallExp,
    OCL_NumericExp,
    OCL_NumericType,
    OCL_OclAnyType,
    OCL_OclContextDefinition,
    OCL_OclExpression,
    OCL_OclFeature,
    OCL_OclFeatureDefinition,
    OCL_OclModel,
    OCL_OclModelElement,
    OCL_OclType,
    OCL_OclUndefinedExp,
    OCL_Operation,
    OCL_OperationCallExp,
    OCL_OperatorCallExp,
    OCL_OrderedSetExp,
    OCL_OrderedSetType,
    OCL_Parameter,
    OCL_Primitive,
    OCL_PrimitiveExp,
    OCL_PropertyCallExp,
    OCL_RealExp,
    OCL_RealType,
    OCL_SequenceExp,
    OCL_SequenceType,
    OCL_SetExp,
    OCL_SetType,
    OCL_StringExp,
    OCL_StringType,
    OCL_SuperExp,
    OCL_TupleExp,
    OCL_TuplePart,
    OCL_TupleType,
    OCL_TupleTypeAttribute,
    OCL_VariableDeclaration,
    OCL_VariableExp,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclModel,
    OclModelElement,
    OclType,
    Operation,
    OperationCallExp,
    OutPattern,
    OutPatternElement,
    Parameter,
    PatternElement,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    Query,
    Rule,
    RuleVariableDeclaration,
    Statement,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    Unit,
    VariableDeclaration,
    VariableExp,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_62 = python_code_.OCL_Attribute(name=";H31)66fDH5")
    assert isinstance(var_62, python_code_.OCL_Attribute)


def test_1():
    var_48 = python_code_.OCL_StringType()
    var_51 = python_code_.ATL_LazyMatchedRule(isUnique=1)
    assert isinstance(var_51, python_code_.ATL_LazyMatchedRule)
    var_55 = python_code_.OCL_Attribute(
        name=var_48, owningAttribute=207.92, attribute=(False,)
    )
    assert isinstance(var_55, python_code_.OCL_Attribute)


def test_2():
    var_25 = 'Z%="S~mL|e4'
    var_27 = python_code_.OCL_OperationCallExp(operationName=var_25)
    assert isinstance(var_27, python_code_.OCL_OperationCallExp)


def test_3():
    var_21 = python_code_.OCL_IntegerExp(integerSymbol="wk\x0c\r1x_s")
    assert isinstance(var_21, python_code_.OCL_IntegerExp)
    var_40 = python_code_.OCL_LoopExp()
    var_42 = python_code_.ATL_IfStat()
    var_43 = python_code_.ATL_BindingStat(
        propertyName=True,
        isAssignment=var_40,
        ATL_BindingStat=b"\x04\x1c\xb8\xce\x1c",
        Statement80=var_42,
        Statement77=-719.99,
    )
    assert isinstance(var_43, python_code_.ATL_BindingStat)


def test_4():
    var_0 = python_code_.MapElement()
    var_40 = "wm"
    var_41 = python_code_.ATL_BindingStat(
        propertyName=var_0, isAssignment=var_40, ATL_BindingStat71="BHTd$SE~Uv]6\r+/4CE"
    )
    assert isinstance(var_41, python_code_.ATL_BindingStat)


@pytest.mark.xfail(strict=True)
def test_5():
    var_8 = python_code_.ATL_RuleVariableDeclaration()
    var_9 = python_code_.MatchedRule()
    var_11 = python_code_.InPattern()
    var_12 = "\n1pjS+'/h IP"
    var_13 = lambda *args, **kwargs: -956
    python_code_.ATL_MatchedRule(
        isAbstract=var_12,
        isRefining=var_12,
        isNoDefault=var_13,
        superRule=var_9,
        Rule61=var_8,
        Rule=None,
        Rule64=var_11,
    )


def test_6():
    var_0 = "W`U|;qD"
    var_1 = []
    var_2 = python_code_.ATL_MatchedRule(
        isAbstract=var_0, isRefining=var_0, isNoDefault=var_1, Rule61=var_0
    )
    assert isinstance(var_2, python_code_.ATL_MatchedRule)


def test_7():
    var_45 = python_code_.OCL_SuperExp()
    var_48 = python_code_.OCL_StringType()
    var_49 = python_code_.OCL_OclFeatureDefinition()
    var_51 = python_code_.ATL_LazyMatchedRule(isUnique=1)
    assert isinstance(var_51, python_code_.ATL_LazyMatchedRule)
    var_52 = python_code_.ATL_MatchedRule(
        isAbstract=(False,), isRefining=var_45, isNoDefault=var_49, children=var_51
    )
    assert isinstance(var_52, python_code_.ATL_MatchedRule)
    var_55 = python_code_.OCL_Attribute(
        name=var_48, owningAttribute=207.92, attribute=(False,)
    )
    assert isinstance(var_55, python_code_.OCL_Attribute)


def test_8():
    var_20 = python_code_.ATL_OutPattern()
    var_25 = set()
    var_26 = python_code_.ATL_Rule(name=var_20, rule19=var_25)
    assert isinstance(var_26, python_code_.ATL_Rule)


def test_9():
    var_0 = python_code_.OCL_TuplePart()
    var_3 = python_code_.OCL_IntegerExp(integerSymbol=False)
    assert isinstance(var_3, python_code_.OCL_IntegerExp)
    var_7 = 'j|"a'
    var_18 = python_code_.OCL_IteratorExp(name=var_7)
    assert isinstance(var_18, python_code_.OCL_IteratorExp)
    var_21 = python_code_.OCL_OclModel(name=var_7)
    assert isinstance(var_21, python_code_.OCL_OclModel)
    var_26 = python_code_.OCL_NumericType()
    var_29 = "VariableDeclaration171"
    var_30 = python_code_.OCL_VariableDeclaration(id=var_0, varName={})
    assert isinstance(var_30, python_code_.OCL_VariableDeclaration)
    var_31 = python_code_.ATL_ForStat()
    var_32 = python_code_.ATL_ForStat
    var_33 = python_code_.OCL_OclType(
        name=var_29,
        type=var_21,
        returnType=var_26,
        OclExpression144=var_30,
        OclExpression85=var_31,
        OclExpression121=var_32,
    )
    assert isinstance(var_33, python_code_.OCL_OclType)


def test_10():
    var_0 = "Operation159 OclType175 LetExp _OCL_OclType__context_"
    var_8 = "LBLY0"
    var_9 = python_code_.OCL_NavigationOrAttributeCallExp(name=var_8)
    assert isinstance(var_9, python_code_.OCL_NavigationOrAttributeCallExp)
    var_10 = python_code_.OCL_RealType()
    var_12 = python_code_.MapType()
    var_13 = lambda *args, **kwargs: []
    var_16 = python_code_.OCL_PropertyCallExp()
    var_17 = python_code_.OCL_OclType(
        name="q [57eh",
        type=None,
        returnType=None,
        valueType=var_12,
        elementType=var_0,
        OclExpression85=var_10,
        OclExpression134=None,
        OclExpression51=None,
        OclExpression157=None,
        OclExpression119=var_10,
        OclExpression67=var_16,
        OclExpression31=var_0,
        OclExpression136=None,
        OclExpression121=None,
        OclExpression57=None,
        OclExpression125=var_12,
    )
    assert isinstance(var_17, python_code_.OCL_OclType)
    var_18 = python_code_.OCL_BooleanExp(booleanSymbol=complex(1011.59, 1867.11))
    assert isinstance(var_18, python_code_.OCL_BooleanExp)
    var_21 = "I"
    var_22 = "h=J{h:"
    var_23 = python_code_.ATL_RuleVariableDeclaration()
    var_24 = python_code_.ATL_CalledRule(
        isEntrypoint=var_21, isEndpoint=var_22, Rule61=var_23, Rule64=var_13
    )
    assert isinstance(var_24, python_code_.ATL_CalledRule)
    var_27 = python_code_.OCL_BagType()
    var_28 = python_code_.OCL_TupleTypeAttribute(name=var_27)
    assert isinstance(var_28, python_code_.OCL_TupleTypeAttribute)


def test_11():
    var_7 = python_code_.Attribute()
    var_9 = "*S'9W9<2}4rzZ|D\x0cn"
    var_10 = python_code_.OCL_OperationCallExp(operationName=var_9)
    assert isinstance(var_10, python_code_.OCL_OperationCallExp)
    var_13 = python_code_.InPatternElement()
    var_16 = python_code_.TupleTypeAttribute
    var_17 = python_code_.OCL_VariableDeclaration(
        id=var_9, varName=var_16, result={"A'nOz^\"`g": -71.52}
    )
    assert isinstance(var_17, python_code_.OCL_VariableDeclaration)
    var_21 = python_code_.ATL_LibraryRef(name=var_16)
    assert isinstance(var_21, python_code_.ATL_LibraryRef)
    var_24 = python_code_.OCL_OperationCallExp(
        operationName=var_9, parentOperation={">$?5R2"}
    )
    assert isinstance(var_24, python_code_.OCL_OperationCallExp)
    var_29 = "rbUL\\\\\\"
    var_30 = python_code_.OCL_TupleTypeAttribute(name=var_29)
    assert isinstance(var_30, python_code_.OCL_TupleTypeAttribute)
    var_31 = python_code_.ATL_ForEachOutPatternElement()
    var_32 = "L,Ppu3G8"
    var_33 = python_code_.ATL_BindingStat(
        propertyName=var_31, isAssignment=var_32, Statement80={}, Statement88=var_21
    )
    assert isinstance(var_33, python_code_.ATL_BindingStat)
    var_34 = python_code_.ATL_ForStat()
    var_35 = python_code_.OCL_MapElement()
    var_36 = python_code_.OCL_OclType(
        name=var_7,
        context_=(),
        returnType=-509.18,
        type162="OclExpression123",
        keyType=var_13,
        OclExpression140=var_16,
        OclExpression69=var_33,
        OclExpression123=var_10,
        OclExpression53=None,
        OclExpression138=var_16,
        OclExpression85=var_34,
        OclExpression157=var_16,
        OclExpression119=var_35,
        OclExpression125=var_21,
    )
    assert isinstance(var_36, python_code_.OCL_OclType)
    var_37 = python_code_.OCL_NavigationOrAttributeCallExp(name=(False,))
    assert isinstance(var_37, python_code_.OCL_NavigationOrAttributeCallExp)


def test_12():
    var_1 = python_code_.OCL_SuperExp()
    var_2 = "LBLY0"
    var_3 = python_code_.OCL_NavigationOrAttributeCallExp(name=var_2)
    assert isinstance(var_3, python_code_.OCL_NavigationOrAttributeCallExp)
    var_4 = python_code_.OCL_RealType()
    var_5 = python_code_.OCL_LetExp()
    var_6 = python_code_.MapType()
    var_7 = lambda *args, **kwargs: []
    var_8 = python_code_.ATL_BindingStat(
        propertyName={2835, -3122.97},
        isAssignment=var_2,
        ATL_BindingStat71=var_1,
        Statement80=var_6,
        Statement77=False,
    )
    assert isinstance(var_8, python_code_.ATL_BindingStat)
    var_9 = "OclExpression123"
    var_10 = python_code_.ATL_Query()
    var_11 = python_code_.OCL_PropertyCallExp()
    var_12 = python_code_.OCL_OclType(
        name=var_9,
        OclExpression140=var_4,
        OclExpression196=var_7,
        OclExpression72=var_7,
        OclExpression=var_10,
        OclExpression157=var_5,
        OclExpression116=complex(-576.20784, 810.137),
        OclExpression121=var_11,
        OclExpression125=var_2,
    )
    assert isinstance(var_12, python_code_.OCL_OclType)
    python_code_.OCL_OclType(
        name=b"\xb7BO\xe9_4\t\x8er\xdc%=\x1b\x8a",
        type=var_1,
        valueType=var_6,
        type162=var_7,
        elementType=-599,
        type170=None,
        OclExpression144=b"h\xc7TU",
        OclExpression69=var_8,
        OclExpression196=var_6,
        OclExpression85=2611.7,
        OclExpression157=var_12,
    )
    var_14 = python_code_.OCL_BooleanExp(booleanSymbol=complex(1011.59, 1867.11))
    assert isinstance(var_14, python_code_.OCL_BooleanExp)
    var_17 = "I"
    var_18 = "A=J{h:"
    var_19 = python_code_.ATL_RuleVariableDeclaration()
    var_20 = python_code_.ATL_CalledRule(
        isEntrypoint=var_17, isEndpoint=var_18, Rule61=var_19, Rule64=var_7
    )
    assert isinstance(var_20, python_code_.ATL_CalledRule)
    var_23 = ";@"
    var_24 = python_code_.OCL_TupleTypeAttribute(name=var_23)
    assert isinstance(var_24, python_code_.OCL_TupleTypeAttribute)


def test_13():
    var_0 = python_code_.MapElement()
    var_2 = python_code_.OCL_Iterator()
    var_3 = "Np@8o^O&VKk&h6`$;jd"
    var_4 = python_code_.OCL_VariableDeclaration(
        id=var_3, varName=var_0, initializedVariable=var_2
    )
    assert isinstance(var_4, python_code_.OCL_VariableDeclaration)
    var_30 = python_code_.OCL_Attribute(name=var_3)
    assert isinstance(var_30, python_code_.OCL_Attribute)
    var_31 = python_code_.OCL_OperationCallExp(operationName=var_3)
    assert isinstance(var_31, python_code_.OCL_OperationCallExp)
    var_33 = python_code_.OCL_OclModel(name=var_3)
    assert isinstance(var_33, python_code_.OCL_OclModel)


def test_14():
    var_37 = "*S'9W9<2}4rzZ|D\x0cn"
    var_38 = python_code_.OCL_OperationCallExp(operationName=";e\\=.@W=~2mb2;Nl@/\x0c")
    assert isinstance(var_38, python_code_.OCL_OperationCallExp)
    var_44 = python_code_.TupleTypeAttribute
    var_45 = python_code_.OCL_VariableDeclaration(
        id=var_37, varName=var_44, result={"A'nOz^\"`g": -71.52}
    )
    assert isinstance(var_45, python_code_.OCL_VariableDeclaration)


def test_15():
    var_3 = python_code_.OCL_IntegerExp(integerSymbol=False)
    assert isinstance(var_3, python_code_.OCL_IntegerExp)
    var_7 = 'j|"a'
    var_8 = python_code_.OCL_Attribute(name=var_7)
    assert isinstance(var_8, python_code_.OCL_Attribute)
    var_18 = python_code_.OCL_IteratorExp(name=var_7)
    assert isinstance(var_18, python_code_.OCL_IteratorExp)
    var_21 = python_code_.OCL_OclModel(name=var_7)
    assert isinstance(var_21, python_code_.OCL_OclModel)
    var_26 = lambda *args, **kwargs: False
    var_27 = python_code_.VariableExp()
    var_28 = {var_27, var_27}
    var_29 = python_code_.OCL_VariableDeclaration(
        id=var_26, varName=b"\xe6\xc1X\x8b~\xd6\xf0", referredVariable=var_28
    )
    assert isinstance(var_29, python_code_.OCL_VariableDeclaration)


def test_16():
    var_52 = ";@"
    var_53 = python_code_.OCL_TupleTypeAttribute(name=var_52)
    assert isinstance(var_53, python_code_.OCL_TupleTypeAttribute)


def test_17():
    var_32 = 'Z%="S~mL|Ze4'
    var_35 = python_code_.OCL_OclModel(name=var_32)
    assert isinstance(var_35, python_code_.OCL_OclModel)


def test_18():
    var_1 = python_code_.ATL_LibraryRef(
        name="MapType165-OCL_LoopExp-ATL_ForEachOutPatternElement-_ATL_LibraryRef__libraries"
    )
    assert isinstance(var_1, python_code_.ATL_LibraryRef)


def test_19():
    var_43 = "VariableDeclWaration171"
    var_47 = python_code_.ATL_Query()
    var_48 = python_code_.ATL_LibraryRef(name=var_43, libraries=var_47)
    assert isinstance(var_48, python_code_.ATL_LibraryRef)


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = "W`U|;D'"
    var_57 = python_code_.InPatternElement()
    var_60 = "OCL_CollectionExp:IterateExp:LetExp146"
    var_61 = python_code_.OCL_VariableExp()
    var_71 = python_code_.ATL_Binding(
        propertyName=1692.26, isAssignment=var_61, bindings=var_60
    )
    assert isinstance(var_71, python_code_.ATL_Binding)
    python_code_.ATL_Unit(name=var_0, unit=var_57)


def test_21():
    var_21 = python_code_.OCL_IntegerExp(integerSymbol="wk\x0c\r1x_s")
    assert isinstance(var_21, python_code_.OCL_IntegerExp)
    var_25 = "KW"
    var_27 = python_code_.OCL_OperationCallExp(operationName=var_25)
    assert isinstance(var_27, python_code_.OCL_OperationCallExp)
    var_30 = python_code_.OCL_NavigationOrAttributeCallExp(name=var_25)
    assert isinstance(var_30, python_code_.OCL_NavigationOrAttributeCallExp)


def test_22():
    var_0 = "Operation159 OclType175 LetExp _OCL_OclType__context_"
    var_1 = python_code_.ATL_LibraryRef(name=False)
    assert isinstance(var_1, python_code_.ATL_LibraryRef)
    var_2 = python_code_.ATL_Module(isRefining=var_0, Unit=var_1)
    assert isinstance(var_2, python_code_.ATL_Module)
    var_3 = "emCU(=K59Ut+,''n"
    var_4 = python_code_.OCL_RealExp(realSymbol=var_3)
    assert isinstance(var_4, python_code_.OCL_RealExp)


def test_23():
    var_1 = (
        "TupleTypeAttribute._OCL_Operation__owningOperation.OCL_LoopExp.ATL_OutPattern"
    )
    var_2 = python_code_.ATL_LocatedElement(
        location=var_1,
        commentsBefore="OclExpression-_OCL_VariableDeclaration__referredVariable-OCL_OclType",
        commentsAfter=var_1,
    )
    assert isinstance(var_2, python_code_.ATL_LocatedElement)
    var_4 = python_code_.OclFeature()
    var_7 = python_code_.OCL_StringExp(stringSymbol=False)
    assert isinstance(var_7, python_code_.OCL_StringExp)
    var_11 = python_code_.OCL_MapExp
    var_12 = python_code_.ATL_ExpressionStat()
    var_13 = python_code_.OCL_IfExp()
    var_14 = python_code_.OCL_LoopExp()
    var_15 = python_code_.OCL_EnumLiteralExp(
        name=complex(4476.6, 2135.967077),
        OclExpression69=var_11,
        OclExpression123={True},
        OclExpression134=var_4,
        OclExpression119={},
        OclExpression67=var_12,
        OclExpression136=var_13,
        OclExpression125=var_14,
    )
    assert isinstance(var_15, python_code_.OCL_EnumLiteralExp)


def test_24():
    var_10 = python_code_.OCL_IteratorExp(name=False)
    assert isinstance(var_10, python_code_.OCL_IteratorExp)


def test_25():
    var_45 = python_code_.OCL_StringType()
    var_48 = python_code_.ATL_LazyMatchedRule(isUnique=1)
    assert isinstance(var_48, python_code_.ATL_LazyMatchedRule)
    var_49 = python_code_.OCL_LetExp()
    var_50 = python_code_.OCL_Attribute(
        name=var_45, owningAttribute=207.92, attribute=(False,)
    )
    assert isinstance(var_50, python_code_.OCL_Attribute)
    var_52 = python_code_.OCL_TupleTypeAttribute
    var_53 = python_code_.ATL_LocatedElement(
        location=var_49,
        commentsBefore=var_52,
        commentsAfter=b"\xae+\xc7wU\x0fE\xca\xa2$\x8f\xc4\xdf\x8e\xe5/\xb5\x8d>",
    )
    assert isinstance(var_53, python_code_.ATL_LocatedElement)


def test_26():
    var_1 = " TR\x0cX J+\ng8\x0b"
    var_2 = python_code_.OCL_TupleExp
    var_3 = python_code_.ATL_BindingStat(propertyName=var_1, isAssignment=var_2)
    assert isinstance(var_3, python_code_.ATL_BindingStat)
    var_9 = "OCL_CollectionExp:IterateExp:LetExp146"
    var_10 = python_code_.OCL_VariableExp()
    var_11 = {var_10, var_10, var_10, var_10}
    var_12 = python_code_.OCL_OperationCallExp(
        operationName=var_9, parentOperation=var_11, PropertyCallExp=var_2
    )
    assert isinstance(var_12, python_code_.OCL_OperationCallExp)
    var_13 = python_code_.OCL_PropertyCallExp()
    var_14 = python_code_.OCL_Operation(
        name=var_2,
        operation202=b"\xbc\xb3\xfc\xe8Z^\x04/W0\xd4",
        owningOperation=var_13,
    )
    assert isinstance(var_14, python_code_.OCL_Operation)
    var_20 = python_code_.ATL_Binding(
        propertyName=1692.26, isAssignment=var_10, bindings=var_9
    )
    assert isinstance(var_20, python_code_.ATL_Binding)
    var_22 = python_code_.ATL_Module(isRefining=var_9, ATL_Module7=var_11, Unit=2297)
    assert isinstance(var_22, python_code_.ATL_Module)
    var_24 = "OCL_LoopExp"
    python_code_.OCL_OperationCallExp(operationName=var_24)
    var_33 = python_code_.ATL_LibraryRef(name=var_2)
    assert isinstance(var_33, python_code_.ATL_LibraryRef)


def test_27():
    var_29 = python_code_.NumericExp()
    var_62 = python_code_.OCL_Operation(
        name="OclModel211", operation={119, True, var_29}
    )
    assert isinstance(var_62, python_code_.OCL_Operation)
    var_66 = python_code_.OCL_OclModel(name=None, model=[True, False, "^Kky<`J<(4"])
    assert isinstance(var_66, python_code_.OCL_OclModel)


def test_28():
    var_1 = " TR\x0cX J+\ng8\x0b"
    var_2 = python_code_.MatchedRule
    var_3 = python_code_.ATL_BindingStat(propertyName=var_1, isAssignment=var_2)
    assert isinstance(var_3, python_code_.ATL_BindingStat)
    var_13 = python_code_.OCL_PropertyCallExp()
    var_14 = python_code_.OCL_Operation(
        name=var_2,
        operation202=b"\xbc\xb3\xfc\xe8Z^\x04/W0\xd4",
        owningOperation=var_13,
    )
    assert isinstance(var_14, python_code_.OCL_Operation)
    var_24 = "OCL_LoopExp"
    var_25 = python_code_.OCL_OperationCallExp(operationName=var_24)
    assert isinstance(var_25, python_code_.OCL_OperationCallExp)
    var_33 = python_code_.ATL_LibraryRef(name=var_2)
    assert isinstance(var_33, python_code_.ATL_LibraryRef)


def test_29():
    var_0 = python_code_.OclModel
    var_1 = python_code_.OCL_IntegerExp(integerSymbol=var_0)
    assert isinstance(var_1, python_code_.OCL_IntegerExp)
    var_5 = python_code_.OCL_Attribute(name=var_0)
    assert isinstance(var_5, python_code_.OCL_Attribute)
    var_46 = python_code_.ATL_OutPattern()
    var_52 = python_code_.ATL_Rule(name="OclExpression144", ModuleElement=var_46)
    assert isinstance(var_52, python_code_.ATL_Rule)
    var_59 = python_code_.OCL_NavigationOrAttributeCallExp(name=(False,))
    assert isinstance(var_59, python_code_.OCL_NavigationOrAttributeCallExp)


def test_30():
    var_0 = python_code_.MapElement()
    var_2 = python_code_.OCL_Iterator()
    var_3 = "Np@8o^O&VKk&h6`$;jd"
    var_4 = python_code_.OCL_VariableDeclaration(
        id=var_3, varName=var_0, initializedVariable=var_2
    )
    assert isinstance(var_4, python_code_.OCL_VariableDeclaration)
    var_30 = python_code_.OCL_Attribute(name=var_3)
    assert isinstance(var_30, python_code_.OCL_Attribute)
    var_33 = python_code_.OCL_OclModel(
        name="Kpz~", model=var_0, model209=set(), metamodel=set()
    )
    assert isinstance(var_33, python_code_.OCL_OclModel)


def test_31():
    var_21 = python_code_.OCL_IntegerExp(integerSymbol="wk\x0c\r1x_s")
    assert isinstance(var_21, python_code_.OCL_IntegerExp)
    var_25 = "KW"
    var_27 = python_code_.OCL_OperationCallExp(operationName=var_25)
    assert isinstance(var_27, python_code_.OCL_OperationCallExp)
    var_29 = ","
    var_30 = python_code_.OCL_NavigationOrAttributeCallExp(name=var_29)
    assert isinstance(var_30, python_code_.OCL_NavigationOrAttributeCallExp)
    var_35 = python_code_.ATL_Binding(propertyName=-1757.91, isAssignment=var_25)
    assert isinstance(var_35, python_code_.ATL_Binding)


def test_32():
    var_37 = python_code_.LoopExp()
    var_40 = python_code_.OCL_LoopExp()
    var_42 = python_code_.ATL_IfStat()
    var_43 = python_code_.ATL_BindingStat(
        propertyName=True,
        isAssignment=var_40,
        ATL_BindingStat=b"\x04\x1c\xb8\xce\x1c",
        Statement80=var_42,
        Statement77=-719.99,
    )
    assert isinstance(var_43, python_code_.ATL_BindingStat)
    var_44 = python_code_.OCL_TupleTypeAttribute(
        name={-4432.27, "{M]W5())?ohK"}, attributes=var_37
    )
    assert isinstance(var_44, python_code_.OCL_TupleTypeAttribute)


def test_33():
    var_20 = python_code_.ATL_OutPattern()
    var_26 = python_code_.ATL_Rule(
        name="rV~M=*5bg3",
        rule=var_20,
        rule17=None,
        rule19={"_ATL_BindingStat__ATL_BindingStatLibraryRefOclExpression", 631.29},
        ModuleElement=None,
    )
    assert isinstance(var_26, python_code_.ATL_Rule)


@pytest.mark.xfail(strict=True)
def test_34():
    var_21 = python_code_.OCL_IntegerExp(integerSymbol="wk\x0c\r1x_s")
    assert isinstance(var_21, python_code_.OCL_IntegerExp)
    var_22 = python_code_.OCL_PrimitiveExp()
    var_25 = "KW"
    var_27 = python_code_.OCL_OperationCallExp(operationName=var_25)
    assert isinstance(var_27, python_code_.OCL_OperationCallExp)
    var_29 = ","
    var_30 = python_code_.OCL_NavigationOrAttributeCallExp(name=var_25)
    assert isinstance(var_30, python_code_.OCL_NavigationOrAttributeCallExp)
    var_33 = lambda *args, **kwargs: -1512
    var_34 = python_code_.ATL_Binding(propertyName=var_29, isAssignment=var_33)
    assert isinstance(var_34, python_code_.ATL_Binding)
    var_36 = "t4~2FrPg5cEks"
    python_code_.ATL_CalledRule(
        isEntrypoint=var_36, isEndpoint=var_22, ATL_CalledRule=True
    )


def test_35():
    var_0 = python_code_.OclModel()
    var_1 = python_code_.OclModel()
    var_2 = {var_0, var_0, var_1}
    var_3 = python_code_.ATL_Module(
        isRefining=True, ATL_Module=var_2, ATL_Module7=var_2, module=var_2
    )
    assert isinstance(var_3, python_code_.ATL_Module)
    var_5 = python_code_.NumericExp()
    var_9 = python_code_.OCL_OperationCallExp(operationName=var_5, PropertyCallExp=1440)
    assert isinstance(var_9, python_code_.OCL_OperationCallExp)
    var_12 = python_code_.OCL_NavigationOrAttributeCallExp(
        name=2837, PropertyCallExp=var_5
    )
    assert isinstance(var_12, python_code_.OCL_NavigationOrAttributeCallExp)
    var_14 = '`nu<T{wu5O~"S^Qld,U'
    var_15 = python_code_.ATL_ForStat()
    var_16 = python_code_.ATL_BindingStat(
        propertyName=var_14, isAssignment=var_14, Statement88=var_15
    )
    assert isinstance(var_16, python_code_.ATL_BindingStat)
    var_21 = "uHz"
    var_22 = python_code_.OclModel()
    var_23 = python_code_.OCL_OclModel(name=var_21, model=var_22, model209=var_2)
    assert isinstance(var_23, python_code_.OCL_OclModel)


def test_36():
    var_56 = "_OCL_OclType__context_ATL_RuleVariableDeclarationModuleElement"
    var_57 = python_code_.InPattern()
    var_0 = python_code_.ATL_MatchedRule(
        isAbstract={
            -1609.69,
            1976,
            "OclExpression,_OCL_VariableDeclaration__initializedVariable,ATL_IfStat",
        },
        isRefining=complex(-3832.902, -329.501548),
        isNoDefault=var_56,
        rule21=var_57,
        children=1134.72,
        Rule64={909, -3156.6, "_OCL_VariableDeclaration__referredVariable"},
    )
    assert isinstance(var_0, python_code_.ATL_MatchedRule)
    var_48 = python_code_.ATL_LazyMatchedRule(isUnique=1)
    assert isinstance(var_48, python_code_.ATL_LazyMatchedRule)
    var_50 = python_code_.OCL_Attribute(
        name="_ATL_CalledRule__ATL_CalledRule:_ATL_Binding__ATL_Binding:OCL_OclExpression:Parameter"
    )
    assert isinstance(var_50, python_code_.OCL_Attribute)
    var_58 = python_code_.OCL_OperationCallExp(operationName=var_56)
    assert isinstance(var_58, python_code_.OCL_OperationCallExp)


def test_37():
    var_0 = python_code_.OCL_OclFeature()
    var_3 = python_code_.ATL_Binding(
        propertyName="O2vn-gTwf_dg38", isAssignment=-653.14, bindings=True
    )
    assert isinstance(var_3, python_code_.ATL_Binding)
    var_6 = lambda *args, **kwargs: 1214
    var_7 = python_code_.LetExp()
    var_8 = python_code_.OCL_VariableDeclaration(
        id=var_6, varName=var_6, initializedVariable=var_0, variable=var_7
    )
    assert isinstance(var_8, python_code_.OCL_VariableDeclaration)
    var_14 = python_code_.OCL_CollectionExp()
    var_15 = "OclExpression144"
    var_16 = python_code_.ATL_ForStat()
    var_17 = python_code_.ATL_BindingStat(
        propertyName=(), isAssignment=var_15, Statement88=var_16, Statement77=var_14
    )
    assert isinstance(var_17, python_code_.ATL_BindingStat)
    var_36 = python_code_.LoopExp()
    var_39 = python_code_.OCL_LoopExp()
    var_40 = python_code_.ATL_IfStat()
    var_41 = python_code_.ATL_BindingStat(
        propertyName=True,
        isAssignment=var_39,
        ATL_BindingStat=b"\x04\x1c\xb8\xce\x1c",
        Statement80=var_40,
        Statement77=-719.99,
    )
    assert isinstance(var_41, python_code_.ATL_BindingStat)
    var_42 = python_code_.OCL_TupleTypeAttribute(
        name={-4432.27, "{M]W5())?ohK"}, attributes=var_36
    )
    assert isinstance(var_42, python_code_.OCL_TupleTypeAttribute)


def test_38():
    var_21 = python_code_.OCL_IntegerExp(integerSymbol="wk\x0c\r1x_s")
    assert isinstance(var_21, python_code_.OCL_IntegerExp)
    var_25 = '"6A]CCo=[{w#\x0clG]z'
    var_45 = ","
    var_48 = python_code_.ATL_Binding(
        propertyName=var_25, isAssignment=var_45, ATL_Binding=var_25
    )
    assert isinstance(var_48, python_code_.ATL_Binding)
    python_code_.ATL_Binding(propertyName=-1757.91, isAssignment=var_25)


def test_39():
    var_2 = python_code_.ATL_ExpressionStat()
    var_3 = python_code_.InPatternElement()
    var_4 = python_code_.ModuleElement()
    var_6 = python_code_.OCL_TupleType()
    var_8 = python_code_.OCL_MapExp()
    var_10 = '#s#pCR"u\tgXa~B'
    var_11 = "R[EBKD%mM<Fm/vAOQ0u"
    var_12 = python_code_.ATL_LocatedElement(
        location=583.01, commentsBefore=var_10, commentsAfter=var_11
    )
    assert isinstance(var_12, python_code_.ATL_LocatedElement)
    var_13 = python_code_.Iterator()
    var_15 = python_code_.ActionBlock
    var_16 = python_code_.OCL_LoopExp()
    var_17 = python_code_.OCL_OclType(
        name=var_3,
        valueType=var_6,
        OclExpression138=var_15,
        OclExpression72=var_2,
        OclExpression134=var_4,
        OclExpression109=var_8,
        OclExpression116=b"\t\xc6\x8c\x8a\x1e\x0b",
        OclExpression125=var_16,
    )
    assert isinstance(var_17, python_code_.OCL_OclType)
    var_18 = "OclModelElement"
    var_19 = python_code_.OCL_StringExp(stringSymbol=var_18)
    assert isinstance(var_19, python_code_.OCL_StringExp)
    var_20 = python_code_.OCL_VariableDeclaration(
        id=var_13, varName=var_4, variable=var_11
    )
    assert isinstance(var_20, python_code_.OCL_VariableDeclaration)
    var_21 = "X{Ku*[dg~'D\x0cH,J"
    python_code_.OCL_VariableDeclaration(
        id=var_21,
        varName=-3270.17,
        result=var_21,
        referredVariable=set(),
        variableDeclaration=var_6,
    )
