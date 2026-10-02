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
    ActionBlock,
    Binding,
    CollectionExp,
    CollectionType,
    DropPattern,
    Helper,
    InPattern,
    InPatternElement,
    Iterator,
    LoopExp,
    MapElement,
    MatchedRule,
    ModuleElement,
    NumericExp,
    NumericType,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclModel,
    OclModelElement,
    OclType,
    OperationCallExp,
    OutPattern,
    OutPatternElement,
    Parameter,
    PatternElement,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    Rule,
    RuleVariableDeclaration,
    Statement,
    TupleExp,
    TuplePart,
    TupleTypeAttribute,
    VariableDeclaration,
    abstractmethod,
    atl_n_ocl_ATL_ActionBlock,
    atl_n_ocl_ATL_Binding,
    atl_n_ocl_ATL_BindingStat,
    atl_n_ocl_ATL_CalledRule,
    atl_n_ocl_ATL_DropPattern,
    atl_n_ocl_ATL_ExpressionStat,
    atl_n_ocl_ATL_ForEachOutPatternElement,
    atl_n_ocl_ATL_ForStat,
    atl_n_ocl_ATL_Helper,
    atl_n_ocl_ATL_IfStat,
    atl_n_ocl_ATL_InPattern,
    atl_n_ocl_ATL_InPatternElement,
    atl_n_ocl_ATL_LazyMatchedRule,
    atl_n_ocl_ATL_MatchedRule,
    atl_n_ocl_ATL_Module,
    atl_n_ocl_ATL_ModuleElement,
    atl_n_ocl_ATL_OutPattern,
    atl_n_ocl_ATL_OutPatternElement,
    atl_n_ocl_ATL_PatternElement,
    atl_n_ocl_ATL_Query,
    atl_n_ocl_ATL_Rule,
    atl_n_ocl_ATL_RuleVariableDeclaration,
    atl_n_ocl_ATL_SimpleInPatternElement,
    atl_n_ocl_ATL_SimpleOutPatternElement,
    atl_n_ocl_ATL_Statement,
    atl_n_ocl_OCL_Attribute,
    atl_n_ocl_OCL_BagExp,
    atl_n_ocl_OCL_BagType,
    atl_n_ocl_OCL_BooleanExp,
    atl_n_ocl_OCL_BooleanType,
    atl_n_ocl_OCL_CollectionExp,
    atl_n_ocl_OCL_CollectionOperationCallExp,
    atl_n_ocl_OCL_CollectionType,
    atl_n_ocl_OCL_EnumLiteralExp,
    atl_n_ocl_OCL_IfExp,
    atl_n_ocl_OCL_IntegerExp,
    atl_n_ocl_OCL_IntegerType,
    atl_n_ocl_OCL_IterateExp,
    atl_n_ocl_OCL_Iterator,
    atl_n_ocl_OCL_IteratorExp,
    atl_n_ocl_OCL_LetExp,
    atl_n_ocl_OCL_LoopExp,
    atl_n_ocl_OCL_MapElement,
    atl_n_ocl_OCL_MapExp,
    atl_n_ocl_OCL_MapType,
    atl_n_ocl_OCL_NavigationOrAttributeCallExp,
    atl_n_ocl_OCL_NumericExp,
    atl_n_ocl_OCL_NumericType,
    atl_n_ocl_OCL_OclAnyType,
    atl_n_ocl_OCL_OclContextDefinition,
    atl_n_ocl_OCL_OclExpression,
    atl_n_ocl_OCL_OclFeature,
    atl_n_ocl_OCL_OclFeatureDefinition,
    atl_n_ocl_OCL_OclModel,
    atl_n_ocl_OCL_OclModelElement,
    atl_n_ocl_OCL_OclType,
    atl_n_ocl_OCL_OclUndefinedExp,
    atl_n_ocl_OCL_Operation,
    atl_n_ocl_OCL_OperationCallExp,
    atl_n_ocl_OCL_OperatorCallExp,
    atl_n_ocl_OCL_OrderedSetExp,
    atl_n_ocl_OCL_OrderedSetType,
    atl_n_ocl_OCL_Parameter,
    atl_n_ocl_OCL_Primitive,
    atl_n_ocl_OCL_PrimitiveExp,
    atl_n_ocl_OCL_PropertyCallExp,
    atl_n_ocl_OCL_RealExp,
    atl_n_ocl_OCL_RealType,
    atl_n_ocl_OCL_SequenceExp,
    atl_n_ocl_OCL_SequenceType,
    atl_n_ocl_OCL_SetExp,
    atl_n_ocl_OCL_SetType,
    atl_n_ocl_OCL_StringExp,
    atl_n_ocl_OCL_StringType,
    atl_n_ocl_OCL_SuperExp,
    atl_n_ocl_OCL_TupleExp,
    atl_n_ocl_OCL_TuplePart,
    atl_n_ocl_OCL_TupleType,
    atl_n_ocl_OCL_TupleTypeAttribute,
    atl_n_ocl_OCL_VariableDeclaration,
    atl_n_ocl_OCL_VariableExp,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = python_code_.atl_n_ocl_OCL_NavigationOrAttributeCallExp(name=True)
    assert isinstance(var_0, python_code_.atl_n_ocl_OCL_NavigationOrAttributeCallExp)
    var_29 = python_code_.atl_n_ocl_OCL_VariableExp()
    var_31 = python_code_.atl_n_ocl_OCL_Operation(name="OclExpression109")
    assert isinstance(var_31, python_code_.atl_n_ocl_OCL_Operation)
    var_40 = True
    var_41 = {2980.78}
    var_42 = python_code_.atl_n_ocl_ATL_CalledRule(
        isEntrypoint=var_29, isEndpoint=var_40, atl_n_ocl_ATL_CalledRule=var_41
    )
    assert isinstance(var_42, python_code_.atl_n_ocl_ATL_CalledRule)
    var_44 = "'\n_zQg4\\e"
    var_45 = python_code_.atl_n_ocl_OCL_OclModel(
        name=var_44, atl_n_ocl_OCL_OclModel141=var_41, atl_n_ocl_OCL_OclModel143=()
    )
    assert isinstance(var_45, python_code_.atl_n_ocl_OCL_OclModel)
    var_47 = python_code_.atl_n_ocl_OCL_BooleanExp(
        booleanSymbol=complex(634.36, 1776.5196737)
    )
    assert isinstance(var_47, python_code_.atl_n_ocl_OCL_BooleanExp)
    var_50 = "j?\\mSEBctg"
    var_51 = python_code_.atl_n_ocl_ATL_Rule(name=var_50)
    assert isinstance(var_51, python_code_.atl_n_ocl_ATL_Rule)


def test_1():
    var_58 = python_code_.atl_n_ocl_OCL_OclModel(
        name="&x_0", atl_n_ocl_OCL_OclModel143=set()
    )
    assert isinstance(var_58, python_code_.atl_n_ocl_OCL_OclModel)


def test_2():
    var_21 = "@BsK\rb ,f"
    python_code_.atl_n_ocl_OCL_TupleTypeAttribute(
        name=var_21, atl_n_ocl_OCL_TupleTypeAttribute=None
    )


def test_3():
    var_11 = "R\x0b\tL%"
    var_14 = python_code_.atl_n_ocl_OCL_TupleTypeAttribute(
        name=var_11, atl_n_ocl_OCL_TupleTypeAttribute=var_11
    )
    assert isinstance(var_14, python_code_.atl_n_ocl_OCL_TupleTypeAttribute)


def test_4():
    var_6 = "atl_n_ocl_OCL_Map%lement"
    var_7 = python_code_.atl_n_ocl_OCL_Attribute(
        name=var_6, atl_n_ocl_OCL_Attribute128=var_6
    )
    assert isinstance(var_7, python_code_.atl_n_ocl_OCL_Attribute)


def test_5():
    var_52 = "atl_n_ocl_OCL_MapElement"
    var_53 = python_code_.atl_n_ocl_OCL_Attribute(
        name=">I]#oiWp:d\x0b.h-", atl_n_ocl_OCL_Attribute=var_52
    )
    assert isinstance(var_53, python_code_.atl_n_ocl_OCL_Attribute)


def test_6():
    var_9 = python_code_.atl_n_ocl_OCL_Operation(
        name='"@0H!rBmU]Wc}?o0A',
        atl_n_ocl_OCL_Operation=set(),
        atl_n_ocl_OCL_Operation133=None,
    )
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_Operation)


def test_7():
    var_9 = python_code_.atl_n_ocl_OCL_Operation(
        name="OclExpression", atl_n_ocl_OCL_Operation136=None
    )
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_Operation)


def test_8():
    python_code_.atl_n_ocl_OCL_VariableDeclaration(
        id="a^RhsXWAIjA>", varName="5oz~Pje", atl_n_ocl_OCL_VariableDeclaration=None
    )


def test_9():
    var_21 = python_code_.atl_n_ocl_OCL_OperationCallExp(operationName="O(^r:@qM")
    assert isinstance(var_21, python_code_.atl_n_ocl_OCL_OperationCallExp)


def test_10():
    var_67 = "_atl_n_ocl_OCL_Operation__atl_n_ocl_OCL_Operation133ActionBlockMatchedRuleOclExression126"
    var_68 = python_code_.atl_n_ocl_OCL_OclUndefinedExp()
    var_69 = python_code_.atl_n_ocl_ATL_BindingStat(
        propertyName=var_67, isAssignment=True, atl_n_ocl_ATL_BindingStat=var_68
    )
    assert isinstance(var_69, python_code_.atl_n_ocl_ATL_BindingStat)


def test_11():
    var_58 = python_code_.atl_n_ocl_ATL_BindingStat(
        propertyName="\x0bY_V5}{BPb", isAssignment=False
    )
    assert isinstance(var_58, python_code_.atl_n_ocl_ATL_BindingStat)


def test_12():
    var_23 = '|j7~#g:\\\\mv,)>"'
    var_26 = python_code_.atl_n_ocl_OCL_OclUndefinedExp()
    python_code_.atl_n_ocl_ATL_Binding(
        propertyName=complex(-3035.376628, -1616.8),
        isAssignment=var_23,
        atl_n_ocl_ATL_Binding=var_26,
    )


def test_13():
    var_16 = True
    python_code_.atl_n_ocl_ATL_Binding(propertyName=None, isAssignment=var_16)


def test_14():
    var_1 = True
    var_2 = python_code_.atl_n_ocl_ATL_Module(isRefining=var_1)
    assert isinstance(var_2, python_code_.atl_n_ocl_ATL_Module)


def test_15():
    var_1 = False
    var_32 = python_code_.atl_n_ocl_ATL_CalledRule(
        isEntrypoint=var_1, isEndpoint=False, atl_n_ocl_ATL_CalledRule={False}
    )
    assert isinstance(var_32, python_code_.atl_n_ocl_ATL_CalledRule)


def test_16():
    var_1 = False
    var_32 = python_code_.atl_n_ocl_ATL_CalledRule(isEntrypoint=True, isEndpoint=var_1)
    assert isinstance(var_32, python_code_.atl_n_ocl_ATL_CalledRule)


@pytest.mark.xfail(strict=True)
def test_17():
    var_5 = python_code_.InPatternElement
    var_8 = True
    python_code_.atl_n_ocl_ATL_MatchedRule(
        isAbstract=var_8,
        isRefining=var_5,
        isNoDefault=var_8,
        atl_n_ocl_ATL_MatchedRule17=var_5,
    )


def test_18():
    var_9 = python_code_.atl_n_ocl_OCL_Operation(
        name="OclExpression126", OclFeature=None
    )
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_Operation)
    var_21 = False
    var_22 = False
    var_23 = python_code_.atl_n_ocl_ATL_MatchedRule(
        isAbstract=var_9,
        isRefining=var_21,
        isNoDefault=var_22,
        atl_n_ocl_ATL_MatchedRule=var_21,
    )
    assert isinstance(var_23, python_code_.atl_n_ocl_ATL_MatchedRule)


def test_19():
    var_0 = python_code_.InPattern()
    var_4 = python_code_.atl_n_ocl_ATL_CalledRule(
        isEntrypoint=var_0, isEndpoint=b"\xa4\xaa\x87\x9f\x93\xa6d\x03>zZ\x97\xb4"
    )
    assert isinstance(var_4, python_code_.atl_n_ocl_ATL_CalledRule)
    var_5 = python_code_.OclContextDefinition()
    var_7 = python_code_.atl_n_ocl_OCL_IterateExp()
    var_9 = python_code_.atl_n_ocl_OCL_IntegerExp(integerSymbol=var_7)
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_IntegerExp)
    var_18 = lambda *args, **kwargs: 922
    var_19 = True
    var_20 = python_code_.atl_n_ocl_ATL_MatchedRule(
        isAbstract=var_18, isRefining=var_19, isNoDefault=var_5
    )
    assert isinstance(var_20, python_code_.atl_n_ocl_ATL_MatchedRule)
    var_25 = 'jo@>&5y\t"tP}2g*~t?<'
    var_26 = python_code_.atl_n_ocl_OCL_IteratorExp(name=var_25)
    assert isinstance(var_26, python_code_.atl_n_ocl_OCL_IteratorExp)
    var_27 = python_code_.atl_n_ocl_OCL_RealExp(realSymbol=var_18)
    assert isinstance(var_27, python_code_.atl_n_ocl_OCL_RealExp)
    var_34 = python_code_.atl_n_ocl_ATL_LazyMatchedRule(
        isUnique=complex(5427.4520905, 604.0)
    )
    assert isinstance(var_34, python_code_.atl_n_ocl_ATL_LazyMatchedRule)


def test_20():
    var_24 = python_code_.atl_n_ocl_ATL_Rule(name="0;YA", ModuleElement=None)
    assert isinstance(var_24, python_code_.atl_n_ocl_ATL_Rule)


def test_21():
    var_16 = python_code_.RuleVariableDeclaration
    var_22 = "j?\\mSEBctg"
    var_23 = python_code_.atl_n_ocl_ATL_Rule(
        name='\x0cp:t!FJBpm|mLN"be',
        atl_n_ocl_ATL_Rule14=set(),
        atl_n_ocl_ATL_Rule=var_22,
        atl_n_ocl_ATL_Rule12=None,
        ModuleElement=var_16,
    )
    assert isinstance(var_23, python_code_.atl_n_ocl_ATL_Rule)


def test_22():
    python_code_.atl_n_ocl_OCL_OclFeatureDefinition()


def test_23():
    var_21 = python_code_.atl_n_ocl_OCL_IteratorExp(name=[])
    assert isinstance(var_21, python_code_.atl_n_ocl_OCL_IteratorExp)


def test_24():
    var_0 = python_code_.atl_n_ocl_OCL_NavigationOrAttributeCallExp(name=True)
    assert isinstance(var_0, python_code_.atl_n_ocl_OCL_NavigationOrAttributeCallExp)
    var_87 = '|j7~#g:\\\\v,)>"'
    var_88 = python_code_.atl_n_ocl_ATL_Rule(name=var_87)
    assert isinstance(var_88, python_code_.atl_n_ocl_ATL_Rule)


def test_25():
    var_0 = 744
    var_1 = python_code_.atl_n_ocl_OCL_IntegerExp(integerSymbol=var_0)
    assert isinstance(var_1, python_code_.atl_n_ocl_OCL_IntegerExp)


def test_26():
    var_0 = python_code_.atl_n_ocl_OCL_OclUndefinedExp()
    var_1 = python_code_.atl_n_ocl_ATL_IfStat()
    var_2 = python_code_.atl_n_ocl_ATL_ActionBlock()
    var_3 = python_code_.atl_n_ocl_ATL_BindingStat(
        propertyName=None,
        isAssignment=(4305.31,),
        atl_n_ocl_ATL_BindingStat51=var_0,
        Statement60=var_1,
        Statement57=var_0,
        Statement=var_2,
    )
    assert isinstance(var_3, python_code_.atl_n_ocl_ATL_BindingStat)
    var_9 = python_code_.atl_n_ocl_OCL_RealExp(realSymbol=None)
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_RealExp)


def test_27():
    var_1 = True
    var_2 = python_code_.atl_n_ocl_ATL_Module(
        isRefining=var_1, atl_n_ocl_ATL_Module5=set()
    )
    assert isinstance(var_2, python_code_.atl_n_ocl_ATL_Module)
    var_31 = python_code_.atl_n_ocl_OCL_BooleanExp(booleanSymbol=set())
    assert isinstance(var_31, python_code_.atl_n_ocl_OCL_BooleanExp)


def test_28():
    var_45 = list
    var_47 = "0)ocv"
    python_code_.atl_n_ocl_OCL_VariableDeclaration(
        id={
            ">bPx-Tz": "grYgfR.|0W~<2^/s8,",
            "OclExpression": "q",
            "\to|wF2CJ\nW[dn": 1,
        },
        varName=var_47,
    )
    var_49 = python_code_.atl_n_ocl_OCL_StringExp(stringSymbol=var_45)
    assert isinstance(var_49, python_code_.atl_n_ocl_OCL_StringExp)


def test_29():
    var_6 = "atl_n_ocl_OCL_MapElement"
    var_7 = python_code_.atl_n_ocl_OCL_Attribute(
        name=var_6, atl_n_ocl_OCL_Attribute128=var_6
    )
    assert isinstance(var_7, python_code_.atl_n_ocl_OCL_Attribute)
    var_16 = python_code_.atl_n_ocl_OCL_MapElement
    var_17 = python_code_.atl_n_ocl_ATL_Binding(propertyName=var_6, isAssignment=var_16)
    var_18 = python_code_.atl_n_ocl_ATL_SimpleOutPatternElement()
    var_19 = python_code_.atl_n_ocl_OCL_LoopExp()
    var_20 = python_code_.atl_n_ocl_OCL_IfExp()
    var_21 = python_code_.atl_n_ocl_OCL_OclType(
        name=var_7,
        OclExpression44=var_17,
        OclExpression38=var_18,
        OclExpression86=var_19,
        OclExpression80=var_16,
        OclExpression98=var_20,
    )
    assert isinstance(var_21, python_code_.atl_n_ocl_OCL_OclType)


def test_30():
    var_0 = python_code_.atl_n_ocl_OCL_NavigationOrAttributeCallExp(name=True)
    assert isinstance(var_0, python_code_.atl_n_ocl_OCL_NavigationOrAttributeCallExp)
    var_2 = "+~.1-1\\2jS,\t~>\x0c/"
    var_3 = False
    var_4 = python_code_.atl_n_ocl_OCL_OclUndefinedExp()
    var_5 = python_code_.atl_n_ocl_ATL_Binding(
        propertyName=var_2, isAssignment=var_3, atl_n_ocl_ATL_Binding=var_4
    )
    var_8 = lambda *args, **kwargs: [1967]
    var_9 = python_code_.atl_n_ocl_ATL_ForEachOutPatternElement()
    var_10 = python_code_.atl_n_ocl_OCL_EnumLiteralExp(
        name=var_0,
        OclExpression44=var_5,
        OclExpression137=var_8,
        OclExpression52=-216.95,
        OclExpression49=set(),
        OclExpression80=[-350.82, 2977.84, True],
        OclExpression40=var_9,
    )
    assert isinstance(var_10, python_code_.atl_n_ocl_OCL_EnumLiteralExp)
    var_18 = -816.08
    var_19 = python_code_.atl_n_ocl_OCL_RealExp(realSymbol=var_18)
    assert isinstance(var_19, python_code_.atl_n_ocl_OCL_RealExp)


def test_31():
    var_0 = python_code_.atl_n_ocl_OCL_Iterator()
    var_1 = python_code_.OclModelElement()
    var_3 = python_code_.atl_n_ocl_OCL_OclFeatureDefinition
    var_4 = python_code_.atl_n_ocl_OCL_Operation(
        name='pB"5Z9ON|',
        atl_n_ocl_OCL_Operation={var_1},
        atl_n_ocl_OCL_Operation136=var_0,
    )
    assert isinstance(var_4, python_code_.atl_n_ocl_OCL_Operation)
    var_6 = "?\x0cNtBy{me.@'vxFsq"
    var_7 = python_code_.atl_n_ocl_OCL_VariableDeclaration(
        id=-1350.01, varName=var_6, atl_n_ocl_OCL_VariableDeclaration108=b"\xf3"
    )
    assert isinstance(var_7, python_code_.atl_n_ocl_OCL_VariableDeclaration)
    var_8 = python_code_.atl_n_ocl_OCL_CollectionType()
    var_11 = python_code_.OclExpression()
    var_15 = False
    var_16 = python_code_.atl_n_ocl_ATL_LazyMatchedRule(isUnique=var_15)
    assert isinstance(var_16, python_code_.atl_n_ocl_ATL_LazyMatchedRule)
    python_code_.atl_n_ocl_OCL_TupleTypeAttribute(
        name=var_11, atl_n_ocl_OCL_TupleTypeAttribute=var_8
    )
    python_code_.atl_n_ocl_ATL_Binding(propertyName=False, isAssignment=var_3)


def test_32():
    var_23 = python_code_.atl_n_ocl_OCL_OclModel(
        name="'\\;cAfIRm\\Cz$E33zVK", atl_n_ocl_OCL_OclModel=None
    )
    assert isinstance(var_23, python_code_.atl_n_ocl_OCL_OclModel)


def test_33():
    var_21 = python_code_.TuplePart()
    var_22 = python_code_.atl_n_ocl_OCL_OclModel(
        name="gxJ%h[\x0c&]y",
        atl_n_ocl_OCL_OclModel=var_21,
        atl_n_ocl_OCL_OclModel143={var_21, var_21, 982.56},
    )
    assert isinstance(var_22, python_code_.atl_n_ocl_OCL_OclModel)


def test_34():
    var_87 = '|j7~#g:\\\\v,)>"'
    var_90 = python_code_.OclModel()
    var_91 = {var_90, var_90}
    var_92 = python_code_.atl_n_ocl_ATL_Module(
        isRefining=complex(1051.575441, 1024.11258), atl_n_ocl_ATL_Module=var_91
    )
    assert isinstance(var_92, python_code_.atl_n_ocl_ATL_Module)
    var_93 = python_code_.atl_n_ocl_ATL_Rule(
        name=var_87,
        atl_n_ocl_ATL_Rule={
            "Sc /H:n!~i": True,
            "S[V2P:xDQnc7V?": "4W%In,1_#.{\x0cG3",
            "{;*Sv~yM8T": -800.59,
        },
        ModuleElement=var_92,
    )
    assert isinstance(var_93, python_code_.atl_n_ocl_ATL_Rule)


def test_35():
    var_7 = python_code_.Rule()
    var_9 = python_code_.atl_n_ocl_OCL_Operation(
        name="/^Q", atl_n_ocl_OCL_Operation136=var_7, OclFeature=None
    )
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_Operation)


def test_36():
    var_0 = python_code_.TupleTypeAttribute()
    var_18 = python_code_.atl_n_ocl_OCL_Operation(
        name="qE+q9Ph]uY\\x6B",
        atl_n_ocl_OCL_Operation={-543.73, 829.81},
        atl_n_ocl_OCL_Operation133=var_0,
        OclFeature=None,
    )
    assert isinstance(var_18, python_code_.atl_n_ocl_OCL_Operation)


def test_37():
    var_16 = python_code_.PrimitiveExp()
    var_19 = python_code_.atl_n_ocl_ATL_Rule(
        name="(`\tIZ/", atl_n_ocl_ATL_Rule12=var_16
    )
    assert isinstance(var_19, python_code_.atl_n_ocl_ATL_Rule)


def test_38():
    var_16 = python_code_.atl_n_ocl_OCL_RealExp
    python_code_.atl_n_ocl_OCL_VariableDeclaration(
        id=">",
        varName="atl_n_ocl_ATL_InPattern.OclExpression44.MatchedRule.atl_n_ocl_OCL_Operation",
        atl_n_ocl_OCL_VariableDeclaration108=var_16,
    )


def test_39():
    var_9 = python_code_.atl_n_ocl_OCL_Operation(
        name="A_f", atl_n_ocl_OCL_Operation=set(), atl_n_ocl_OCL_Operation136=None
    )
    assert isinstance(var_9, python_code_.atl_n_ocl_OCL_Operation)
    var_21 = python_code_.atl_n_ocl_OCL_OperationCallExp(
        operationName="atl_n_ocl_ATL_InPattern,atl_n_ocl_ATL_BindingStat,OclModel144",
        atl_n_ocl_OCL_OperationCallExp=set(),
    )
    assert isinstance(var_21, python_code_.atl_n_ocl_OCL_OperationCallExp)


def test_40():
    var_0 = python_code_.atl_n_ocl_OCL_OclUndefinedExp()
    var_1 = python_code_.atl_n_ocl_ATL_IfStat()
    var_2 = python_code_.atl_n_ocl_ATL_ActionBlock()
    var_3 = python_code_.atl_n_ocl_ATL_BindingStat(
        propertyName=None,
        isAssignment=(4305.31,),
        atl_n_ocl_ATL_BindingStat51=var_0,
        Statement60=var_1,
        Statement57=var_0,
        Statement=var_2,
    )
    assert isinstance(var_3, python_code_.atl_n_ocl_ATL_BindingStat)


def test_41():
    var_2 = "OclModel:atl_n_ocl_OCL_LetExp:atl_n_ocl_ATL_ExpressionStat:atl_n_ocl_OCL_VariableDeclaration"
    var_9 = python_code_.atl_n_ocl_ATL_Helper()
    var_43 = python_code_.atl_n_ocl_ATL_Rule(name=var_2)
    assert isinstance(var_43, python_code_.atl_n_ocl_ATL_Rule)
    var_44 = python_code_.OclExpression()
    var_45 = {var_43, var_9}
    var_46 = python_code_.atl_n_ocl_ATL_Module(
        isRefining=var_44, atl_n_ocl_ATL_Module8=var_45
    )
    assert isinstance(var_46, python_code_.atl_n_ocl_ATL_Module)


def test_42():
    var_16 = python_code_.atl_n_ocl_OCL_BooleanType
    python_code_.atl_n_ocl_OCL_VariableDeclaration(
        id=False,
        varName={
            "4": 799.44,
            "atl_n_ocl_OCL_OperationCallExp,_atl_n_ocl_OCL_Attribute__atl_n_ocl_OCL_Attribute128,_atl_n_ocl_OCL_OperationCallExp__atl_n_ocl_OCL_OperationCallExp": "_atl_n_ocl_ATL_MatchedRule__atl_n_ocl_ATL_MatchedRule17 atl_n_ocl_OCL_Attribute _atl_n_ocl_ATL_Rule__atl_n_ocl_ATL_Rule12",
        },
        atl_n_ocl_OCL_VariableDeclaration=var_16,
    )


def test_43():
    var_23 = "|'7~#g:\\\\mv,)>\")"
    var_24 = python_code_.atl_n_ocl_ATL_Rule(
        name="X*{;;m:wg&\x0bMX,,",
        atl_n_ocl_ATL_Rule14=set(),
        atl_n_ocl_ATL_Rule=None,
        ModuleElement=var_23,
    )
    assert isinstance(var_24, python_code_.atl_n_ocl_ATL_Rule)
