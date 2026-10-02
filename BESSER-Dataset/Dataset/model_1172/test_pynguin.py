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
    ATL_Callable,
    ATL_Helper,
    ATL_LocatedElement,
    ATL_ModuleCallable,
    ATL_ModuleElement,
    ATL_Rule,
    ATL_RuleWithPattern,
    ATL_StaticRule,
    ActionBlock,
    Attribute,
    Binding,
    Callable,
    CallableParameter,
    CollectionExp,
    CollectionType,
    ContextHelper,
    DropPattern,
    Helper,
    IfExp,
    InPattern,
    InPatternElement,
    IterateExp,
    Iterator,
    JavaBody,
    LetExp,
    Library,
    LibraryRef,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
    MatchedRule,
    ModuleElement,
    NumericExp,
    NumericType,
    OCL_TypedElement,
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
    ResolveTempResolution,
    Rule,
    RuleResolutionInfo,
    RuleVariableDeclaration,
    RuleWithPattern,
    Statement,
    StaticRule,
    StringToStringMap,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    Unit,
    VariableDeclaration,
    VariableExp,
    abstractmethod,
    atlext_ATL_ActionBlock,
    atlext_ATL_Binding,
    atlext_ATL_BindingStat,
    atlext_ATL_Callable,
    atlext_ATL_CallableParameter,
    atlext_ATL_CalledRule,
    atlext_ATL_ContextHelper,
    atlext_ATL_DropPattern,
    atlext_ATL_ExpressionStat,
    atlext_ATL_ForEachOutPatternElement,
    atlext_ATL_ForStat,
    atlext_ATL_Helper,
    atlext_ATL_IfStat,
    atlext_ATL_InPattern,
    atlext_ATL_InPatternElement,
    atlext_ATL_LazyRule,
    atlext_ATL_Library,
    atlext_ATL_LibraryRef,
    atlext_ATL_LocatedElement,
    atlext_ATL_MatchedRule,
    atlext_ATL_Module,
    atlext_ATL_ModuleCallable,
    atlext_ATL_ModuleElement,
    atlext_ATL_OutPattern,
    atlext_ATL_OutPatternElement,
    atlext_ATL_PatternElement,
    atlext_ATL_Query,
    atlext_ATL_Rule,
    atlext_ATL_RuleResolutionInfo,
    atlext_ATL_RuleVariableDeclaration,
    atlext_ATL_RuleWithPattern,
    atlext_ATL_SimpleInPatternElement,
    atlext_ATL_SimpleOutPatternElement,
    atlext_ATL_Statement,
    atlext_ATL_StaticHelper,
    atlext_ATL_StaticRule,
    atlext_ATL_StringToStringMap,
    atlext_ATL_Unit,
    atlext_OCL_Attribute,
    atlext_OCL_BagExp,
    atlext_OCL_BagType,
    atlext_OCL_BooleanExp,
    atlext_OCL_BooleanType,
    atlext_OCL_CollectionExp,
    atlext_OCL_CollectionOperationCallExp,
    atlext_OCL_CollectionType,
    atlext_OCL_EnumLiteralExp,
    atlext_OCL_GetAppliedStereotypesBody,
    atlext_OCL_IfExp,
    atlext_OCL_IntegerExp,
    atlext_OCL_IntegerType,
    atlext_OCL_IterateExp,
    atlext_OCL_Iterator,
    atlext_OCL_IteratorExp,
    atlext_OCL_JavaBody,
    atlext_OCL_LetExp,
    atlext_OCL_LoopExp,
    atlext_OCL_MapElement,
    atlext_OCL_MapExp,
    atlext_OCL_MapType,
    atlext_OCL_NavigationOrAttributeCallExp,
    atlext_OCL_NumericExp,
    atlext_OCL_NumericType,
    atlext_OCL_OclAnyType,
    atlext_OCL_OclContextDefinition,
    atlext_OCL_OclExpression,
    atlext_OCL_OclFeature,
    atlext_OCL_OclFeatureDefinition,
    atlext_OCL_OclModel,
    atlext_OCL_OclModelElement,
    atlext_OCL_OclType,
    atlext_OCL_OclUndefinedExp,
    atlext_OCL_Operation,
    atlext_OCL_OperationCallExp,
    atlext_OCL_OperatorCallExp,
    atlext_OCL_OrderedSetExp,
    atlext_OCL_OrderedSetType,
    atlext_OCL_Parameter,
    atlext_OCL_Primitive,
    atlext_OCL_PrimitiveExp,
    atlext_OCL_PropertyCallExp,
    atlext_OCL_RealExp,
    atlext_OCL_RealType,
    atlext_OCL_ResolveTempResolution,
    atlext_OCL_SequenceExp,
    atlext_OCL_SequenceType,
    atlext_OCL_SetExp,
    atlext_OCL_SetType,
    atlext_OCL_StringExp,
    atlext_OCL_StringType,
    atlext_OCL_SuperExp,
    atlext_OCL_TupleExp,
    atlext_OCL_TuplePart,
    atlext_OCL_TupleType,
    atlext_OCL_TupleTypeAttribute,
    atlext_OCL_TypedElement,
    atlext_OCL_VariableDeclaration,
    atlext_OCL_VariableExp,
    date,
    datetime,
    time,
)


def test_0():
    var_3 = python_code_.atlext_OCL_Operation(name=(), OclFeature="]'")
    assert isinstance(var_3, python_code_.atlext_OCL_Operation)


def test_1():
    var_12 = python_code_.LoopExp()
    var_13 = "_atlext_OCL_OclExpression__elseExpression"
    var_14 = python_code_.atlext_OCL_Operation(
        name=var_13, operation=var_12, owningOperation=168.46
    )
    assert isinstance(var_14, python_code_.atlext_OCL_Operation)
    python_code_.atlext_OCL_Operation(name=(), OclFeature="]'")


def test_2():
    var_2 = python_code_.atlext_ATL_LibraryRef(name=complex(1888.0, -3027.30812))
    assert isinstance(var_2, python_code_.atlext_ATL_LibraryRef)
    var_3 = lambda *args, **kwargs: False
    var_5 = python_code_.LetExp()
    var_6 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted="_atlext_ATL_LibraryRef__libraries",
        elements106=var_5,
        in_=var_5,
        body=None,
        arguments=None,
    )
    assert isinstance(var_6, python_code_.atlext_OCL_OclExpression)
    var_7 = "~0XpV`W9\n~|\\`vUkE"
    var_8 = python_code_.atlext_ATL_ActionBlock()
    var_9 = python_code_.atlext_ATL_RuleWithPattern(
        isAbstract=-203.98,
        isRefining=var_6,
        isNoDefault=var_7,
        Rule68="gRDziJ0p#b\x0cT",
        Rule71=var_8,
    )
    assert isinstance(var_9, python_code_.atlext_ATL_RuleWithPattern)
    var_36 = "Operation174.OclType.IfExp117.Operation174"
    python_code_.atlext_ATL_StringToStringMap(key=var_36, value=var_3)


def test_3():
    var_2 = python_code_.atlext_ATL_LibraryRef(name=complex(1888.0, -3027.30812))
    assert isinstance(var_2, python_code_.atlext_ATL_LibraryRef)
    var_3 = lambda *args, **kwargs: False
    var_4 = python_code_.atlext_OCL_TupleType()
    var_5 = python_code_.LetExp()
    var_6 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted=var_2,
        body115=var_3,
        oclExpression=var_4,
        in_=var_5,
        arguments=var_3,
        thenExpression={"atlext_OCL_Attribute Parameter": True, "w:|h7": True},
    )
    assert isinstance(var_6, python_code_.atlext_OCL_OclExpression)
    var_7 = "~0XpV`W9\n~|\\`vUkE"
    var_8 = python_code_.atlext_ATL_ActionBlock()
    var_9 = python_code_.atlext_ATL_RuleWithPattern(
        isAbstract=-203.98,
        isRefining=var_6,
        isNoDefault=var_7,
        Rule68="gRDziJ0p#b\x0cT",
        Rule71=var_8,
    )
    assert isinstance(var_9, python_code_.atlext_ATL_RuleWithPattern)
    python_code_.atlext_ATL_CallableParameter(name=var_9)
    var_14 = python_code_.ATL_ModuleCallable()
    var_15 = python_code_.OutPatternElement()
    var_16 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted=var_14,
        body115=var_15,
        condition={},
        elseExpression=complex(-1260.0, -3128.78),
    )
    assert isinstance(var_16, python_code_.atlext_OCL_OclExpression)
    var_31 = "Operation174.OclType.IfExp117.Operation174"
    python_code_.atlext_ATL_StringToStringMap(key=var_31, value=var_3)


def test_4():
    var_6 = python_code_.ATL_ModuleCallable()
    var_7 = python_code_.OutPatternElement()
    var_8 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted=var_6,
        body115=var_7,
        condition={},
        elseExpression=complex(-1260.0, -3128.78),
    )
    assert isinstance(var_8, python_code_.atlext_OCL_OclExpression)
    var_15 = python_code_.atlext_OCL_TupleTypeAttribute(
        name={
            "_atlext_ATL_Rule__rule19",
            "_atlext_ATL_LibraryRef__libraries,_atlext_OCL_OclExpression__body",
            -432,
        }
    )
    assert isinstance(var_15, python_code_.atlext_OCL_TupleTypeAttribute)
    var_17 = python_code_.atlext_OCL_IntegerExp(integerSymbol="w5c&NZQ\t-^[m  `")
    assert isinstance(var_17, python_code_.atlext_OCL_IntegerExp)


def test_5():
    var_7 = "OclModelElement atlext_ATL_Callable _atlext_OCL_OclExpression__source"
    python_code_.atlext_ATL_CallableParameter(name=var_7)


def test_6():
    var_4 = python_code_.InPatternElement()
    var_26 = python_code_.atlext_ATL_BindingStat(propertyName=var_4, isAssignment=set())
    assert isinstance(var_26, python_code_.atlext_ATL_BindingStat)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.OCL_TypedElement()
    var_2 = sorted
    var_3 = python_code_.atlext_ATL_CalledRule(isEntrypoint=var_2, isEndpoint=var_2)
    assert isinstance(var_3, python_code_.atlext_ATL_CalledRule)
    var_5 = python_code_.atlext_OCL_Operation(name=var_0)
    assert isinstance(var_5, python_code_.atlext_OCL_Operation)
    var_6 = python_code_.atlext_OCL_PropertyCallExp(
        isStaticCall=var_2,
        OclExpression219=var_5,
        OclExpression151=var_3,
        OclExpression172=var_2,
        OclExpression161=var_3,
    )
    assert isinstance(var_6, python_code_.atlext_OCL_PropertyCallExp)
    var_7 = python_code_.atlext_ATL_Library()
    var_9 = python_code_.atlext_OCL_SequenceType()
    var_12 = python_code_.LoopExp()
    var_13 = "_atlext_OCL_OclExpression__elseExpression"
    var_14 = python_code_.atlext_OCL_Operation(
        name=var_13, operation=var_12, owningOperation=168.46
    )
    assert isinstance(var_14, python_code_.atlext_OCL_Operation)
    var_21 = python_code_.atlext_OCL_StringExp(stringSymbol=var_13)
    assert isinstance(var_21, python_code_.atlext_OCL_StringExp)
    var_24 = python_code_.atlext_ATL_BindingStat(
        propertyName=var_13,
        isAssignment=[-3088.61],
        atlext_ATL_BindingStat=var_6,
        Statement87=None,
    )
    assert isinstance(var_24, python_code_.atlext_ATL_BindingStat)
    var_32 = python_code_.atlext_ATL_LibraryRef(name=var_7)
    assert isinstance(var_32, python_code_.atlext_ATL_LibraryRef)
    python_code_.atlext_ATL_Module(
        isRefining=var_9, atlext_ATL_Module8=var_24, Unit=var_32
    )


def test_8():
    var_0 = python_code_.OCL_TypedElement()
    var_2 = sorted
    var_3 = python_code_.atlext_ATL_CalledRule(isEntrypoint=var_2, isEndpoint=var_2)
    assert isinstance(var_3, python_code_.atlext_ATL_CalledRule)
    var_5 = python_code_.atlext_OCL_Operation(name=var_0)
    assert isinstance(var_5, python_code_.atlext_OCL_Operation)
    var_6 = python_code_.atlext_OCL_PropertyCallExp(
        isStaticCall=var_2,
        OclExpression219=var_5,
        OclExpression151=var_3,
        OclExpression172=var_2,
        OclExpression161=var_3,
    )
    assert isinstance(var_6, python_code_.atlext_OCL_PropertyCallExp)


def test_9():
    var_0 = python_code_.atlext_ATL_OutPattern()
    var_1 = "atlext_OCL_OperationCallExp.MapType.Attribute.VariableDeclaration"
    var_2 = python_code_.atlext_ATL_RuleWithPattern(
        isAbstract=var_1,
        isRefining=var_1,
        isNoDefault=var_1,
        Rule68=var_0,
        Rule71=var_1,
    )
    assert isinstance(var_2, python_code_.atlext_ATL_RuleWithPattern)
    var_3 = python_code_.atlext_OCL_Operation(name=(), OclFeature="]'")
    assert isinstance(var_3, python_code_.atlext_OCL_Operation)


def test_10():
    var_27 = python_code_.OperationCallExp()
    var_41 = python_code_.atlext_OCL_CollectionExp()
    var_42 = {var_41}
    var_43 = python_code_.atlext_ATL_ContextHelper()
    var_44 = python_code_.atlext_OCL_OperationCallExp(
        operationName=var_27, parentOperation=var_42, PropertyCallExp=var_43
    )
    assert isinstance(var_44, python_code_.atlext_OCL_OperationCallExp)


def test_11():
    var_0 = python_code_.OperationCallExp()
    var_1 = python_code_.OclModel()
    var_2 = {var_1, var_1, var_1, var_1}
    var_3 = python_code_.atlext_ATL_LibraryRef(name=var_0)
    assert isinstance(var_3, python_code_.atlext_ATL_LibraryRef)
    var_4 = python_code_.atlext_ATL_Module(
        isRefining=1039.81, atlext_ATL_Module=var_2, atlext_ATL_Module11=[], Unit=var_3
    )
    assert isinstance(var_4, python_code_.atlext_ATL_Module)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.Callable()
    var_1 = python_code_.atlext_ATL_LibraryRef(name=var_0)
    assert isinstance(var_1, python_code_.atlext_ATL_LibraryRef)
    var_4 = "^BL _<58935e"
    var_5 = python_code_.OclModel()
    var_6 = {var_5, var_5, var_5, var_5, var_5}
    var_7 = python_code_.atlext_OCL_OclModel(name=var_4, metamodel=var_6)
    assert isinstance(var_7, python_code_.atlext_OCL_OclModel)
    var_11 = python_code_.atlext_ATL_LazyRule(isUnique=(True,))
    assert isinstance(var_11, python_code_.atlext_ATL_LazyRule)
    var_16 = python_code_.TupleExp
    python_code_.atlext_ATL_Module(
        isRefining=var_11,
        atlext_ATL_Module8={-620.09, 2696},
        atlext_ATL_Module11=var_16,
    )


def test_13():
    var_0 = "atlext_OCL_MapElement_atlext_ATL_Module__atlext_ATL_Module"
    var_1 = python_code_.atlext_OCL_OclModel(name=var_0)
    assert isinstance(var_1, python_code_.atlext_OCL_OclModel)
    var_2 = python_code_.OclFeature()
    var_5 = python_code_.InPatternElement()
    var_6 = python_code_.ResolveTempResolution()
    var_13 = python_code_.OperationCallExp()
    var_18 = python_code_.ResolveTempResolution()
    var_23 = python_code_.RuleResolutionInfo
    var_24 = python_code_.MapType()
    var_25 = python_code_.TupleTypeAttribute()
    var_26 = object
    var_27 = python_code_.atlext_ATL_BindingStat(propertyName=var_5, isAssignment=set())
    assert isinstance(var_27, python_code_.atlext_ATL_BindingStat)
    var_28 = python_code_.atlext_OCL_CollectionExp()
    var_29 = {var_28}
    var_30 = python_code_.atlext_ATL_ContextHelper()
    var_31 = python_code_.atlext_OCL_OperationCallExp(
        operationName=var_13, parentOperation=var_29, PropertyCallExp=var_30
    )
    assert isinstance(var_31, python_code_.atlext_OCL_OperationCallExp)
    var_32 = python_code_.atlext_OCL_TypedElement
    var_33 = python_code_.atlext_ATL_SimpleOutPatternElement()
    var_34 = python_code_.atlext_OCL_OclType(
        name=var_0,
        context_=var_18,
        valueType=var_23,
        type177=var_23,
        keyType=var_24,
        type183=var_25,
        OclExpression142=var_26,
        OclExpression76=var_27,
        OclExpression123=var_28,
        OclExpression139=var_31,
        OclExpression161=var_32,
        OclExpression81=var_2,
        OclExpression56=var_33,
        OclExpression=var_6,
    )
    assert isinstance(var_34, python_code_.atlext_OCL_OclType)


def test_14():
    var_0 = "atlext_OCL_MapElement_atlext_ATL_Module__atlext_ATL_Module"
    var_1 = python_code_.atlext_OCL_OclModel(name=var_0)
    assert isinstance(var_1, python_code_.atlext_OCL_OclModel)


def test_15():
    var_0 = python_code_.OperationCallExp()
    var_3 = python_code_.atlext_ATL_LibraryRef(name=var_0)
    assert isinstance(var_3, python_code_.atlext_ATL_LibraryRef)


def test_16():
    var_51 = python_code_.atlext_ATL_Unit(name=True)
    assert isinstance(var_51, python_code_.atlext_ATL_Unit)


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = python_code_.OperationCallExp()
    var_1 = python_code_.OclModel()
    var_2 = {var_1, var_1, var_1, var_1}
    var_3 = python_code_.atlext_ATL_LibraryRef(name=var_0)
    assert isinstance(var_3, python_code_.atlext_ATL_LibraryRef)
    var_4 = python_code_.atlext_ATL_Module(
        isRefining=1039.81, atlext_ATL_Module=var_2, atlext_ATL_Module11=[], Unit=var_3
    )
    assert isinstance(var_4, python_code_.atlext_ATL_Module)
    var_5 = "Q}:bgDb"
    var_6 = "OLf<QeD.~2"
    python_code_.atlext_ATL_LocatedElement(
        location={"n:j*]g@m", 1486.59, "atlext_ATL_Binding"},
        commentsBefore=var_2,
        commentsAfter=var_5,
        fileLocation=var_0,
        fileObject=var_6,
        atlext_ATL_LocatedElement=var_3,
    )


def test_18():
    var_3 = python_code_.atlext_ATL_CalledRule
    var_4 = "_atlext_ATL_Module__atlext_ATL_Module8"
    var_5 = python_code_.atlext_ATL_LocatedElement(
        location=var_3,
        commentsBefore=False,
        commentsAfter=var_4,
        fileLocation=var_4,
        fileObject=True,
    )
    assert isinstance(var_5, python_code_.atlext_ATL_LocatedElement)
    var_11 = ";q4zgQnh:^'rD4y+c"
    var_12 = python_code_.atlext_OCL_PrimitiveExp()
    var_13 = python_code_.atlext_OCL_Operation(name=var_11, owningOperation=var_12)
    assert isinstance(var_13, python_code_.atlext_OCL_Operation)
    var_17 = python_code_.atlext_ATL_Unit(name=True)
    assert isinstance(var_17, python_code_.atlext_ATL_Unit)


def test_19():
    python_code_.atlext_ATL_OutPattern()


def test_20():
    var_0 = python_code_.atlext_OCL_IntegerExp
    var_1 = python_code_.atlext_OCL_TupleTypeAttribute(name=var_0)
    assert isinstance(var_1, python_code_.atlext_OCL_TupleTypeAttribute)
    var_3 = python_code_.atlext_OCL_BooleanExp(booleanSymbol=var_0)
    assert isinstance(var_3, python_code_.atlext_OCL_BooleanExp)
    var_7 = "Gu}(Di"
    python_code_.atlext_ATL_StringToStringMap(
        key=var_7, value=complex(533.0414273, -1698.4160881)
    )
    var_18 = python_code_.atlext_ATL_LibraryRef(name=True)
    assert isinstance(var_18, python_code_.atlext_ATL_LibraryRef)
    var_21 = python_code_.atlext_ATL_IfStat()
    var_22 = python_code_.atlext_ATL_BindingStat(
        propertyName=var_7,
        isAssignment=-2743,
        Statement84=var_21,
        Statement=b"\xc5f\xb3x\xc2\x87q\xbc\xc8\xf6n6YT\x9fti",
    )
    assert isinstance(var_22, python_code_.atlext_ATL_BindingStat)
    var_31 = "jl:AX'2(xinQ"
    var_32 = python_code_.atlext_OCL_StringExp(stringSymbol=var_31)
    assert isinstance(var_32, python_code_.atlext_OCL_StringExp)


def test_21():
    var_34 = python_code_.Primitive()
    var_36 = python_code_.ATL_ModuleElement()
    var_38 = python_code_.TupleType()
    var_40 = python_code_.LoopExp()
    var_41 = "_atlext_OCL_OclExpression__elseExpression"
    var_42 = python_code_.atlext_OCL_Operation(
        name=var_41, operation=var_40, owningOperation=168.46
    )
    assert isinstance(var_42, python_code_.atlext_OCL_Operation)
    var_47 = ";q4zgQnh:^'rD4y+c"
    var_51 = python_code_.Iterator()
    var_53 = python_code_.atlext_ATL_Unit(name=var_47, unit={var_34, var_51})
    assert isinstance(var_53, python_code_.atlext_ATL_Unit)
    var_56 = python_code_.atlext_OCL_TupleTypeAttribute(name=var_47, attributes=var_38)
    assert isinstance(var_56, python_code_.atlext_OCL_TupleTypeAttribute)
    var_57 = python_code_.atlext_OCL_StringExp(stringSymbol=var_36)
    assert isinstance(var_57, python_code_.atlext_OCL_StringExp)


def test_22():
    var_2 = python_code_.atlext_ATL_LibraryRef(
        name="atlext_ATL_LibraryRef,_atlext_ATL_RuleWithPattern__atlext_ATL_RuleWithPattern,OclModel"
    )
    assert isinstance(var_2, python_code_.atlext_ATL_LibraryRef)
    var_3 = lambda *args, **kwargs: False
    var_7 = "~0XpV`W9\n7~|\\`vUkE"
    var_33 = python_code_.atlext_OCL_OperatorCallExp()
    var_35 = "_atlext_ATL_Binding__atlext_ATL_Binding66.ActionBlock.Operation174"
    var_36 = python_code_.InPattern()
    var_37 = set()
    var_38 = python_code_.atlext_ATL_OutPattern()
    var_39 = python_code_.atlext_ATL_RuleWithPattern(
        isAbstract=var_3,
        isRefining=var_35,
        isNoDefault=var_7,
        atlext_ATL_RuleWithPattern=var_36,
        superRule=var_37,
        Rule71=var_33,
        Rule=var_38,
    )
    assert isinstance(var_39, python_code_.atlext_ATL_RuleWithPattern)


@pytest.mark.xfail(strict=True)
def test_23():
    var_2 = python_code_.atlext_ATL_ModuleCallable()
    var_5 = python_code_.atlext_OCL_OclFeature()
    var_6 = python_code_.atlext_OCL_IntegerExp(
        integerSymbol="_atlext_OCL_VariableDeclaration__referredVariable,Query,atlext_OCL_Attribute,atlext_ATL_Callable"
    )
    assert isinstance(var_6, python_code_.atlext_OCL_IntegerExp)
    var_12 = "!\n}uFl"
    var_13 = python_code_.atlext_OCL_IteratorExp(name=var_12)
    assert isinstance(var_13, python_code_.atlext_OCL_IteratorExp)
    var_18 = python_code_.atlext_OCL_NavigationOrAttributeCallExp(
        name=b"\xce\x1f\xff\x1a\xd7\xaa\xdb2\x15\x0fv2\xd8s\x97", PropertyCallExp=var_2
    )
    assert isinstance(var_18, python_code_.atlext_OCL_NavigationOrAttributeCallExp)
    var_23 = "atlext_ATL_ContextHelper"
    var_24 = "LoopExp-MapType-TupleType"
    var_25 = python_code_.atlext_ATL_ModuleElement
    python_code_.atlext_ATL_LocatedElement(
        location=var_5,
        commentsBefore=var_23,
        commentsAfter=var_12,
        fileLocation={True},
        fileObject=var_24,
        atlext_ATL_LocatedElement=var_25,
    )


def test_24():
    var_0 = python_code_.OperationCallExp()
    var_1 = python_code_.atlext_OCL_NavigationOrAttributeCallExp(name=var_0)
    assert isinstance(var_1, python_code_.atlext_OCL_NavigationOrAttributeCallExp)
    var_16 = python_code_.atlext_ATL_CallableParameter(name=-1381)
    var_23 = python_code_.Operation()
    var_24 = python_code_.OclType()
    var_25 = python_code_.IfExp()
    var_26 = python_code_.atlext_OCL_NumericExp
    var_27 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted=var_16,
        body115=var_23,
        oclExpression=var_24,
        elseExpression=var_25,
        initExpression=var_26,
    )
    assert isinstance(var_27, python_code_.atlext_OCL_OclExpression)


def test_25():
    var_3 = python_code_.atlext_ATL_CalledRule
    var_4 = "_atlext_ATL_Module__atlext_ATL_Module8"
    var_5 = python_code_.atlext_ATL_LocatedElement(
        location=var_3,
        commentsBefore=False,
        commentsAfter=var_4,
        fileLocation=var_4,
        fileObject=True,
    )
    assert isinstance(var_5, python_code_.atlext_ATL_LocatedElement)
    var_13 = python_code_.atlext_OCL_Operation(
        name="f", atlext_OCL_Operation=set(), OclFeature=var_3
    )
    assert isinstance(var_13, python_code_.atlext_OCL_Operation)
    var_19 = python_code_.atlext_ATL_Unit(name=True)
    assert isinstance(var_19, python_code_.atlext_ATL_Unit)


def test_26():
    var_0 = python_code_.OperationCallExp()
    var_3 = python_code_.atlext_ATL_LibraryRef(name=var_0)
    assert isinstance(var_3, python_code_.atlext_ATL_LibraryRef)
    var_23 = python_code_.atlext_OCL_TupleType()
    var_24 = python_code_.atlext_OCL_VariableDeclaration(
        id=var_0, varName=complex(-927.612957, 522.62), variableDeclaration=var_23
    )
    assert isinstance(var_24, python_code_.atlext_OCL_VariableDeclaration)


def test_27():
    var_3 = python_code_.atlext_ATL_CalledRule
    var_4 = "_atlext_ATL_Module__atlext_ATL_Module8"
    var_5 = python_code_.atlext_ATL_LocatedElement(
        location=var_3,
        commentsBefore=False,
        commentsAfter=var_4,
        fileLocation=var_4,
        fileObject=True,
    )
    assert isinstance(var_5, python_code_.atlext_ATL_LocatedElement)
    var_31 = "atlext_ATL_OutPattern"
    var_32 = python_code_.LetExp()
    var_33 = python_code_.atlext_OCL_VariableDeclaration(
        id=var_31, varName=True, variable=var_32
    )
    assert isinstance(var_33, python_code_.atlext_OCL_VariableDeclaration)


def test_28():
    var_2 = python_code_.atlext_ATL_LibraryRef(name=complex(1888.0, -3027.30812))
    assert isinstance(var_2, python_code_.atlext_ATL_LibraryRef)
    var_3 = lambda *args, **kwargs: False
    var_4 = python_code_.atlext_OCL_TupleType()
    var_6 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted="fGw~?Zv=xQ",
        initExpression119=var_3,
        elseExpression=None,
        body=var_4,
        thenExpression=None,
    )
    assert isinstance(var_6, python_code_.atlext_OCL_OclExpression)
    var_7 = "~0XpV`W9\n~|\\`vUkE"
    var_8 = python_code_.atlext_ATL_ActionBlock()
    var_9 = python_code_.atlext_ATL_RuleWithPattern(
        isAbstract=-203.98,
        isRefining=var_6,
        isNoDefault=var_7,
        Rule68="gRDziJ0p#b\x0cT",
        Rule71=var_8,
    )
    assert isinstance(var_9, python_code_.atlext_ATL_RuleWithPattern)
    python_code_.atlext_ATL_CallableParameter(name=var_9)
    var_16 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted=var_7, condition=var_7, initExpression=var_9
    )
    assert isinstance(var_16, python_code_.atlext_OCL_OclExpression)
    var_37 = python_code_.atlext_ATL_Unit(name=True)
    assert isinstance(var_37, python_code_.atlext_ATL_Unit)


def test_29():
    var_2 = python_code_.atlext_ATL_LibraryRef(name=complex(1888.0, -3027.30812))
    assert isinstance(var_2, python_code_.atlext_ATL_LibraryRef)
    var_4 = python_code_.atlext_OCL_TupleType()
    var_31 = python_code_.atlext_OCL_Operation(name=(), OclFeature="]'")
    assert isinstance(var_31, python_code_.atlext_OCL_Operation)
    var_34 = python_code_.atlext_ATL_Helper(hasContext=var_2, isAttribute=var_4)
    assert isinstance(var_34, python_code_.atlext_ATL_Helper)


def test_30():
    var_0 = python_code_.atlext_OCL_NumericType()
    var_2 = python_code_.atlext_ATL_ModuleCallable()
    var_9 = python_code_.atlext_OCL_TupleExp()
    var_11 = python_code_.Unit()
    var_12 = python_code_.atlext_ATL_LibraryRef(name=var_9, libraries=var_11)
    assert isinstance(var_12, python_code_.atlext_ATL_LibraryRef)
    var_13 = python_code_.atlext_ATL_Module(isRefining=var_2, Unit=var_12)
    assert isinstance(var_13, python_code_.atlext_ATL_Module)
    var_14 = python_code_.ContextHelper()
    var_18 = ""
    var_19 = python_code_.atlext_ATL_CalledRule(isEntrypoint=var_18, isEndpoint=var_18)
    assert isinstance(var_19, python_code_.atlext_ATL_CalledRule)
    var_21 = python_code_.atlext_ATL_Helper(hasContext=var_0, isAttribute=var_14)
    assert isinstance(var_21, python_code_.atlext_ATL_Helper)
    python_code_.atlext_ATL_LibraryRef(name="atlext_OCL_IfExp", libraries=None)
    var_36 = python_code_.atlext_OCL_TupleTypeAttribute(
        name={
            "_atlext_ATL_Rule__rule19",
            "_atlext_ATL_LibraryRef__libraries,_atlext_OCL_OclExpression__body",
            -432,
        }
    )
    assert isinstance(var_36, python_code_.atlext_OCL_TupleTypeAttribute)
    var_38 = python_code_.atlext_OCL_IntegerExp(integerSymbol="w5c&NZQ\t-^[m  `")
    assert isinstance(var_38, python_code_.atlext_OCL_IntegerExp)


def test_31():
    var_2 = python_code_.atlext_ATL_LibraryRef(name=complex(1888.0, -3027.30812))
    assert isinstance(var_2, python_code_.atlext_ATL_LibraryRef)
    var_3 = lambda *args, **kwargs: False
    var_4 = python_code_.atlext_OCL_TupleType()
    var_6 = python_code_.atlext_OCL_OclExpression(
        implicitlyCasted="fGw~?Zv=xQ",
        initExpression119=var_3,
        elseExpression=None,
        body=var_4,
        thenExpression=None,
    )
    assert isinstance(var_6, python_code_.atlext_OCL_OclExpression)
    var_7 = "~0XpV`W9\n~|\\`vUkE"
    var_8 = python_code_.atlext_ATL_ActionBlock()
    var_9 = python_code_.atlext_ATL_RuleWithPattern(
        isAbstract=-203.98,
        isRefining=var_6,
        isNoDefault=var_7,
        Rule68="gRDziJ0p#b\x0cT",
        Rule71=var_8,
    )
    assert isinstance(var_9, python_code_.atlext_ATL_RuleWithPattern)
    python_code_.atlext_ATL_CallableParameter(name=var_9)
    var_36 = python_code_.LoopExp()
    var_37 = "_atlext_OCL_OclExpression__elseExpression"
    var_38 = python_code_.atlext_OCL_Operation(
        name=var_37, operation=var_36, owningOperation=168.46
    )
    assert isinstance(var_38, python_code_.atlext_OCL_Operation)
    python_code_.atlext_OCL_Operation(name=(), OclFeature="]'")
