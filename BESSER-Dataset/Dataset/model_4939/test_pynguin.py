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
    Align,
    BlockLevelComponent,
    ButtonType,
    ClassifiableComponent,
    DateFormat,
    Enum,
    EventComponent,
    EventType,
    Extension,
    FieldSetLegendAlign,
    FormControl,
    FormControlConstraint,
    HeadingLevel,
    IdentifiableComponent,
    InlineComponent,
    List,
    Locale,
    LogicalOperator,
    MatchingOperator,
    MessageDialogEvent,
    ObjectAlign,
    ObjectComponent,
    OrderedListType,
    Orientation,
    PhraseElementType,
    RichWidget,
    ScriptType,
    SubmitFormMethod,
    TextField,
    UnorderedListType,
    abstractmethod,
    date,
    datetime,
    ric_AccordionPanel,
    ric_BlockLevelComponent,
    ric_Button,
    ric_CheckGroup,
    ric_Checkbox,
    ric_ClassifiableComponent,
    ric_ContentRegion,
    ric_ContextualNavigationRegion,
    ric_Datepicker,
    ric_Div,
    ric_Document,
    ric_Event,
    ric_EventComponent,
    ric_Fieldset,
    ric_FooterRegion,
    ric_Form,
    ric_FormControl,
    ric_FormControlConstraint,
    ric_HeaderRegion,
    ric_Heading,
    ric_IdentifiableComponent,
    ric_Image,
    ric_InlineComponent,
    ric_InputFile,
    ric_Label,
    ric_LineBreak,
    ric_Link,
    ric_LinkGroup,
    ric_List,
    ric_ListItem,
    ric_Logo,
    ric_MessageDialog,
    ric_MessageDialogButton,
    ric_NavigationRegion,
    ric_NumberValueConstraint,
    ric_ObjectComponent,
    ric_OrderedList,
    ric_Paragraph,
    ric_PhraseElement,
    ric_Portal,
    ric_Radio,
    ric_RadioGroup,
    ric_RequiredFieldConstraint,
    ric_RichWidget,
    ric_Script,
    ric_SearchRegion,
    ric_Section,
    ric_Select,
    ric_SelectItem,
    ric_Span,
    ric_Tab,
    ric_TabbedPanel,
    ric_TextArea,
    ric_TextField,
    ric_UnorderedList,
    ric_ValidDateConstraint,
    ric_ValueConstraint,
    time,
)


def test_0():
    var_1 = ""
    var_2 = python_code_.ric_ClassifiableComponent(class_=var_1)
    assert isinstance(var_2, python_code_.ric_ClassifiableComponent)
    var_5 = False
    var_6 = python_code_.ric_CheckGroup(
        orientation=var_5, ric_CheckGroup=(1619, "\x0b)jWtHnv:O-R^", True)
    )
    var_7 = python_code_.ric_Checkbox(checked=var_5, ric_Checkbox=var_6)
    assert isinstance(var_7, python_code_.ric_Checkbox)
    python_code_.ric_CheckGroup(orientation=var_1)
    var_10 = "h3"
    var_11 = python_code_.ric_LinkGroup(title=var_10)
    assert isinstance(var_11, python_code_.ric_LinkGroup)
    var_12 = {var_11, var_11, var_11, var_11}
    var_13 = python_code_.ric_NavigationRegion(
        orientation=var_1, ric_NavigationRegion126=var_12
    )
    assert isinstance(var_13, python_code_.ric_NavigationRegion)


def test_1():
    var_0 = python_code_.ric_ValidDateConstraint(dateFormat=())
    assert isinstance(var_0, python_code_.ric_ValidDateConstraint)
    var_2 = "ric_Section8e0"
    python_code_.ric_MessageDialogButton(label=var_2, event=var_2)


def test_2():
    var_1 = "p\\uKe@^%i#[4t"
    var_2 = "ric_Section80"
    var_3 = python_code_.ric_MessageDialogButton(label=var_1, event=var_2)
    var_4 = python_code_.ric_AccordionPanel()
    var_5 = python_code_.ric_Section(
        title=var_3, ric_Section=var_4, ric_Section83=(1,), ric_Section92=var_2
    )
    assert isinstance(var_5, python_code_.ric_Section)


@pytest.mark.xfail(strict=True)
def test_3():
    var_2 = "ric_Section80"
    python_code_.ric_CheckGroup(orientation=var_2)
    var_6 = "_ric_Event__ric_Event:ric_Label:_ric_RadioGroup__ric_RadioGroup"
    var_7 = python_code_.ric_AccordionPanel()
    var_8 = python_code_.ric_FooterRegion()
    var_9 = python_code_.ric_ObjectComponent(
        align=[],
        width=",!}ngj/0W)TbH|}",
        height={"onkeypress": -1032.53, "sc<a'PZ)m3u": True, ":#(BcH.t\rL}^": 1376},
        border=[],
        hspace=complex(-1426.0, 1978.889),
        vspace=complex(-2569.420962, 1690.7045699),
        ric_ObjectComponent183=var_8,
    )
    assert isinstance(var_9, python_code_.ric_ObjectComponent)
    var_10 = {var_9, var_9}
    var_11 = python_code_.IdentifiableComponent
    python_code_.ric_Section(
        title=var_6,
        ric_Section=var_7,
        ric_Section86=var_10,
        ric_Section92=var_10,
        ric_Section98=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = "_ric_ObjectComponent__ric_ObjectComponent162"
    var_1 = python_code_.ric_ValueConstraint(
        matchingOperator=var_0,
        matchingValue=b"\r\x03(\xbd\xd8\xdbp>j_",
        logicalOperator=[],
    )
    assert isinstance(var_1, python_code_.ric_ValueConstraint)
    var_2 = python_code_.ric_TabbedPanel()
    var_3 = python_code_.ric_BlockLevelComponent()
    var_4 = {var_3, var_3}
    python_code_.ric_Tab(title=var_0, ric_Tab=var_2, ric_Tab61=var_4)
    var_6 = "d\r"
    var_7 = int
    var_8 = python_code_.ric_Script(name=var_7, type=var_6, implementation=var_6)
    var_10 = {var_1, var_1}
    var_11 = "<Yje+,n4]!="
    var_12 = python_code_.ric_Fieldset(
        legend=var_3, legendAlign=var_11, legendFormat=var_0
    )
    assert isinstance(var_12, python_code_.ric_Fieldset)
    python_code_.ric_FormControl(
        name=var_6,
        value=var_1,
        ric_FormControl9=var_8,
        ric_FormControl3=-375.47,
        ric_FormControl5=var_10,
        ric_FormControl7=b"s\xfaz\x00.\xfe\xf4\x08T\xe3\xe8",
        ric_FormControl27=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = -1018
    var_1 = complex
    var_2 = python_code_.ric_TextArea(
        cols={";0\tX": "yhXs\x0c\x0cJ8$C`7Bl"}, rols=var_0, readonly=var_1
    )
    assert isinstance(var_2, python_code_.ric_TextArea)
    var_4 = "ric_Label197"
    var_5 = python_code_.ric_Image(src=var_4, alt=var_4)
    assert isinstance(var_5, python_code_.ric_Image)
    var_6 = python_code_.ric_TabbedPanel()
    var_7 = python_code_.ScriptType.textJavaScript
    var_10 = python_code_.TextField()
    var_13 = "ric_FormControl3"
    var_14 = python_code_.ric_Label(text=var_6, format=var_13, ric_Label=var_7)
    assert isinstance(var_14, python_code_.ric_Label)
    var_15 = python_code_.ric_Label(text=var_4, format=-117.81, ric_Label=var_10)
    var_18 = True
    var_19 = python_code_.ric_TextField(
        charWidth=var_0, maxChars=var_1, readonly=var_18, password=var_15
    )
    assert isinstance(var_19, python_code_.ric_TextField)
    var_20 = python_code_.ric_ContentRegion()
    var_21 = 864
    var_22 = python_code_.ric_ObjectComponent(
        align=var_20,
        width=var_21,
        height=var_1,
        border=var_21,
        hspace=var_18,
        vspace={},
        ric_ObjectComponent87=-355,
        ric_ObjectComponent135=b"\xa03\xa7",
    )
    assert isinstance(var_22, python_code_.ric_ObjectComponent)
    var_23 = python_code_.ric_IdentifiableComponent(id=var_2)
    assert isinstance(var_23, python_code_.ric_IdentifiableComponent)
    python_code_.ric_Div(align=var_1, ric_Div40=var_1)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.ric_Paragraph(align=-847)
    assert isinstance(var_0, python_code_.ric_Paragraph)
    var_1 = "3A*p7j\x0b#}QK1;"
    var_2 = True
    var_3 = python_code_.ric_Checkbox(
        checked=var_2, ric_Checkbox=complex(1762.659818, 2266.46)
    )
    assert isinstance(var_3, python_code_.ric_Checkbox)
    var_4 = {var_3, var_3, var_3, var_3, var_3}
    var_5 = python_code_.ric_CheckGroup(orientation=var_1, ric_CheckGroup199=var_4)
    assert isinstance(var_5, python_code_.ric_CheckGroup)
    var_6 = python_code_.ric_Checkbox(checked=var_0, ric_Checkbox=var_5)
    var_7 = {var_3, var_6}
    var_8 = python_code_.ric_Label(text=var_3, format=var_4, ric_Label=var_3)
    assert isinstance(var_8, python_code_.ric_Label)
    python_code_.ric_CheckGroup(
        orientation=b'__\xb7\xdf\xbf"%\xa53\x8b \xa7',
        ric_CheckGroup=var_0,
        ric_CheckGroup199=var_7,
        ric_CheckGroup201=var_8,
    )


def test_7():
    var_1 = ""
    var_2 = python_code_.ric_ClassifiableComponent(class_=var_1)
    assert isinstance(var_2, python_code_.ric_ClassifiableComponent)
    var_21 = False
    var_22 = python_code_.ric_CheckGroup(
        orientation=var_21, ric_CheckGroup=(1619, "\x0b)jWtHnv:O-R^", True)
    )
    var_23 = python_code_.ric_Checkbox(checked=var_21, ric_Checkbox=var_22)
    assert isinstance(var_23, python_code_.ric_Checkbox)
    python_code_.ric_CheckGroup(orientation=var_1)
    var_26 = "h3"
    var_27 = python_code_.ric_LinkGroup(title=var_26)
    assert isinstance(var_27, python_code_.ric_LinkGroup)
    var_28 = {var_27, var_27, var_27}
    var_29 = python_code_.ric_NavigationRegion(
        orientation="[r MX\ne;", ric_NavigationRegion126=set()
    )
    assert isinstance(var_29, python_code_.ric_NavigationRegion)
    var_33 = int
    var_34 = python_code_.ric_ListItem(
        text="\n?l_g&'H<&Gu|\x0c", format=var_26, ric_ListItem=var_33
    )
    assert isinstance(var_34, python_code_.ric_ListItem)
    var_35 = "ric_Div"
    var_36 = python_code_.ric_FormControl(name=var_28, value=var_35)
    assert isinstance(var_36, python_code_.ric_FormControl)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = python_code_.FormControlConstraint()
    var_1 = -4585
    var_2 = False
    var_3 = python_code_.ric_InputFile(charWidth=var_0, maxChars=var_1, readonly=var_2)
    assert isinstance(var_3, python_code_.ric_InputFile)
    var_7 = python_code_.ric_BlockLevelComponent()
    var_8 = python_code_.ric_ContextualNavigationRegion()
    python_code_.ric_InlineComponent(
        text=b"\xde\xe2P\xb6|\xf4E\xc4\x04\x10\x1a\x00\xee",
        ric_InlineComponent50=var_7,
        ric_InlineComponent51=-2542,
        ric_InlineComponent129=var_8,
    )


def test_9():
    var_0 = python_code_.ric_Paragraph(align=-847)
    assert isinstance(var_0, python_code_.ric_Paragraph)
    var_20 = python_code_.ric_ValidDateConstraint(dateFormat="uH1KK8")
    assert isinstance(var_20, python_code_.ric_ValidDateConstraint)
    var_24 = python_code_.ric_Checkbox(checked=False)
    assert isinstance(var_24, python_code_.ric_Checkbox)


@pytest.mark.xfail(strict=True)
def test_10():
    var_2 = "h3"
    var_3 = python_code_.ric_PhraseElement(
        phraseType=var_2,
        title={"*OKJ13F4k\t9\\o": -2065.72, "McgipQTVe:`vPlB/M+G": 2314.91},
    )
    assert isinstance(var_3, python_code_.ric_PhraseElement)
    var_4 = python_code_.ric_Paragraph(align=[True, -3148])
    assert isinstance(var_4, python_code_.ric_Paragraph)
    var_5 = python_code_.ric_ValidDateConstraint(dateFormat="uH1KK8")
    assert isinstance(var_5, python_code_.ric_ValidDateConstraint)
    python_code_.ric_FormControl(
        name=var_4, value=var_2, ric_FormControl9=var_3, ric_FormControl11=var_5
    )


def test_11():
    var_2 = "LessOrEqualsThan"
    var_3 = python_code_.ric_ClassifiableComponent(class_=var_2)
    assert isinstance(var_3, python_code_.ric_ClassifiableComponent)
    var_4 = lambda *args, **kwargs: []
    var_5 = "[o,bLB(U9w)`Ii"
    var_6 = "h1-absoluteBottom"
    var_7 = python_code_.ric_FormControl(name=var_6, value=var_4)
    assert isinstance(var_7, python_code_.ric_FormControl)
    var_8 = python_code_.ric_ValueConstraint(
        matchingOperator=var_4,
        matchingValue=var_5,
        logicalOperator=var_4,
        ric_ValueConstraint=var_7,
    )
    assert isinstance(var_8, python_code_.ric_ValueConstraint)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = lambda *args, **kwargs: 6205
    python_code_.ric_Label(
        text="ric_Form", format=complex(-745.56, 3299.2524), ric_Label23=var_0
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = python_code_.ric_FooterRegion()
    var_2 = "Submit.ric_InlineComponent81.ric_RadioGroup196"
    var_52 = "`"
    var_53 = python_code_.ric_FormControl(
        name=var_52, value=var_52, ric_FormControl=var_2, ric_FormControl27=var_2
    )
    assert isinstance(var_53, python_code_.ric_FormControl)
    var_54 = python_code_.ric_RadioGroup(
        orientation=var_52, ric_RadioGroup=var_0, ric_RadioGroup196=-3015
    )
    var_55 = python_code_.LogicalOperator
    var_56 = python_code_.ric_CheckGroup(orientation=var_55, ric_CheckGroup=var_55)
    python_code_.ric_Label(
        text=var_2,
        format=b"\x0b\xd7\x1a8\xe3\x83\xa4\xe8 \x13\x12\xa7G?\x80\x84",
        ric_Label=var_53,
        ric_Label197=var_54,
        ric_Label202=var_56,
    )


@pytest.mark.xfail(strict=True)
def test_14():
    var_1 = "p\\uKe@%i#[4t"
    var_6 = python_code_.ric_SearchRegion()
    var_7 = python_code_.ric_SelectItem
    python_code_.ric_Fieldset(
        legend=None,
        legendAlign=var_6,
        legendFormat=var_1,
        ric_Fieldset=-197,
        ric_Fieldset26=var_7,
        ric_Fieldset31=var_7,
    )


def test_15():
    python_code_.FieldSetLegendAlign.top


def test_16():
    var_7 = "Up(Vb`Lc->:"
    var_8 = python_code_.ric_IdentifiableComponent(id=var_7)
    assert isinstance(var_8, python_code_.ric_IdentifiableComponent)
    var_9 = python_code_.ric_HeaderRegion()
    var_12 = python_code_.List()
    var_14 = dict
    var_15 = python_code_.ric_UnorderedList(type=None)
    assert isinstance(var_15, python_code_.ric_UnorderedList)
    var_16 = "9k"
    var_17 = python_code_.ric_Paragraph(align=var_16)
    assert isinstance(var_17, python_code_.ric_Paragraph)
    var_18 = python_code_.ric_Radio(checked=var_9)
    assert isinstance(var_18, python_code_.ric_Radio)
    var_19 = python_code_.ric_NavigationRegion(orientation=None)
    assert isinstance(var_19, python_code_.ric_NavigationRegion)
    var_20 = python_code_.ric_LinkGroup(
        title=var_12, ric_LinkGroup=var_18, ric_LinkGroup208=var_9
    )
    assert isinstance(var_20, python_code_.ric_LinkGroup)
    var_25 = -3659
    var_26 = True
    var_27 = python_code_.ric_Select(size=var_25, multiple=var_26)
    assert isinstance(var_27, python_code_.ric_Select)
    var_30 = python_code_.ric_Button(type=var_12, disabled=419.05, image=var_7)
    assert isinstance(var_30, python_code_.ric_Button)
    var_33 = True
    var_34 = False
    var_35 = python_code_.ric_TextField(
        charWidth=var_26, maxChars=4.71, readonly=var_33, password=var_34
    )
    assert isinstance(var_35, python_code_.ric_TextField)
    python_code_.ric_SelectItem(
        itemLabel=var_16, value=None, selected=var_26, ric_SelectItem=var_27
    )
    var_41 = python_code_.ric_Checkbox(checked=var_14)
    assert isinstance(var_41, python_code_.ric_Checkbox)


def test_17():
    var_1 = ""
    var_2 = python_code_.ric_ClassifiableComponent(class_=var_1)
    assert isinstance(var_2, python_code_.ric_ClassifiableComponent)
    var_5 = False
    var_6 = python_code_.ric_CheckGroup(
        orientation=var_5, ric_CheckGroup=(1619, "\x0b)jWtHnv:O-R^", True)
    )
    var_7 = python_code_.ric_Checkbox(checked=var_5, ric_Checkbox=var_6)
    assert isinstance(var_7, python_code_.ric_Checkbox)
    var_8 = python_code_.ric_HeaderRegion()
    python_code_.ric_CheckGroup(orientation=var_1)
    var_10 = "h3"
    var_11 = python_code_.ric_LinkGroup(title=var_10)
    assert isinstance(var_11, python_code_.ric_LinkGroup)
    var_12 = {var_11, var_11, var_11, var_11}
    var_13 = python_code_.ric_NavigationRegion(
        orientation="[r MX\ne;", ric_NavigationRegion126=set()
    )
    assert isinstance(var_13, python_code_.ric_NavigationRegion)
    var_17 = int
    python_code_.ric_ListItem(text=var_8, format=var_17)
    var_19 = "ric_Div"
    var_20 = python_code_.ric_FormControl(name=var_12, value=var_19)
    assert isinstance(var_20, python_code_.ric_FormControl)


def test_18():
    var_2 = "Submit.ric_InlineComponent8.ric_RadioGroup196"
    var_3 = python_code_.ric_CheckGroup(orientation=var_2)
    var_5 = "Up(Vb`Lc->:"
    var_6 = python_code_.ric_IdentifiableComponent(id=var_5)
    assert isinstance(var_6, python_code_.ric_IdentifiableComponent)
    var_7 = python_code_.ric_HeaderRegion()
    var_10 = python_code_.List()
    var_12 = dict
    var_13 = python_code_.ric_ValueConstraint(
        matchingOperator=var_3,
        matchingValue=var_12,
        logicalOperator="_ric_ValueConstraint__ric_ValueConstraint",
    )
    assert isinstance(var_13, python_code_.ric_ValueConstraint)
    python_code_.ric_ListItem(text=None, format=var_3)
    var_15 = python_code_.ric_UnorderedList(type=None)
    assert isinstance(var_15, python_code_.ric_UnorderedList)
    var_16 = "9k"
    var_17 = python_code_.ric_Paragraph(align=var_16)
    assert isinstance(var_17, python_code_.ric_Paragraph)
    var_18 = python_code_.ric_Radio(checked=var_7)
    assert isinstance(var_18, python_code_.ric_Radio)
    var_20 = python_code_.ric_NavigationRegion(orientation=None)
    assert isinstance(var_20, python_code_.ric_NavigationRegion)
    var_21 = python_code_.ric_LinkGroup(
        title=var_10, ric_LinkGroup=var_18, ric_LinkGroup208=var_7
    )
    assert isinstance(var_21, python_code_.ric_LinkGroup)
    var_27 = 850
    var_28 = True
    var_29 = python_code_.ric_Select(size=var_27, multiple=var_28)
    assert isinstance(var_29, python_code_.ric_Select)
    var_32 = python_code_.ric_Button(type=var_10, disabled=419.05, image=var_5)
    assert isinstance(var_32, python_code_.ric_Button)
    var_35 = True
    var_36 = False
    var_37 = python_code_.ric_TextField(
        charWidth=var_28, maxChars=4.71, readonly=var_35, password=var_36
    )
    assert isinstance(var_37, python_code_.ric_TextField)
    python_code_.ric_SelectItem(
        itemLabel=var_2, value=None, selected=var_28, ric_SelectItem=var_29
    )
    var_43 = python_code_.ric_Checkbox(checked=var_12)
    assert isinstance(var_43, python_code_.ric_Checkbox)
    python_code_.ric_SelectItem(itemLabel={}, value=var_3, selected=var_36)
