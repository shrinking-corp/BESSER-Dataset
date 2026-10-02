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
    ComplexHTMLTypeKinds,
    CoreComponent,
    DataAccessKinds,
    DynamicPage,
    EJSLPart,
    Enum,
    Extension,
    HTMLTypes,
    InternalLink,
    Link,
    Page,
    PageActionKind,
    PageActionPositionKind,
    PageKinds,
    PluginKinds,
    Section,
    SimpleHTMLTypeKinds,
    StandardTypeKinds,
    Type,
    date,
    datetime,
    eJSL_Attribute,
    eJSL_Author,
    eJSL_BackendSection,
    eJSL_CMSCore,
    eJSL_CMSExtension,
    eJSL_Class,
    eJSL_ComplexHTMLTypes,
    eJSL_Component,
    eJSL_ComponentReference,
    eJSL_ContextLink,
    eJSL_CssBlock,
    eJSL_CustomPage,
    eJSL_Datatype,
    eJSL_DatatypeReference,
    eJSL_DetailPageField,
    eJSL_DetailsPage,
    eJSL_DynamicPage,
    eJSL_EJSLModel,
    eJSL_EJSLPart,
    eJSL_Entity,
    eJSL_Entitypackage,
    eJSL_Extension,
    eJSL_ExtensionPackage,
    eJSL_ExternalLink,
    eJSL_Feature,
    eJSL_FrontendSection,
    eJSL_HTMLTypes,
    eJSL_IndexPage,
    eJSL_InternalLink,
    eJSL_KeyValuePair,
    eJSL_Language,
    eJSL_Library,
    eJSL_Link,
    eJSL_LinkParameter,
    eJSL_Manifestation,
    eJSL_Method,
    eJSL_MethodParameter,
    eJSL_Module,
    eJSL_Package,
    eJSL_Page,
    eJSL_PageAction,
    eJSL_PageReference,
    eJSL_Parameter,
    eJSL_ParameterGroup,
    eJSL_Plugin,
    eJSL_Position,
    eJSL_PositionParameter,
    eJSL_Reference,
    eJSL_Section,
    eJSL_SimpleHTMLTypes,
    eJSL_StandardTypes,
    eJSL_StaticPage,
    eJSL_Template,
    eJSL_Type,
    eJSL_coreFeature,
    time,
)


def test_0():
    var_9 = "bRc/KEo/G"
    python_code_.eJSL_EJSLModel(name=var_9)
    var_11 = python_code_.StandardTypeKinds.Text
    var_13 = python_code_.eJSL_Manifestation
    var_14 = python_code_.eJSL_StaticPage(preserve=var_13, HTMLBody=None)
    assert isinstance(var_14, python_code_.eJSL_StaticPage)
    var_16 = python_code_.DynamicPage()
    var_17 = True
    var_18 = python_code_.eJSL_StaticPage(preserve=var_17, HTMLBody=var_16)
    var_19 = python_code_.Extension()
    var_21 = python_code_.eJSL_PositionParameter(
        name=-3145.15, divid=var_9, type=var_9, eJSL_PositionParameter=None
    )
    assert isinstance(var_21, python_code_.eJSL_PositionParameter)
    var_22 = python_code_.eJSL_KeyValuePair(
        name=var_9, value=var_9, eJSL_KeyValuePair=var_19, eJSL_KeyValuePair185=var_21
    )
    assert isinstance(var_22, python_code_.eJSL_KeyValuePair)
    var_23 = python_code_.eJSL_Type()
    python_code_.eJSL_Entity(
        name=True,
        preserve=var_11,
        eJSL_Entity=set(),
        eJSL_Entity44={"3/D\x0b\taeLi": 708, "!Lfd9 6wg": False},
        eJSL_Entity42=var_23,
        eJSL_Entity59={-1195},
        eJSL_Entity159=var_13,
    )
    python_code_.eJSL_ComponentReference(core=var_9)
    var_34 = "_eJSL_Extension__eJSL_Extension116"
    var_35 = python_code_.eJSL_Position(name=var_13)
    var_36 = python_code_.eJSL_PositionParameter(
        name=var_9, divid=var_34, type=var_18, eJSL_PositionParameter=var_35
    )
    assert isinstance(var_36, python_code_.eJSL_PositionParameter)


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = "o=n+KV!gh']VQ"
    python_code_.eJSL_Attribute(
        name=var_0,
        preserve=5372,
        isunique=None,
        id=b"1c\xf0~u\xcc\xf3`\x82X1Od",
        isprimary=var_0,
        eJSL_Attribute80=var_0,
    )
    var_2 = "QA+"
    python_code_.eJSL_PageAction(
        name=var_0,
        pageActionType=var_2,
        pageActionPosition=var_0,
        eJSL_PageAction=var_2,
    )
    var_4 = python_code_.eJSL_InternalLink(
        name=b"\xe54\x8af\xdf\xb9\xc9\x99\x9b\xa1>P\x03k>",
        eJSL_InternalLink=complex(-1551.717159, 745.2758),
    )
    assert isinstance(var_4, python_code_.eJSL_InternalLink)
    var_5 = "webservice"
    var_6 = python_code_.eJSL_Package(name=var_5)
    assert isinstance(var_6, python_code_.eJSL_Package)
    var_7 = python_code_.DataAccessKinds.backendDAO
    var_9 = python_code_.eJSL_Datatype
    python_code_.eJSL_Language(sys=(), name=var_2, eJSL_Language=var_9)
    python_code_.eJSL_EJSLModel(name=511)
    var_12 = "eJSL_Parameter32"
    var_13 = python_code_.eJSL_ExternalLink(target=var_9, label=var_12)
    assert isinstance(var_13, python_code_.eJSL_ExternalLink)
    var_14 = python_code_.eJSL_Class(name=var_9)
    assert isinstance(var_14, python_code_.eJSL_Class)
    var_15 = "{8xHgxx$:\r"
    python_code_.eJSL_Datatype(name=var_15, type=var_14, eJSL_Datatype41=var_4)
    var_21 = "bottom-_eJSL_Parameter__eJSL_Parameter"
    var_22 = python_code_.eJSL_SimpleHTMLTypes(htmltype=var_21)
    assert isinstance(var_22, python_code_.eJSL_SimpleHTMLTypes)
    var_26 = python_code_.eJSL_FrontendSection()
    var_30 = python_code_.eJSL_Feature()
    var_31 = python_code_.eJSL_Parameter(
        name=complex(2554.96804, -1151.538),
        defaultvalue=complex(206.596093, 2131.3099),
        label=var_15,
        size=var_26,
        descripton={'Jwn#w_vbn\\-b"As&': "z0"},
        eJSL_Parameter=[],
        eJSL_Parameter21=var_30,
    )
    var_32 = {var_31, var_31, var_31, var_31, var_31}
    python_code_.eJSL_Page(
        name=var_7,
        eJSL_Page=var_30,
        eJSL_Page64=var_22,
        eJSL_Page67=var_32,
        eJSL_Page70=var_9,
        eJSL_Page106=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = python_code_.eJSL_Library()
    var_1 = python_code_.PageActionPositionKind.center
    var_2 = python_code_.eJSL_ContextLink
    var_3 = python_code_.eJSL_Class(
        name=var_2,
        eJSL_Class=var_1,
        eJSL_Class151=(-1666,),
        eJSL_Class161=b"\xe4\xe1\xf6\xc4\xeah.V\xc9|y\xb4\x1d\x14(Q\xf8",
    )
    assert isinstance(var_3, python_code_.eJSL_Class)
    var_4 = {var_3, var_3, var_3}
    python_code_.eJSL_Class(
        name=-2007.52,
        eJSL_Class=var_0,
        eJSL_Class153=var_3,
        eJSL_Class156=var_3,
        eJSL_Class154=var_4,
    )


def test_3():
    var_0 = python_code_.eJSL_Link
    var_1 = "1r,12"
    python_code_.eJSL_Author(name=None, authoremail=var_0, authorurl=var_1)
    var_3 = python_code_.eJSL_ExternalLink(target=var_1, label=var_1)
    assert isinstance(var_3, python_code_.eJSL_ExternalLink)


def test_4():
    var_63 = python_code_.eJSL_Template()
    python_code_.eJSL_CssBlock(selector=True, eJSL_CssBlock=var_63)


def test_5():
    var_0 = python_code_.eJSL_ExtensionPackage()
    var_3 = python_code_.eJSL_DatatypeReference()
    var_4 = "na:Ay5>oipMk\x0c["
    var_5 = lambda *args, **kwargs: []
    var_6 = python_code_.eJSL_CssBlock(selector=var_4)
    var_7 = python_code_.eJSL_KeyValuePair(
        name=(True, True, -1965.86),
        value=var_5,
        eJSL_KeyValuePair96=var_0,
        eJSL_KeyValuePair180=var_3,
        eJSL_KeyValuePair188=var_6,
    )
    assert isinstance(var_7, python_code_.eJSL_KeyValuePair)
    var_8 = {var_7}
    var_9 = python_code_.eJSL_Language(
        sys="eJSL_CssBlock187,UNPUBLISH", name=var_4, eJSL_Language179=var_8
    )
    assert isinstance(var_9, python_code_.eJSL_Language)
    var_20 = "c\nHM^"
    python_code_.eJSL_KeyValuePair(
        name=var_20,
        value=var_20,
        eJSL_KeyValuePair93=complex(-270.65537, -2232.633),
        eJSL_KeyValuePair188=var_0,
    )


def test_6():
    python_code_.eJSL_ComponentReference(core=["? 1l{#6C(5+gZ0f(>xl", True, -523])
    var_6 = "eJSL_Parameter68_eJSL_Entity__eJSL_Entity"
    var_7 = python_code_.eJSL_Plugin(type=var_6)
    assert isinstance(var_7, python_code_.eJSL_Plugin)
    var_8 = python_code_.eJSL_ComplexHTMLTypes(htmltype=var_6)
    assert isinstance(var_8, python_code_.eJSL_ComplexHTMLTypes)


@pytest.mark.xfail(strict=True)
def test_7():
    var_4 = "na:Ay5>oipMk["
    var_22 = python_code_.eJSL_ComplexHTMLTypes(htmltype=var_4)
    assert isinstance(var_22, python_code_.eJSL_ComplexHTMLTypes)
    var_24 = '"e>2\ruRD\nk{['
    var_25 = python_code_.eJSL_Plugin(type=var_22)
    assert isinstance(var_25, python_code_.eJSL_Plugin)
    var_26 = True
    var_27 = python_code_.eJSL_StandardTypes(
        type=var_4,
        notnull=complex(2119.70519, 185.4881322),
        default=var_24,
        autoincrement=var_26,
    )
    assert isinstance(var_27, python_code_.eJSL_StandardTypes)
    var_28 = python_code_.eJSL_Page(name=var_4, eJSL_Page67="")
    python_code_.eJSL_PageReference(sect=var_24, eJSL_PageReference125=var_28)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = "$vt1!(h~~R"
    var_1 = python_code_.eJSL_Section()
    var_2 = python_code_.eJSL_PageReference(
        sect=var_0, eJSL_PageReference133=b"r\x80\xba\xfd\x12", eJSL_PageReference=var_1
    )
    python_code_.eJSL_ComponentReference(core=var_0, eJSL_ComponentReference=var_2)


def test_9():
    var_4 = "na:Ay5>oipMk\x0c["
    python_code_.eJSL_CssBlock(selector=var_4)
    var_17 = python_code_.eJSL_EJSLPart()
    python_code_.eJSL_ParameterGroup(name=None, label=True)
    var_24 = python_code_.eJSL_Type
    var_33 = python_code_.eJSL_Language(sys=var_17, name=var_24)
    var_34 = {var_33, var_33}
    python_code_.eJSL_Extension(
        name="_eJSL_Entity__eJSL_Entity77", eJSL_Extension114=var_34
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = python_code_.eJSL_ExtensionPackage()
    var_2 = python_code_.eJSL_CMSCore()
    var_3 = python_code_.eJSL_DatatypeReference()
    var_4 = "na:Ay5>oipMk\x0c["
    var_5 = lambda *args, **kwargs: []
    var_6 = python_code_.eJSL_CssBlock(selector=var_4)
    var_7 = python_code_.eJSL_KeyValuePair(
        name=(True, True, -1965.86),
        value=var_5,
        eJSL_KeyValuePair96=var_0,
        eJSL_KeyValuePair180=var_3,
        eJSL_KeyValuePair188=var_6,
    )
    assert isinstance(var_7, python_code_.eJSL_KeyValuePair)
    var_8 = {var_7}
    var_9 = python_code_.eJSL_Language(
        sys="eJSL_CssBlock187,UNPUBLISH", name=var_4, eJSL_Language179=var_8
    )
    assert isinstance(var_9, python_code_.eJSL_Language)
    var_10 = {var_9, var_9, var_9}
    var_11 = python_code_.eJSL_Extension(
        name=var_4, eJSL_Extension112=var_2, eJSL_Extension114=var_10
    )
    python_code_.eJSL_Manifestation(
        creationdate=var_0,
        copyright=var_3,
        license=["", -1289, 1200.59],
        link=var_0,
        version=var_4,
        description=var_4,
        eJSL_Manifestation=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_4 = "'`~\\FGYesc,\t"
    var_5 = lambda *args, **kwargs: True
    python_code_.eJSL_Manifestation(
        creationdate=var_4,
        copyright=complex(1497.9812, -2397.2918207),
        license=[-1485.85, False, False],
        link={},
        version=var_5,
        description=var_5,
        eJSL_Manifestation177=var_5,
    )


def test_12():
    var_0 = python_code_.eJSL_ExtensionPackage()
    var_3 = python_code_.eJSL_DatatypeReference()
    var_4 = "na:Ay5>oipMk\x0c["
    var_5 = lambda *args, **kwargs: []
    var_6 = python_code_.eJSL_CssBlock(selector=var_4)
    var_7 = python_code_.eJSL_KeyValuePair(
        name=(True, True, -1965.86),
        value=var_5,
        eJSL_KeyValuePair96=var_0,
        eJSL_KeyValuePair180=var_3,
        eJSL_KeyValuePair188=var_6,
    )
    assert isinstance(var_7, python_code_.eJSL_KeyValuePair)
    python_code_.eJSL_ParameterGroup(name=None, label=True)
    var_23 = "eJSL_DynamicPage82,eJSL_Attribute80"
    var_24 = python_code_.eJSL_Type
    var_25 = "{(z^#_KrTG-\\Pg"
    python_code_.eJSL_Manifestation(
        creationdate=True,
        copyright=var_23,
        license=var_24,
        link=var_25,
        version=var_25,
        description=var_4,
        eJSL_Manifestation=(True,),
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_1 = python_code_.eJSL_Link()
    var_3 = python_code_.eJSL_InternalLink
    var_4 = True
    var_5 = True
    python_code_.eJSL_Attribute(
        name=var_1,
        preserve=var_5,
        isunique=None,
        id=b"\n\x9b\xee\xb5O\xde",
        isprimary=var_3,
        eJSL_Attribute51=var_3,
        eJSL_Attribute80=-2167,
    )
    var_7 = "_eJSL_Page__eJSL_Page126 eJSL_Attribute80 _eJSL_InternalLink__eJSL_InternalLink _eJSL_Manifestation__eJSL_Manifestation"
    var_8 = python_code_.eJSL_LinkParameter(
        name="_eJSL_Parameter__eJSL_Parameter29:eJSL_Type:Datetime",
        id=var_7,
        value=var_1,
        eJSL_LinkParameter=-4112.91,
    )
    var_9 = python_code_.eJSL_Type()
    python_code_.eJSL_Attribute(
        name=var_7,
        preserve=var_5,
        isunique=var_3,
        id=var_4,
        isprimary=-1418.98,
        eJSL_Attribute110=var_8,
        eJSL_Attribute50=var_9,
    )


def test_14():
    var_0 = python_code_.eJSL_DetailsPage
    var_1 = "1r,12"
    python_code_.eJSL_Author(name=None, authoremail=var_0, authorurl=var_1)
    var_3 = python_code_.eJSL_ExternalLink(
        target=b'\xf0\x90\x03 \x0e\x8dbV"\xa75~\xa8\xf5\x9a\x8a\x9c', label=var_0
    )
    assert isinstance(var_3, python_code_.eJSL_ExternalLink)
    var_4 = python_code_.eJSL_Template()
    python_code_.eJSL_CssBlock(selector=True, eJSL_CssBlock=var_4)
    var_6 = python_code_.eJSL_ContextLink()
    python_code_.eJSL_LinkParameter(
        name=var_0,
        id="eJSL_Position182,Datetime,backendDAO,eJSL_KeyValuePair26",
        value=(2247.54,),
        eJSL_LinkParameter=var_6,
    )


def test_15():
    var_6 = "eJSL_Parameter68_eJSL_Entity__eJSL_Entity"
    var_7 = python_code_.eJSL_Plugin(type=var_6)
    assert isinstance(var_7, python_code_.eJSL_Plugin)


def test_16():
    var_0 = python_code_.PageActionKind
    python_code_.eJSL_Extension(name=(), eJSL_Extension114=var_0)
    var_2 = False
    var_3 = "X2RoZ"
    var_4 = python_code_.eJSL_Plugin(type=var_3, eJSL_Plugin137=var_3)
    assert isinstance(var_4, python_code_.eJSL_Plugin)
    python_code_.eJSL_Entity(
        name=var_0, preserve=var_2, eJSL_Entity135=var_4, eJSL_Entity48=var_0
    )
    python_code_.eJSL_Author(name=var_2, authoremail=var_0, authorurl=" {!H0e1 t7f\r8%")
    var_8 = python_code_.eJSL_StaticPage(preserve=var_2, HTMLBody=["XJ"])
    assert isinstance(var_8, python_code_.eJSL_StaticPage)


def test_17():
    var_0 = python_code_.eJSL_ExtensionPackage()
    var_4 = "bRc/KEo/G"
    python_code_.eJSL_EJSLModel(name=var_4)
    var_6 = python_code_.StandardTypeKinds.Text
    var_7 = python_code_.Section()
    var_35 = python_code_.eJSL_Manifestation
    var_36 = python_code_.eJSL_StaticPage(preserve=var_35, HTMLBody=None)
    assert isinstance(var_36, python_code_.eJSL_StaticPage)
    var_38 = python_code_.DynamicPage()
    python_code_.eJSL_LinkParameter(
        name=var_0, id=var_7, value=var_4, eJSL_LinkParameter=-523.97
    )
    var_40 = True
    var_41 = python_code_.eJSL_StaticPage(preserve=var_40, HTMLBody=var_38)
    var_42 = python_code_.Extension()
    var_44 = python_code_.eJSL_PositionParameter(
        name=-3145.15, divid=var_4, type=var_4, eJSL_PositionParameter=None
    )
    assert isinstance(var_44, python_code_.eJSL_PositionParameter)
    var_45 = python_code_.eJSL_KeyValuePair(
        name=var_4, value=var_4, eJSL_KeyValuePair=var_42, eJSL_KeyValuePair185=var_44
    )
    assert isinstance(var_45, python_code_.eJSL_KeyValuePair)
    var_46 = python_code_.eJSL_Type()
    var_48 = python_code_.eJSL_Entity(
        name=True,
        preserve=var_6,
        eJSL_Entity=set(),
        eJSL_Entity44={"3/D\x0b\taeLi": 708, "!Lfd9 6wg": False},
        eJSL_Entity42=var_46,
        eJSL_Entity59={-1195},
        eJSL_Entity159=var_35,
    )
    var_49 = {var_48}
    var_50 = python_code_.eJSL_DynamicPage(preserve=var_35, eJSL_DynamicPage=var_49)
    assert isinstance(var_50, python_code_.eJSL_DynamicPage)
    python_code_.eJSL_ComponentReference(core=var_4)
    var_59 = "_eJSL_Extension__eJSL_Extension116"
    var_60 = python_code_.eJSL_Position(name=var_4)
    var_61 = python_code_.eJSL_PositionParameter(
        name=var_4, divid=var_59, type=var_41, eJSL_PositionParameter=var_60
    )
    assert isinstance(var_61, python_code_.eJSL_PositionParameter)


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = python_code_.SimpleHTMLTypeKinds.Integer
    var_1 = "Alq1\t"
    python_code_.eJSL_Datatype(name=var_0, type=var_1)
    var_6 = "_eJSL_Parameter__eJSL_Parameter29"
    var_7 = python_code_.eJSL_PageReference(
        sect=["Vlhq!xO\x0bnm|sYUa`1", False, True], eJSL_PageReference=[]
    )
    python_code_.eJSL_Page(
        name=var_6,
        eJSL_Page67=var_6,
        eJSL_Page70={},
        eJSL_Page126=var_7,
        eJSL_Page73=None,
    )


def test_19():
    var_4 = "bRc/KEo/G"
    python_code_.eJSL_EJSLModel(name=var_4)
    var_41 = "na:Ay5>oipMk\x0c["
    python_code_.eJSL_CssBlock(selector=var_41)


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = python_code_.HTMLTypes()
    var_1 = "@<pH`g"
    var_2 = 'G=^\x0bMNS"*M(x!|ntfJ['
    var_3 = python_code_.eJSL_PageReference
    python_code_.eJSL_Parameter(
        name=var_1,
        defaultvalue=var_2,
        label=complex(-904.896155, 510.22),
        size=var_0,
        descripton=var_0,
        eJSL_Parameter23=var_3,
        eJSL_Parameter171="eJSL_Type eJSL_Entity159",
    )


def test_21():
    var_0 = python_code_.eJSL_ExtensionPackage()
    var_3 = python_code_.eJSL_DatatypeReference()
    var_4 = "na:Ay5>oipMk\x0c["
    var_5 = lambda *args, **kwargs: []
    var_6 = python_code_.eJSL_CssBlock(selector=var_4)
    var_7 = python_code_.eJSL_KeyValuePair(
        name=(True, True, -1965.86),
        value=var_5,
        eJSL_KeyValuePair96=var_0,
        eJSL_KeyValuePair180=var_3,
        eJSL_KeyValuePair188=var_6,
    )
    assert isinstance(var_7, python_code_.eJSL_KeyValuePair)
    var_8 = {var_7}
    var_9 = python_code_.eJSL_Language(
        sys="eJSL_CssBlock187,UNPUBLISH", name=var_4, eJSL_Language179=var_8
    )
    assert isinstance(var_9, python_code_.eJSL_Language)
    var_17 = ""
    var_18 = python_code_.eJSL_EJSLPart()
    python_code_.eJSL_Datatype(
        name=var_17,
        type=-276,
        eJSL_Datatype=var_18,
        eJSL_Datatype19=var_18,
        eJSL_Datatype41=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = python_code_.eJSL_Library()
    var_7 = '\tq+aq-"QvJZUp7#/Stp'
    var_8 = True
    python_code_.eJSL_LinkParameter(
        name=var_7,
        id=var_8,
        value=var_7,
        eJSL_LinkParameter109=[2200, -1534.23, "8rBvaa[^,sgFNI?E"],
    )
    var_10 = python_code_.eJSL_Component()
    var_14 = python_code_.eJSL_SimpleHTMLTypes(htmltype=var_7)
    assert isinstance(var_14, python_code_.eJSL_SimpleHTMLTypes)
    var_16 = python_code_.eJSL_PageReference(sect=var_0)
    python_code_.eJSL_ComponentReference(
        core=[], eJSL_ComponentReference130=var_10, eJSL_ComponentReference=var_16
    )


def test_23():
    var_1 = "Alq1\t"
    var_10 = python_code_.eJSL_Module
    var_11 = python_code_.eJSL_StaticPage(
        preserve=var_10, HTMLBody={"/PM9nsfU9oVO": -1, "": 0}
    )
    assert isinstance(var_11, python_code_.eJSL_StaticPage)
    var_16 = python_code_.eJSL_Method(
        name=-464, returnvalue=False, eJSL_Method166=set()
    )
    assert isinstance(var_16, python_code_.eJSL_Method)
    python_code_.eJSL_ParameterGroup(name=None, label=-3074, eJSL_ParameterGroup31=None)
    var_19 = True
    python_code_.eJSL_Reference(lower=var_16, upper=var_10, preserve=var_19, id=var_19)
    var_23 = "SAVE_CLOSEImage_eJSL_Entitypackage__eJSL_Entitypackage37"
    python_code_.eJSL_KeyValuePair(name=var_23, value=(), eJSL_KeyValuePair=var_10)
    var_35 = "eJSL_DynamicPage82,eJSL_Attribute80"
    var_36 = python_code_.eJSL_Type
    var_37 = "{(z^#_KrTG-\\Pg"
    python_code_.eJSL_Manifestation(
        creationdate=True,
        copyright=var_35,
        license=var_36,
        link=var_37,
        version=var_37,
        description=var_1,
        eJSL_Manifestation=(True,),
    )


def test_24():
    var_5 = python_code_.PluginKinds.editors
    var_6 = "eJSL_Parameter68_eJSL_Entity__eJSL_Entity"
    var_7 = python_code_.eJSL_Plugin(type=var_6)
    assert isinstance(var_7, python_code_.eJSL_Plugin)
    var_8 = python_code_.eJSL_ComplexHTMLTypes(htmltype=var_6)
    assert isinstance(var_8, python_code_.eJSL_ComplexHTMLTypes)
    var_10 = '"e>2\ruRD\nk{['
    var_11 = python_code_.eJSL_Method(
        name=var_10, returnvalue=var_10, eJSL_Method163=var_5
    )
    assert isinstance(var_11, python_code_.eJSL_Method)


def test_25():
    var_6 = "eJSL_Parameter68_eJSL_Entity__eJSL_Entity"
    var_7 = python_code_.eJSL_Plugin(type=var_6)
    assert isinstance(var_7, python_code_.eJSL_Plugin)
    var_8 = python_code_.eJSL_ComplexHTMLTypes(htmltype=var_6)
    assert isinstance(var_8, python_code_.eJSL_ComplexHTMLTypes)
    var_12 = python_code_.eJSL_Method(name=var_6, returnvalue=var_6)
    assert isinstance(var_12, python_code_.eJSL_Method)
    python_code_.eJSL_ParameterGroup(name=var_6, label=complex(-660.0, 5162.705567))


@pytest.mark.xfail(strict=True)
def test_26():
    var_0 = python_code_.eJSL_Type()
    var_1 = python_code_.eJSL_IndexPage()
    var_4 = "'`~\\FGYesc,\t"
    var_5 = lambda *args, **kwargs: True
    python_code_.eJSL_Manifestation(
        creationdate=var_4,
        copyright=var_4,
        license="_eJSL_Attribute__eJSL_Attribute50 eJSL_Entity _eJSL_MethodParameter__eJSL_MethodParameter eJSL_Entitypackage37",
        link="79",
        version=var_4,
        description=var_4,
        eJSL_Manifestation=None,
    )
    python_code_.eJSL_KeyValuePair(
        name=["$uiCStJR+", 548.35, True],
        value=var_4,
        eJSL_KeyValuePair93=var_0,
        eJSL_KeyValuePair188=[],
    )
    var_8 = python_code_.eJSL_PageReference(sect=var_5, eJSL_PageReference133=var_1)
    python_code_.eJSL_Page(name=None, eJSL_Page126=var_8, eJSL_Page75=782.07)


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = True
    var_1 = python_code_.DataAccessKinds
    var_2 = python_code_.eJSL_LinkParameter(
        name=None, id=var_0, value=var_0, eJSL_LinkParameter=var_1
    )
    var_3 = False
    var_4 = "\n`|'\"x,xCN\x0bu\x0bUEQ"
    var_5 = python_code_.eJSL_Attribute(
        name=var_4,
        preserve=var_3,
        isunique=var_1,
        id=var_3,
        isprimary=True,
        eJSL_Attribute83=var_3,
    )
    var_6 = {var_5}
    python_code_.eJSL_Reference(
        lower=-1417,
        upper=2678.38,
        preserve=var_3,
        id=var_1,
        eJSL_Reference55=var_6,
        eJSL_Reference61=var_1,
    )
    var_8 = python_code_.eJSL_PageReference(sect=var_4)
    var_10 = python_code_.eJSL_Method(name=var_8, returnvalue=var_2)
    assert isinstance(var_10, python_code_.eJSL_Method)
    var_11 = python_code_.InternalLink()
    python_code_.eJSL_Entitypackage(
        name={},
        eJSL_Entitypackage={-2439.64},
        eJSL_Entitypackage40=b'\xa4\x93S"\xa1\x85\xf6\xc8t8\xeb\xfc\xbe\xc3\xde\x1cL\xa5u',
    )
    var_15 = python_code_.eJSL_Feature()
    python_code_.eJSL_ParameterGroup(name=var_4, label=var_5)
    var_20 = "_eJSL_LinkParameter__eJSL_LinkParameter109"
    var_21 = python_code_.eJSL_ComponentReference(core=var_20)
    var_22 = python_code_.eJSL_Page(name=var_3, eJSL_Page=var_15, eJSL_Page75=var_6)
    var_23 = python_code_.eJSL_PageAction(
        name=var_20, pageActionType=var_4, pageActionPosition=var_3
    )
    var_24 = bool
    var_25 = python_code_.eJSL_ComplexHTMLTypes(htmltype=var_24)
    assert isinstance(var_25, python_code_.eJSL_ComplexHTMLTypes)
    var_29 = "eJSL_KeyValuePair180.extensions.eJSL_Attribute62.eJSL_Package147"
    python_code_.eJSL_Author(
        name=var_4, authoremail=var_4, authorurl=var_29, eJSL_Author=()
    )
    var_33 = python_code_.eJSL_DetailPageField
    python_code_.eJSL_Parameter(
        name=var_1,
        defaultvalue=var_20,
        label=var_21,
        size=var_21,
        descripton=var_33,
        eJSL_Parameter68=var_22,
    )
    var_36 = False
    python_code_.eJSL_LinkParameter(
        name=var_23, id=var_36, value=var_3, eJSL_LinkParameter109=var_15
    )
    python_code_.eJSL_Method(name=var_29, returnvalue=[], eJSL_Method163=var_1)
    python_code_.eJSL_Extension(name=var_1, eJSL_Extension114=var_11)
