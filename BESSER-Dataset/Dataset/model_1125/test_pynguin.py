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
    Enum,
    FIELD_FORMAT,
    UNIT,
    cjsidl_EObject,
    cjsidl_action,
    cjsidl_actionList,
    cjsidl_arrayDef,
    cjsidl_bitfieldDef,
    cjsidl_bodyDef,
    cjsidl_bodyRef,
    cjsidl_bodyScopedRef,
    cjsidl_constDef,
    cjsidl_constReference,
    cjsidl_containerDef,
    cjsidl_containerRef,
    cjsidl_declaredConstSet,
    cjsidl_declaredConstSetRef,
    cjsidl_declaredEventDef,
    cjsidl_declaredTypeSet,
    cjsidl_declaredTypeSetRef,
    cjsidl_defaultState,
    cjsidl_defaultTransition,
    cjsidl_description,
    cjsidl_entry,
    cjsidl_eventDef,
    cjsidl_exit,
    cjsidl_fixedFieldDef,
    cjsidl_fixedLenString,
    cjsidl_footerDef,
    cjsidl_footerRef,
    cjsidl_footerScopedRef,
    cjsidl_formatEnumDef,
    cjsidl_guard,
    cjsidl_guardAction,
    cjsidl_guardParam,
    cjsidl_headerDef,
    cjsidl_headerRef,
    cjsidl_headerScopedRef,
    cjsidl_internalEventSet,
    cjsidl_internalTransition,
    cjsidl_jaus,
    cjsidl_listDef,
    cjsidl_messageDef,
    cjsidl_messageRef,
    cjsidl_messageScopedRef,
    cjsidl_messageSet,
    cjsidl_messages,
    cjsidl_nextState,
    cjsidl_popTransition,
    cjsidl_protocolBehavior,
    cjsidl_pushTransition,
    cjsidl_recordDef,
    cjsidl_refAttr,
    cjsidl_references,
    cjsidl_scaledRangeDef,
    cjsidl_scopedConstId,
    cjsidl_scopedEventType,
    cjsidl_scopedType,
    cjsidl_scopedTypeId,
    cjsidl_sendActionList,
    cjsidl_sequenceDef,
    cjsidl_serviceDef,
    cjsidl_simpleNumericType,
    cjsidl_simpleTransition,
    cjsidl_startState,
    cjsidl_state,
    cjsidl_stateMachine,
    cjsidl_subField,
    cjsidl_taggedItemDef,
    cjsidl_taggedUnitsEnum,
    cjsidl_transParam,
    cjsidl_transParams,
    cjsidl_transition,
    cjsidl_typeDef,
    cjsidl_typeReference,
    cjsidl_valueRange,
    cjsidl_valueSetDef,
    cjsidl_valueSpec,
    cjsidl_varField,
    cjsidl_varFormatField,
    cjsidl_varLenField,
    cjsidl_varLenString,
    cjsidl_variantDef,
    containerDef,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.cjsidl_recordDef()
    var_1 = "?/bNe{Cpa\n\n~Hr"
    var_6 = "iUP"
    var_10 = python_code_.cjsidl_formatEnumDef(
        fieldFormat=complex(1403.6, 228.38), fieldFormatStr=-3384.9, index=-276.63
    )
    var_11 = "r"
    var_12 = python_code_.cjsidl_containerRef(
        comment=var_11, optional=var_10, name=b"\xebZ\xf5)#\xc1E\xa1>\x1c\x13?\xfc\xd2W"
    )
    python_code_.cjsidl_listDef(
        countComment=var_11,
        minCount=var_0,
        maxCount=var_1,
        cjsidl_listDef383={},
        cjsidl_listDef392=var_6,
        cjsidl_listDef395=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = "8VuN2'XO"
    python_code_.cjsidl_declaredEventDef(comment=var_0, name=var_0)
    var_2 = "7.m\\"
    python_code_.cjsidl_messageScopedRef(
        name=var_0,
        comment=var_2,
        cjsidl_messageScopedRef466={-1412, -1, "cjsidl_scaledRangeDef368"},
    )
    var_6 = lambda *args, **kwargs: "_cjsidl_valueRange__cjsidl_valueRange359"
    var_7 = "cjsidl_protocolBehavior69"
    var_8 = 'H?j!RBEs"mSsy6'
    var_9 = "EDF<gl[wld"
    var_10 = python_code_.cjsidl_listDef(
        countComment=var_9, minCount=var_0, maxCount=var_8, cjsidl_listDef=var_6
    )
    assert isinstance(var_10, python_code_.cjsidl_listDef)
    python_code_.cjsidl_containerDef(
        comment=var_2, optional=var_6, name=var_7, cjsidl_containerDef399=var_10
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = "(B*^"
    python_code_.cjsidl_eventDef(name=var_0)
    var_3 = "cjsidl_messages50_cjsidl_headerDef__cjsidl_headerDef245"
    var_4 = "_cjsidl_transition__cjsidl_transition122,_cjsidl_exit__cjsidl_exit110,cjsidl_transParam176"
    var_5 = python_code_.cjsidl_constDef(
        comment=var_4, name=var_4, constValue=var_3, fieldUnits=var_0
    )
    python_code_.cjsidl_constReference(
        comment=var_4,
        cjsidl_constReference346={""},
        cjsidl_constReference390=var_3,
        cjsidl_constReference402=var_0,
        cjsidl_constReference454=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_1 = "_cjsidl_protocolBehavior__cjsidl_protocolBehavior:cjsidl_state165:_cjsidl_refAttr__cjsidl_refAttr:_cjsidl_taggedUnitsEnum__cjsidl_taggedUnitsEnum339"
    var_2 = "^zW"
    var_3 = python_code_.cjsidl_footerRef(comment=var_1, name=var_2)
    var_4 = python_code_.cjsidl_entry
    python_code_.cjsidl_declaredConstSet(
        constName=var_4,
        name=set(),
        constSetVersion=3,
        cjsidl_declaredConstSet23={
            "cjsidl_varLenString": False,
            "1YdaI&wgCR\n\x0c]1`e^&": "y1yon(=\r=.WLk",
        },
    )
    var_8 = "o^z"
    var_9 = "m7uog"
    var_10 = python_code_.cjsidl_declaredTypeSetRef(comment=var_8, name=var_9)
    python_code_.cjsidl_declaredTypeSet(
        typeName=var_2, name=var_2, version=var_3, cjsidl_declaredTypeSet189=var_10
    )


def test_4():
    var_1 = "_cjsidl_valueSetDef__cjsidl_valueSetDef351._cjsidl_action__cjsidl_action181.cjsidl_nextState161.cjsidl_serviceDef11"
    var_2 = lambda *args, **kwargs: True
    var_3 = python_code_.cjsidl_bodyRef(
        comment=var_1, name=var_2, cjsidl_bodyRef251=True
    )
    python_code_.cjsidl_description(content=var_3)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "cjsidl_EObject234 _cjsidl_subField__cjsidl_subField _cjsidl_messageDef__cjsidl_messageDef473"
    var_1 = python_code_.cjsidl_containerRef(
        comment=b"\xbf7\x89\xf6\x14\xf5\xd0+\x0fz",
        optional=(False, -2908, -383),
        name=var_0,
        cjsidl_containerRef419=True,
    )
    python_code_.cjsidl_action(
        comment=var_1, name="!", cjsidl_action=-259, cjsidl_action183={1421.92, True, 1}
    )
    var_3 = python_code_.cjsidl_bodyScopedRef
    var_4 = python_code_.cjsidl_bodyDef(comment=(), name=var_3, cjsidl_bodyDef=var_3)
    var_5 = "cjsidl_constReference408 cjsidl_pushTransition154 _cjsidl_declaredConstSetRef__cjsidl_declaredConstSetRef27"
    var_6 = "_cjsidl_varField__cjsidl_varField"
    var_7 = python_code_.cjsidl_scopedConstId()
    python_code_.cjsidl_varLenString(
        comment=var_6,
        optional=var_5,
        name=var_5,
        lowerLim=var_3,
        upperLim=var_0,
        cjsidl_varLenString299=var_7,
    )
    var_9 = "/\nqoVX@hBVk\x0bk"
    var_10 = python_code_.cjsidl_recordDef()
    python_code_.cjsidl_varLenField(
        lowerLim=var_4,
        upperLim=var_5,
        comment=var_5,
        optional=var_3,
        fieldFormat=var_0,
        name=var_9,
        countComment=var_3,
        cjsidl_varLenField443=var_10,
    )
    var_12 = lambda *args, **kwargs: "ir5"
    python_code_.cjsidl_listDef(
        countComment=var_5,
        minCount=var_9,
        maxCount=True,
        cjsidl_listDef383=var_12,
        cjsidl_listDef389=var_3,
        cjsidl_listDef395=var_1,
    )


def test_6():
    var_0 = '4s26D"nr;f\x0cMUQ3'
    var_1 = lambda *args, **kwargs: False
    python_code_.cjsidl_arrayDef(
        comment=var_0, optional=333.91, name=var_0, arraySize=var_1
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_1 = int
    python_code_.cjsidl_stateMachine(
        comment={
            "cjsidl_valueSetDef381": -1564.61,
            "q\r\rB>L\tAy\r=:x0wf6W": True,
            "_cjsidl_valueRange__cjsidl_valueRange365-cjsidl_declaredTypeSet30-_cjsidl_serviceDef__cjsidl_serviceDef7-_cjsidl_simpleNumericType__cjsidl_simpleNumericType309": 3187,
        },
        name=var_1,
    )
    var_4 = "Z)T"
    var_5 = python_code_.cjsidl_simpleTransition(comment=var_1)
    python_code_.cjsidl_nextState(comment=var_4, cjsidl_nextState=var_5)


@pytest.mark.xfail(strict=True)
def test_8():
    python_code_.cjsidl_entry(comment=(), cjsidl_entry106=set())
    var_2 = "AMP-cjsidl_bodyDef249-_cjsidl_transParam__cjsidl_transParam"
    var_4 = python_code_.cjsidl_headerDef
    python_code_.cjsidl_startState(comment=var_4)
    var_6 = python_code_.cjsidl_popTransition(comment=[])
    python_code_.cjsidl_transition(
        comment=var_2,
        type=var_2,
        name=var_4,
        cjsidl_transition128=var_4,
        cjsidl_transition157=var_6,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.cjsidl_footerDef
    var_1 = "_cjsidl_varLenString__cjsidl_varLenString296,_cjsidl_state__cjsidl_state88,cjsidl_headerDef245"
    var_2 = python_code_.cjsidl_startState(comment=var_1)
    var_3 = python_code_.cjsidl_stateMachine(
        comment=var_1, name=var_0, cjsidl_stateMachine=var_1
    )
    var_4 = lambda *args, **kwargs: 1712
    python_code_.cjsidl_state(
        comment=False,
        initial=var_0,
        name=var_1,
        cjsidl_state73=var_2,
        cjsidl_state84=var_3,
        cjsidl_state94=[
            841,
            -1761.14,
            "WATT_PER_METER_KELVIN-_cjsidl_footerDef__cjsidl_footerDef253-METER_PER_SEC_SQR",
        ],
        cjsidl_state168=var_4,
        cjsidl_state96=var_4,
    )
