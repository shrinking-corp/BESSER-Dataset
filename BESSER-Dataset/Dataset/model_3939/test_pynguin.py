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
    ActionVerb,
    Enum,
    Expression,
    GestureKind,
    NamedElement,
    PlatformMapping,
    RESTURL,
    RESTVerb,
    ReferrableElement,
    ScreenKind,
    Type,
    UIActionKind,
    UIActionSpecification,
    UIComponentOrDataType,
    UrlFragment,
    applauseDsl_AbsoluteRESTURL,
    applauseDsl_Attribute,
    applauseDsl_AttributeReference,
    applauseDsl_DataSource,
    applauseDsl_DataSourceAccessMethod,
    applauseDsl_DataSourceBodySpecification,
    applauseDsl_DataSourceCall,
    applauseDsl_DataType,
    applauseDsl_Entity,
    applauseDsl_EntityMemberCall,
    applauseDsl_EntityMemberCallTail,
    applauseDsl_Expression,
    applauseDsl_ListItemCellDeclaration,
    applauseDsl_LoopVariable,
    applauseDsl_Model,
    applauseDsl_NamedElement,
    applauseDsl_Parameter,
    applauseDsl_Platform,
    applauseDsl_PlatformMapping,
    applauseDsl_RESTMethodCall,
    applauseDsl_RESTSpecification,
    applauseDsl_RESTURL,
    applauseDsl_ReferrableElement,
    applauseDsl_RelativeRESTURL,
    applauseDsl_Screen,
    applauseDsl_ScreenListItemCell,
    applauseDsl_ScreenSection,
    applauseDsl_ScreenSectionItems,
    applauseDsl_StringLiteral,
    applauseDsl_Type,
    applauseDsl_TypeMapping,
    applauseDsl_UIAction,
    applauseDsl_UIActionDeleteAction,
    applauseDsl_UIActionNavigateAction,
    applauseDsl_UIActionSpecification,
    applauseDsl_UIComponentDeclaration,
    applauseDsl_UIComponentMemberCall,
    applauseDsl_UIComponentMemberConfiguration,
    applauseDsl_UIComponentMemberDeclaration,
    applauseDsl_UIComponentOrDataType,
    applauseDsl_UrlFragment,
    applauseDsl_UrlPathFragment,
    applauseDsl_Variable,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.applauseDsl_UIComponentMemberDeclaration(name='r2nFr"Q4}#HFV')
    var_10 = lambda *args, **kwargs: [False, "d0,e^"]
    var_11 = False
    var_12 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_10, returnsMany=var_11
    )
    assert isinstance(var_12, python_code_.applauseDsl_DataSourceAccessMethod)


def test_1():
    var_5 = python_code_.Expression()
    var_65 = python_code_.applauseDsl_DataSourceAccessMethod(
        name="rs8H~O",
        returnsMany=False,
        applauseDsl_DataSourceAccessMethod=None,
        applauseDsl_DataSourceAccessMethod16=set(),
        applauseDsl_DataSourceAccessMethod79=var_5,
    )
    assert isinstance(var_65, python_code_.applauseDsl_DataSourceAccessMethod)


def test_2():
    var_62 = "ky\x0b\x0c"
    var_83 = lambda *args, **kwargs: -1905
    var_86 = python_code_.applauseDsl_DataSource()
    var_88 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_83,
        returnsMany=var_62,
        applauseDsl_DataSourceAccessMethod18=set(),
        applauseDsl_DataSourceAccessMethod=var_86,
    )
    assert isinstance(var_88, python_code_.applauseDsl_DataSourceAccessMethod)


@pytest.mark.xfail(strict=True)
def test_3():
    var_34 = python_code_.applauseDsl_UrlFragment()
    var_62 = "ky\x0b\x0c"
    var_64 = lambda *args, **kwargs: -1905
    var_66 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_64, returnsMany=var_34
    )
    assert isinstance(var_66, python_code_.applauseDsl_DataSourceAccessMethod)
    var_78 = python_code_.applauseDsl_DataSource()
    var_80 = python_code_.PlatformMapping
    var_82 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_64,
        returnsMany=var_62,
        applauseDsl_DataSourceAccessMethod18=set(),
        applauseDsl_DataSourceAccessMethod=var_78,
    )
    assert isinstance(var_82, python_code_.applauseDsl_DataSourceAccessMethod)
    var_83 = python_code_.applauseDsl_RESTURL()
    var_84 = python_code_.applauseDsl_RESTSpecification(
        verb=var_62,
        applauseDsl_RESTSpecification20=var_83,
        applauseDsl_RESTSpecification22=var_80,
    )
    var_85 = python_code_.applauseDsl_Parameter()
    var_86 = {var_85, var_85}
    python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_62,
        returnsMany=var_64,
        applauseDsl_DataSourceAccessMethod18=var_84,
        applauseDsl_DataSourceAccessMethod16=var_86,
    )


def test_4():
    var_0 = python_code_.applauseDsl_AbsoluteRESTURL(port={"`Q&\n", -1, -700})
    assert isinstance(var_0, python_code_.applauseDsl_AbsoluteRESTURL)


def test_5():
    var_57 = lambda *args, **kwargs: True
    var_61 = python_code_.applauseDsl_DataSource()
    var_62 = python_code_.applauseDsl_AbsoluteRESTURL(
        port=var_57, applauseDsl_AbsoluteRESTURL=var_61
    )
    assert isinstance(var_62, python_code_.applauseDsl_AbsoluteRESTURL)


def test_6():
    var_5 = lambda *args, **kwargs: [False, "d0,e^"]
    var_18 = python_code_.applauseDsl_AbsoluteRESTURL(
        port=[632, True], applauseDsl_AbsoluteRESTURL32=var_5
    )
    assert isinstance(var_18, python_code_.applauseDsl_AbsoluteRESTURL)


def test_7():
    var_3 = lambda *args, **kwargs: [False, "d0,e^"]
    var_4 = False
    var_5 = python_code_.applauseDsl_Attribute(
        many=var_4,
        name=var_4,
        applauseDsl_Attribute=var_3,
        applauseDsl_Attribute6=set(),
    )
    assert isinstance(var_5, python_code_.applauseDsl_Attribute)


def test_8():
    python_code_.applauseDsl_Attribute(
        many=False, name=";x", applauseDsl_Attribute6=None
    )


def test_9():
    var_93 = True
    var_94 = lambda *args, **kwargs: True
    var_95 = python_code_.applauseDsl_Entity(
        abstract=var_93, applauseDsl_Entity12=var_94
    )
    assert isinstance(var_95, python_code_.applauseDsl_Entity)


def test_10():
    var_7 = python_code_.applauseDsl_Model()
    python_code_.applauseDsl_NamedElement(name=[], applauseDsl_NamedElement=var_7)


def test_11():
    python_code_.applauseDsl_UIComponentMemberDeclaration(name='r2nFr"Q4}#HFV')


def test_12():
    var_0 = "Hz\tnG&VtH,"
    var_90 = "ky\x0b\x0c"
    var_91 = python_code_.applauseDsl_UIComponentMemberCall()
    var_92 = lambda *args, **kwargs: -1905
    var_93 = python_code_.applauseDsl_ListItemCellDeclaration()
    var_94 = python_code_.applauseDsl_UIComponentDeclaration()
    python_code_.applauseDsl_UIComponentMemberDeclaration(
        name=var_90,
        applauseDsl_UIComponentMemberDeclaration89=var_91,
        applauseDsl_UIComponentMemberDeclaration92=var_92,
        applauseDsl_UIComponentMemberDeclaration=var_93,
        applauseDsl_UIComponentMemberDeclaration71=var_94,
    )
    var_96 = python_code_.applauseDsl_Screen(
        kind=var_0,
        title=var_90,
        applauseDsl_Screen39=b"y\x03\x13\x94D{A\x99\xa0\xabd{\xbda[",
    )
    assert isinstance(var_96, python_code_.applauseDsl_Screen)


def test_13():
    var_0 = "Hz\tnG&VtH,"
    var_90 = "ky\x0b\x0c"
    var_91 = python_code_.applauseDsl_UIComponentMemberCall()
    python_code_.applauseDsl_UIComponentMemberDeclaration(
        name=var_0, applauseDsl_UIComponentMemberDeclaration92=var_91
    )
    var_96 = python_code_.applauseDsl_Screen(
        kind=var_0,
        title=var_90,
        applauseDsl_Screen39=b"y\x03\x13\x94D{A\x99\xa0\xabd{\xbda[",
    )
    assert isinstance(var_96, python_code_.applauseDsl_Screen)


def test_14():
    var_0 = python_code_.ReferrableElement()
    python_code_.applauseDsl_UIComponentMemberDeclaration(
        name="applauseDsl_Screen65._applauseDsl_Screen__applauseDsl_Screen._applauseDsl_Entity__applauseDsl_Entity",
        applauseDsl_UIComponentMemberDeclaration89=var_0,
        applauseDsl_UIComponentMemberDeclaration92=None,
        applauseDsl_UIComponentMemberDeclaration71=None,
    )


def test_15():
    var_8 = python_code_.applauseDsl_UIComponentMemberDeclaration(
        name="'|[AvKYINea`X:1",
        applauseDsl_UIComponentMemberDeclaration92=None,
        applauseDsl_UIComponentMemberDeclaration=None,
    )
    var_15 = "?"
    var_16 = -563
    var_17 = python_code_.applauseDsl_ScreenListItemCell()
    python_code_.applauseDsl_UIAction(
        title=var_8,
        icon=var_15,
        gesture=var_15,
        order=var_16,
        applauseDsl_UIAction61=var_17,
        applauseDsl_UIAction63={},
    )


def test_16():
    var_0 = python_code_.ReferrableElement()
    python_code_.applauseDsl_UIComponentMemberDeclaration(
        name="applauseDsl_Screen65._applauseDsl_Screen__applauseDsl_Screen._applauseDsl_Entity__applauseDsl_Entity",
        applauseDsl_UIComponentMemberDeclaration89=var_0,
        applauseDsl_UIComponentMemberDeclaration92=None,
        applauseDsl_UIComponentMemberDeclaration71=None,
    )
    var_11 = python_code_.PlatformMapping()
    var_12 = python_code_.applauseDsl_LoopVariable()
    var_15 = lambda *args, **kwargs: "8r\n\n_{3^jHMm"
    python_code_.applauseDsl_UIAction(
        title=var_12,
        icon=b":|",
        gesture=var_11,
        order=var_15,
        applauseDsl_UIAction=True,
    )


def test_17():
    var_65 = '""Wl~*'
    python_code_.applauseDsl_ScreenSection(title=var_65)


def test_18():
    var_0 = python_code_.applauseDsl_AbsoluteRESTURL(port={"`Q&\n", -1, -700})
    assert isinstance(var_0, python_code_.applauseDsl_AbsoluteRESTURL)
    var_113 = "_applauseDsl_Entity__applauseDsl_Entit1applauseDsl_ListItemCellDeclaration69_applauseDsl_ScreenSection__applauseDsl_ScreenSection"
    var_117 = "applauseDsl_ReferrableElement-applauseDsl_EntityMemberCallTail-_applauseDsl_Screen__applauseDsl_Screen-applauseDsl_Screen41"
    var_118 = python_code_.applauseDsl_Screen(
        kind=var_117, title=var_117, applauseDsl_Screen65=False
    )
    assert isinstance(var_118, python_code_.applauseDsl_Screen)
    var_119 = python_code_.applauseDsl_ScreenSection(
        title=var_113, applauseDsl_ScreenSection=var_118
    )
    assert isinstance(var_119, python_code_.applauseDsl_ScreenSection)


@pytest.mark.xfail(strict=True)
def test_19():
    var_8 = "applauseDsl_Model:_applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod18:_applauseDsl_Attribute__applauseDsl_Attribute94:_applauseDsl_ReferrableElement__applauseDsl_ReferrableElement"
    var_9 = python_code_.applauseDsl_RESTSpecification
    var_15 = python_code_.applauseDsl_DataSourceCall(
        name=var_8, applauseDsl_DataSourceCall46=None, applauseDsl_DataSourceCall81=None
    )
    python_code_.applauseDsl_ScreenSection(
        title=var_9,
        applauseDsl_ScreenSection45=var_15,
        applauseDsl_ScreenSection48=var_9,
    )


def test_20():
    var_0 = python_code_.applauseDsl_AbsoluteRESTURL(port={"`Q&\n", -1, -700})
    assert isinstance(var_0, python_code_.applauseDsl_AbsoluteRESTURL)
    var_113 = "_applauseDsl_Entity__applauseDsl_Entit1applauseDsl_ListItemCellDeclaration69_applauseDsl_ScreenSection__applauseDsl_ScreenSection"
    var_120 = python_code_.applauseDsl_ScreenSectionItems()
    python_code_.applauseDsl_ScreenSection(
        title=var_113, applauseDsl_ScreenSection48=var_120
    )


def test_21():
    var_0 = "swipe-applauseDsl_EntityMemberCallTail-applauseDsl_Entity4"
    python_code_.applauseDsl_DataSourceCall(
        name=var_0, applauseDsl_DataSourceCall46=var_0
    )


def test_22():
    var_0 = "swipe-applauseDsl_EntityMemberCallTail-applauseDsl_Entity4"
    var_1 = python_code_.applauseDsl_TypeMapping(simpleName=var_0)
    assert isinstance(var_1, python_code_.applauseDsl_TypeMapping)
    var_2 = python_code_.Type()
    python_code_.applauseDsl_DataSourceCall(
        name=var_2, applauseDsl_DataSourceCall76=var_1
    )


@pytest.mark.xfail(strict=True)
def test_23():
    var_1 = "applauseDsl_ScreenSection45"
    var_28 = 2978
    var_54 = python_code_.applauseDsl_UIActionSpecification()
    var_55 = python_code_.applauseDsl_UIAction(
        title=var_1,
        icon=var_1,
        gesture="T",
        order=var_28,
        applauseDsl_UIAction63=None,
        applauseDsl_UIAction=None,
    )
    var_64 = python_code_.applauseDsl_UIActionDeleteAction()
    var_65 = '""Wl~*'
    var_66 = python_code_.applauseDsl_TypeMapping(
        simpleName="applauseDsl_Model,applauseDsl_Screen41",
        applauseDsl_TypeMapping=None,
    )
    assert isinstance(var_66, python_code_.applauseDsl_TypeMapping)
    var_67 = python_code_.Type
    var_68 = python_code_.applauseDsl_DataSourceCall(name=var_65)
    python_code_.applauseDsl_Screen(
        kind=var_54,
        title=var_67,
        applauseDsl_Screen=var_55,
        applauseDsl_Screen39=var_68,
        applauseDsl_Screen43=var_64,
    )


def test_24():
    var_0 = python_code_.applauseDsl_RelativeRESTURL()
    var_1 = "applauseDsl_ScreenSection45"
    var_2 = python_code_.applauseDsl_DataSource()
    python_code_.applauseDsl_DataSourceCall(
        name=var_1,
        applauseDsl_DataSourceCall76=var_0,
        applauseDsl_DataSourceCall81=var_2,
    )


def test_25():
    var_0 = python_code_.applauseDsl_AbsoluteRESTURL(port=-2086)
    assert isinstance(var_0, python_code_.applauseDsl_AbsoluteRESTURL)
    var_77 = python_code_.applauseDsl_UIActionNavigateAction(actionVerb="DefaultList")
    assert isinstance(var_77, python_code_.applauseDsl_UIActionNavigateAction)


@pytest.mark.xfail(strict=True)
def test_26():
    var_84 = python_code_.applauseDsl_UIActionNavigateAction(actionVerb="O?c yN0%mZ+")
    assert isinstance(var_84, python_code_.applauseDsl_UIActionNavigateAction)
    python_code_.applauseDsl_ReferrableElement(
        name={
            "applauseDsl_UrlFragment33": False,
            "applauseDsl_EntityMemberCall": 3205.23,
        },
        applauseDsl_ReferrableElement=var_84,
    )


def test_27():
    var_0 = python_code_.applauseDsl_EntityMemberCall()
    var_1 = python_code_.applauseDsl_ScreenSectionItems()
    var_4 = python_code_.ReferrableElement()
    var_7 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_1, returnsMany=var_4
    )
    assert isinstance(var_7, python_code_.applauseDsl_DataSourceAccessMethod)
    var_10 = python_code_.applauseDsl_DataSourceBodySpecification()
    var_11 = "1=Rm}Ruv0(=\x0bP"
    var_12 = python_code_.applauseDsl_StringLiteral(value=var_11)
    assert isinstance(var_12, python_code_.applauseDsl_StringLiteral)
    var_13 = "b"
    var_14 = python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb=var_13, applauseDsl_UIActionNavigateAction67=var_11
    )
    assert isinstance(var_14, python_code_.applauseDsl_UIActionNavigateAction)
    var_16 = "7yPP\tmPI(t~e-}@zf@"
    var_17 = python_code_.applauseDsl_RESTMethodCall()
    var_18 = python_code_.applauseDsl_DataSource()
    python_code_.applauseDsl_DataSourceCall(
        name=var_16,
        applauseDsl_DataSourceCall76=var_17,
        applauseDsl_DataSourceCall81=var_18,
    )
    var_21 = False
    var_22 = lambda *args, **kwargs: -1001
    var_23 = python_code_.applauseDsl_UIComponentOrDataType
    var_24 = python_code_.applauseDsl_Attribute(
        many=var_10,
        name=var_22,
        applauseDsl_Attribute=var_23,
        applauseDsl_Attribute94=var_0,
    )
    var_25 = {var_24}
    var_26 = python_code_.applauseDsl_Entity(
        abstract=var_21, applauseDsl_Entity1=var_22, applauseDsl_Entity4=var_25
    )
    assert isinstance(var_26, python_code_.applauseDsl_Entity)


def test_28():
    var_4 = '0\tF"-v1,%^'
    python_code_.applauseDsl_ReferrableElement(name=var_4)


def test_29():
    var_0 = "Hz\tnG&VtH,"
    var_1 = "^i"
    var_2 = python_code_.applauseDsl_TypeMapping
    python_code_.applauseDsl_UIAction(
        title=(),
        icon=var_0,
        gesture=var_1,
        order={True, 0},
        applauseDsl_UIAction63=b"\x12\xed}\x14\xb7\x80C\xdf",
        applauseDsl_UIAction=var_2,
    )
    python_code_.applauseDsl_ReferrableElement(
        name=var_0, applauseDsl_ReferrableElement=b"^\xaeP\xe5\x16\xf8"
    )
    python_code_.applauseDsl_ScreenSection(title=var_1)


def test_30():
    var_92 = python_code_.applauseDsl_RESTSpecification(verb=-1105.23)
    var_93 = False
    var_94 = python_code_.applauseDsl_Attribute(
        many=var_93,
        name=var_93,
        applauseDsl_Attribute=var_92,
        applauseDsl_Attribute6=set(),
    )
    assert isinstance(var_94, python_code_.applauseDsl_Attribute)


def test_31():
    var_34 = python_code_.applauseDsl_UrlFragment()
    var_62 = "ky\x0b\x0c"
    var_64 = lambda *args, **kwargs: -1905
    var_66 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_64, returnsMany=var_34
    )
    assert isinstance(var_66, python_code_.applauseDsl_DataSourceAccessMethod)
    var_80 = python_code_.PlatformMapping
    var_83 = python_code_.applauseDsl_RESTURL()
    python_code_.applauseDsl_RESTSpecification(
        verb=var_62,
        applauseDsl_RESTSpecification20=var_83,
        applauseDsl_RESTSpecification22=var_80,
    )


def test_32():
    var_0 = python_code_.applauseDsl_Model()
    python_code_.applauseDsl_NamedElement(
        name=complex(-1612.3557457, 824.505), applauseDsl_NamedElement=var_0
    )
    var_2 = python_code_.applauseDsl_LoopVariable()
    var_3 = python_code_.applauseDsl_UrlFragment()
    var_65 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=None, returnsMany=var_3
    )
    assert isinstance(var_65, python_code_.applauseDsl_DataSourceAccessMethod)
    var_67 = python_code_.applauseDsl_AbsoluteRESTURL
    python_code_.applauseDsl_RESTSpecification(
        verb=var_2,
        applauseDsl_RESTSpecification=var_67,
        applauseDsl_RESTSpecification20=-3119,
    )


def test_33():
    var_0 = python_code_.applauseDsl_EntityMemberCall()
    var_1 = "1gh@X_@~60Vq\x0bY-bu"
    var_2 = "_applauseDsl_Entity__applauseDsl_Entit1applauseDsl_ListItemCellDeclaration69_applauseDsl_ScreenSection__applauseDsl_ScreenSection"
    var_3 = python_code_.applauseDsl_Screen(
        kind=var_2,
        title=var_1,
        applauseDsl_Screen65=None,
        applauseDsl_Screen=var_0,
        applauseDsl_Screen39=None,
        applauseDsl_Screen41=set(),
        applauseDsl_Screen43=set(),
    )
    assert isinstance(var_3, python_code_.applauseDsl_Screen)


def test_34():
    var_3 = "1gh@X_@~60Vq\x0bY-bu"
    var_4 = "_applauseDsl_Entity__applauseDsl_Entity1applauseDsl_ListItemCellDeclaration69_applauseDsl_ScreenSection__applauseDsl_ScreenSection"
    var_5 = python_code_.applauseDsl_Screen(
        kind=var_4,
        title=var_3,
        applauseDsl_Screen39=b"y\x03\x13\x94D{A\x99\xa0\xabd{\xbda[",
    )
    assert isinstance(var_5, python_code_.applauseDsl_Screen)


def test_35():
    python_code_.ReferrableElement()


def test_36():
    var_3 = python_code_.applauseDsl_UIActionSpecification()
    var_4 = python_code_.applauseDsl_StringLiteral(value=var_3)
    assert isinstance(var_4, python_code_.applauseDsl_StringLiteral)
    var_5 = "applauseDsl_ListItemCellDeclaration69"
    var_6 = python_code_.applauseDsl_Screen(
        kind=var_5, title=complex(2480.0, 1024.18178)
    )
    assert isinstance(var_6, python_code_.applauseDsl_Screen)


def test_37():
    var_0 = python_code_.applauseDsl_AbsoluteRESTURL(
        port=-308, applauseDsl_AbsoluteRESTURL=None
    )
    assert isinstance(var_0, python_code_.applauseDsl_AbsoluteRESTURL)
    var_121 = bytes
    var_122 = "r"
    var_123 = -3231
    var_125 = python_code_.applauseDsl_UIAction(
        title=var_122,
        icon=var_122,
        gesture="T",
        order=var_123,
        applauseDsl_UIAction63=None,
        applauseDsl_UIAction=None,
    )
    var_126 = {var_125, var_125}
    var_127 = python_code_.applauseDsl_Screen(
        kind=b"xT\xa9tj\x10\xdf\xdf\x15\xa2\xbb",
        title=var_122,
        applauseDsl_Screen=var_121,
        applauseDsl_Screen43=var_126,
    )
    assert isinstance(var_127, python_code_.applauseDsl_Screen)


def test_38():
    var_81 = "+M7DeDTM<:%m^7q"
    var_82 = python_code_.applauseDsl_UIActionNavigateAction(actionVerb=var_81)
    assert isinstance(var_82, python_code_.applauseDsl_UIActionNavigateAction)
    var_86 = python_code_.applauseDsl_ScreenSectionItems()
    var_87 = python_code_.applauseDsl_ScreenSection(
        title=var_81, applauseDsl_ScreenSection48=var_86
    )
    var_88 = {var_87}
    var_89 = python_code_.applauseDsl_Screen(
        kind=(), title=var_81, applauseDsl_Screen41=var_88, applauseDsl_Screen43=var_88
    )
    assert isinstance(var_89, python_code_.applauseDsl_Screen)


def test_39():
    var_0 = python_code_.applauseDsl_RESTSpecification(verb=set())
    var_1 = python_code_.applauseDsl_UrlPathFragment(name=var_0)
    assert isinstance(var_1, python_code_.applauseDsl_UrlPathFragment)


@pytest.mark.xfail(strict=True)
def test_40():
    var_38 = "Gy$\"kh\\JFIg4H\ny':"
    var_41 = python_code_.UIComponentOrDataType
    var_42 = 'D_Uk\x0b"-lLRjVW:>b'
    var_43 = python_code_.applauseDsl_ScreenSectionItems()
    var_44 = python_code_.applauseDsl_ScreenSection(
        title=var_38, applauseDsl_ScreenSection48=var_43
    )
    var_45 = {var_44}
    var_46 = python_code_.applauseDsl_Screen(
        kind=(), title=var_38, applauseDsl_Screen41=var_45, applauseDsl_Screen43=var_45
    )
    assert isinstance(var_46, python_code_.applauseDsl_Screen)
    var_53 = python_code_.applauseDsl_AbsoluteRESTURL(port=["T", 0])
    assert isinstance(var_53, python_code_.applauseDsl_AbsoluteRESTURL)
    python_code_.applauseDsl_ScreenSection(
        title=var_42,
        applauseDsl_ScreenSection45=var_41,
        applauseDsl_ScreenSection=var_41,
    )
    python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb=var_38, applauseDsl_UIActionNavigateAction=var_46
    )


@pytest.mark.xfail(strict=True)
def test_41():
    var_2 = "applauseDsl_Type,applauseDsl_UIComponentMemberCall"
    python_code_.applauseDsl_UIComponentMemberDeclaration(name=var_2)
    var_5 = "{{]EUZ4L2"
    var_6 = python_code_.applauseDsl_ScreenSection(
        title="applauseDsl_DataSourceAccessMethod",
        applauseDsl_ScreenSection45=1277.7,
        applauseDsl_ScreenSection48=-2165.1,
        applauseDsl_ScreenSection=set(),
    )
    python_code_.applauseDsl_DataSourceCall(
        name=var_5, applauseDsl_DataSourceCall46=var_6
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_0 = python_code_.applauseDsl_RESTMethodCall
    var_1 = python_code_.applauseDsl_ScreenSectionItems()
    python_code_.applauseDsl_ScreenSection(
        title={True, False, True},
        applauseDsl_ScreenSection45=var_0,
        applauseDsl_ScreenSection48=var_1,
    )
    var_4 = python_code_.applauseDsl_Expression()
    var_6 = '#AXvq@$\n)"+\rce^#m'
    var_7 = python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb=var_6, applauseDsl_UIActionNavigateAction67=var_4
    )
    assert isinstance(var_7, python_code_.applauseDsl_UIActionNavigateAction)
    var_8 = False
    var_9 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=-1707, returnsMany=var_8
    )
    assert isinstance(var_9, python_code_.applauseDsl_DataSourceAccessMethod)
    python_code_.applauseDsl_RESTSpecification(
        verb=[
            "_applauseDsl_DataSourceCall__applauseDsl_DataSourceCall76 applauseDsl_RESTSpecification _applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod16",
            -26.19,
            1857.53,
        ],
        applauseDsl_RESTSpecification=var_9,
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = python_code_.applauseDsl_Model()
    python_code_.applauseDsl_NamedElement(name="W.)QBE%#*yk,(")
    var_2 = -1774
    var_3 = bytes
    var_4 = python_code_.applauseDsl_AbsoluteRESTURL(
        port=var_2,
        applauseDsl_AbsoluteRESTURL=complex(749.244296, -2798.0),
        applauseDsl_AbsoluteRESTURL32=var_3,
    )
    assert isinstance(var_4, python_code_.applauseDsl_AbsoluteRESTURL)
    var_5 = "r"
    var_6 = -3231
    var_7 = python_code_.applauseDsl_UIActionSpecification()
    var_8 = python_code_.applauseDsl_UIAction(
        title=var_3,
        icon=-692.68,
        gesture={250.89},
        order=var_6,
        applauseDsl_UIAction63=var_7,
    )
    var_9 = {var_8, var_8}
    var_10 = python_code_.applauseDsl_Screen(
        kind=b"xT\xa9tj\x10\xdf\xdf\x15\xa2\xbb",
        title=var_5,
        applauseDsl_Screen=var_3,
        applauseDsl_Screen43=var_9,
    )
    assert isinstance(var_10, python_code_.applauseDsl_Screen)
    var_12 = python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb=var_6, applauseDsl_UIActionNavigateAction67=var_0
    )
    assert isinstance(var_12, python_code_.applauseDsl_UIActionNavigateAction)
    python_code_.applauseDsl_ReferrableElement(
        name=var_10, applauseDsl_ReferrableElement=var_12
    )


def test_44():
    var_8 = python_code_.applauseDsl_UIComponentMemberDeclaration(
        name='iX"EQGqT\n}',
        applauseDsl_UIComponentMemberDeclaration=None,
        applauseDsl_UIComponentMemberDeclaration71=None,
    )
    var_15 = python_code_.applauseDsl_TypeMapping(
        simpleName="s>3<", applauseDsl_TypeMapping=var_8
    )
    assert isinstance(var_15, python_code_.applauseDsl_TypeMapping)


def test_45():
    var_0 = "swipe-applauseDsl_EntityMemberCallTail-applauseDsl_Entity4"
    var_1 = python_code_.applauseDsl_TypeMapping(simpleName=var_0)
    assert isinstance(var_1, python_code_.applauseDsl_TypeMapping)


def test_46():
    var_0 = python_code_.applauseDsl_AbsoluteRESTURL(
        port=-315, applauseDsl_AbsoluteRESTURL=None
    )
    assert isinstance(var_0, python_code_.applauseDsl_AbsoluteRESTURL)
    python_code_.applauseDsl_UIComponentMemberDeclaration(
        name=-1,
        applauseDsl_UIComponentMemberDeclaration92=None,
        applauseDsl_UIComponentMemberDeclaration71=True,
        applauseDsl_UIComponentMemberDeclaration73=True,
    )


def test_47():
    var_95 = True
    var_97 = python_code_.applauseDsl_Entity(abstract=var_95)
    assert isinstance(var_97, python_code_.applauseDsl_Entity)
    var_98 = python_code_.applauseDsl_Attribute(
        many=var_95, name=None, applauseDsl_Attribute=var_97
    )
    assert isinstance(var_98, python_code_.applauseDsl_Attribute)


def test_48():
    python_code_.applauseDsl_NamedElement(name=())


@pytest.mark.xfail(strict=True)
def test_49():
    var_77 = python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb="_applauseDsl_RESTSpecification__applauseDsl_RESTSpecification20"
    )
    assert isinstance(var_77, python_code_.applauseDsl_UIActionNavigateAction)
    var_97 = python_code_.applauseDsl_Platform()
    var_100 = python_code_.applauseDsl_AttributeReference()
    var_101 = python_code_.applauseDsl_Entity(abstract=var_97)
    assert isinstance(var_101, python_code_.applauseDsl_Entity)
    python_code_.applauseDsl_Entity(
        abstract=var_100, applauseDsl_Entity=var_101, applauseDsl_Entity1=-2885
    )


def test_50():
    var_42 = False
    var_43 = lambda *args, **kwargs: True
    var_44 = python_code_.applauseDsl_Entity(abstract=var_42, applauseDsl_Entity=var_43)
    assert isinstance(var_44, python_code_.applauseDsl_Entity)


@pytest.mark.xfail(strict=True)
def test_51():
    var_1 = "1gh@X_@~60Vq\x0bY-bu"
    var_2 = "_applauseDsl_Entity__applauseDsl_Entity1applauseDsl_ListItemCellDeclaration69_applauseDsl_ScreenSection__applauseDsl_ScreenSection"
    var_3 = python_code_.applauseDsl_Screen(
        kind=var_2,
        title=var_1,
        applauseDsl_Screen39=b"y\x03\x13\x94D{A\x99\xa0\xabd{\xbda[",
    )
    assert isinstance(var_3, python_code_.applauseDsl_Screen)
    python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb=var_1, applauseDsl_UIActionNavigateAction=var_3
    )


def test_52():
    var_0 = "Hz\tnG&VtH,"
    var_91 = python_code_.UIActionSpecification()
    var_92 = False
    var_95 = python_code_.applauseDsl_Attribute(
        many=var_92,
        name=var_0,
        applauseDsl_Attribute94=var_91,
        applauseDsl_Attribute104=var_92,
    )
    assert isinstance(var_95, python_code_.applauseDsl_Attribute)


def test_53():
    var_5 = lambda *args, **kwargs: [False, "d0,e^"]
    var_25 = False
    var_26 = python_code_.applauseDsl_Attribute(
        many=var_25,
        name=var_5,
        applauseDsl_Attribute=var_5,
        applauseDsl_Attribute94=[],
        applauseDsl_Attribute99=-2900,
    )
    assert isinstance(var_26, python_code_.applauseDsl_Attribute)


@pytest.mark.xfail(strict=True)
def test_54():
    var_1 = python_code_.applauseDsl_ScreenSectionItems()
    var_2 = python_code_.applauseDsl_ScreenSection(
        title={}, applauseDsl_ScreenSection48=var_1
    )
    var_4 = python_code_.NamedElement
    python_code_.applauseDsl_RESTSpecification(verb=var_4)
    var_6 = python_code_.applauseDsl_UIComponentMemberCall()
    var_9 = "|W6^o\x0bO!%gvH(`j16"
    var_10 = python_code_.applauseDsl_UrlPathFragment(name=var_9)
    assert isinstance(var_10, python_code_.applauseDsl_UrlPathFragment)
    var_13 = python_code_.applauseDsl_DataSource()
    python_code_.applauseDsl_DataSourceCall(
        name=var_9,
        applauseDsl_DataSourceCall=var_6,
        applauseDsl_DataSourceCall81=var_13,
    )
    var_17 = "_applauseDsl_UIComponentMemberDeclaration__applauseDsl_UIComponentMemberDeclaration73-_applauseDsl_Entity__applauseDsl_Entity12-applauseDsl_Attribute"
    var_18 = python_code_.applauseDsl_UIActionNavigateAction(actionVerb=var_17)
    assert isinstance(var_18, python_code_.applauseDsl_UIActionNavigateAction)
    python_code_.applauseDsl_Screen(
        kind=var_4, title=var_4, applauseDsl_Screen65=var_18, applauseDsl_Screen43=var_2
    )


@pytest.mark.xfail(strict=True)
def test_55():
    var_0 = python_code_.UrlFragment()
    var_2 = "applauseDsl_ScreenSection45._applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod79.applauseDsl_Entity.applauseDsl_UIAction"
    var_3 = "sD-kyaOH-uA9dL%"
    var_4 = python_code_.applauseDsl_UIActionNavigateAction(
        actionVerb=var_3,
        applauseDsl_UIActionNavigateAction=b"\x9e\x04i\xd3\x1b\xca\xd9\x0e\x12#\x8f\xe0\xef\x81\xa6x\xd8~\x02",
    )
    assert isinstance(var_4, python_code_.applauseDsl_UIActionNavigateAction)
    python_code_.applauseDsl_Screen(kind=var_3, title=var_2, applauseDsl_Screen41=var_0)


def test_56():
    python_code_.applauseDsl_UIComponentMemberDeclaration(name='r2nFr"Q4}#HFV')
    var_5 = lambda *args, **kwargs: [False, "d0,e^"]
    var_6 = True
    var_7 = python_code_.applauseDsl_DataSourceAccessMethod(
        name=var_5, returnsMany=var_6
    )
    assert isinstance(var_7, python_code_.applauseDsl_DataSourceAccessMethod)
    var_18 = python_code_.applauseDsl_Entity(abstract=False, applauseDsl_Entity4={1})
    assert isinstance(var_18, python_code_.applauseDsl_Entity)


def test_57():
    var_0 = python_code_.applauseDsl_Model()
    python_code_.applauseDsl_NamedElement(
        name=complex(-1612.3557457, 824.505), applauseDsl_NamedElement=var_0
    )
    var_97 = True
    var_98 = 'A"<)$x)\tU'
    var_99 = python_code_.applauseDsl_Type()
    var_100 = python_code_.applauseDsl_Attribute(
        many=134.91, name=var_98, applauseDsl_Attribute6=var_99
    )
    var_101 = {var_100, var_100, var_100, var_100, var_100}
    var_102 = python_code_.applauseDsl_Entity(
        abstract=var_97, applauseDsl_Entity4=var_101
    )
    assert isinstance(var_102, python_code_.applauseDsl_Entity)
