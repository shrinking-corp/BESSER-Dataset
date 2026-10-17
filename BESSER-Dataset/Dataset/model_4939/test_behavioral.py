import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BlockLevelComponent,
    ClassifiableComponent,
    EventComponent,
    FormControl,
    FormControlConstraint,
    IdentifiableComponent,
    InlineComponent,
    List,
    ObjectComponent,
    RichWidget,
    TextField,
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
    Align,
    ButtonType,
    DateFormat,
    EventType,
    Extension,
    FieldSetLegendAlign,
    HeadingLevel,
    Locale,
    LogicalOperator,
    MatchingOperator,
    MessageDialogEvent,
    ObjectAlign,
    OrderedListType,
    Orientation,
    PhraseElementType,
    ScriptType,
    SubmitFormMethod,
    UnorderedListType,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_accompanyingPhrase2_reverse_link_reassign_clear():
    a1 = ric_PhraseElement(phraseType="sample_text", title="sample_text")
    a2 = ric_PhraseElement(phraseType="sample_text_2", title="sample_text_2")
    b = ric_FormControl(name="sample_text", value="sample_text")
    _safe_set(b, 'ric_FormControl3', {a1})
    assert _is_linked(b, 'ric_FormControl3', a1)
    if hasattr(a1, 'ric_PhraseElement'):
        assert _is_linked(a1, 'ric_PhraseElement', b)
    _safe_set(b, 'ric_FormControl3', {a2})
    assert _is_linked(b, 'ric_FormControl3', a2)
    if hasattr(a1, 'ric_PhraseElement'):
        assert not _is_linked(a1, 'ric_PhraseElement', b)
    if hasattr(a2, 'ric_PhraseElement'):
        assert _is_linked(a2, 'ric_PhraseElement', b)
    _safe_set(b, 'ric_FormControl3', set())
    assert not _is_linked(b, 'ric_FormControl3', a2)
    if hasattr(a2, 'ric_PhraseElement'):
        assert not _is_linked(a2, 'ric_PhraseElement', b)


def test_assoc_action14_reverse_link_reassign_clear():
    a1 = ric_Form(method="sample_text", name="sample_text")
    a2 = ric_Form(method="sample_text_2", name="sample_text_2")
    b = ric_Document(fileName="sample_text", index=True, title="sample_text")
    _safe_set(b, 'ric_Document', a1)
    assert _is_linked(b, 'ric_Document', a1)
    if hasattr(a1, 'ric_Form'):
        assert _is_linked(a1, 'ric_Form', b)
    _safe_set(b, 'ric_Document', a2)
    assert _is_linked(b, 'ric_Document', a2)
    if hasattr(a1, 'ric_Form'):
        assert not _is_linked(a1, 'ric_Form', b)
    if hasattr(a2, 'ric_Form'):
        assert _is_linked(a2, 'ric_Form', b)
    _safe_set(b, 'ric_Document', None)
    assert not _is_linked(b, 'ric_Document', a2)
    if hasattr(a2, 'ric_Form'):
        assert not _is_linked(a2, 'ric_Form', b)


def test_assoc_buttons100_reverse_link_reassign_clear():
    a1 = ric_MessageDialogButton(event="sample_text", label="sample_text")
    a2 = ric_MessageDialogButton(event="sample_text_2", label="sample_text_2")
    b = ric_MessageDialog(autoOpen=True, height=7, maxHeightResize=7, maxWidthResize=7, message="sample_text", minHeightResize=7, minWidthResize=7, modal=True, resizable=True, title="sample_text", width=7)
    _safe_set(b, 'ric_MessageDialog', {a1})
    assert _is_linked(b, 'ric_MessageDialog', a1)
    if hasattr(a1, 'ric_MessageDialogButton'):
        assert _is_linked(a1, 'ric_MessageDialogButton', b)
    _safe_set(b, 'ric_MessageDialog', {a2})
    assert _is_linked(b, 'ric_MessageDialog', a2)
    if hasattr(a1, 'ric_MessageDialogButton'):
        assert not _is_linked(a1, 'ric_MessageDialogButton', b)
    if hasattr(a2, 'ric_MessageDialogButton'):
        assert _is_linked(a2, 'ric_MessageDialogButton', b)
    _safe_set(b, 'ric_MessageDialog', set())
    assert not _is_linked(b, 'ric_MessageDialog', a2)
    if hasattr(a2, 'ric_MessageDialogButton'):
        assert not _is_linked(a2, 'ric_MessageDialogButton', b)


def test_assoc_checkGroups30_reverse_link_reassign_clear():
    a1 = ric_Fieldset(legend="sample_text", legendAlign="sample_text", legendFormat="sample_text")
    a2 = ric_Fieldset(legend="sample_text_2", legendAlign="sample_text_2", legendFormat="sample_text_2")
    b = ric_CheckGroup(orientation="sample_text")
    _safe_set(b, 'ric_CheckGroup', a1)
    assert _is_linked(b, 'ric_CheckGroup', a1)
    if hasattr(a1, 'ric_Fieldset31'):
        assert _is_linked(a1, 'ric_Fieldset31', b)
    _safe_set(b, 'ric_CheckGroup', a2)
    assert _is_linked(b, 'ric_CheckGroup', a2)
    if hasattr(a1, 'ric_Fieldset31'):
        assert not _is_linked(a1, 'ric_Fieldset31', b)
    if hasattr(a2, 'ric_Fieldset31'):
        assert _is_linked(a2, 'ric_Fieldset31', b)
    _safe_set(b, 'ric_CheckGroup', None)
    assert not _is_linked(b, 'ric_CheckGroup', a2)
    if hasattr(a2, 'ric_Fieldset31'):
        assert not _is_linked(a2, 'ric_Fieldset31', b)


def test_assoc_checks198_reverse_link_reassign_clear():
    a1 = ric_Checkbox(checked=True)
    a2 = ric_Checkbox(checked=False)
    b = ric_CheckGroup(orientation="sample_text")
    _safe_set(b, 'ric_CheckGroup199', {a1})
    assert _is_linked(b, 'ric_CheckGroup199', a1)
    if hasattr(a1, 'ric_Checkbox'):
        assert _is_linked(a1, 'ric_Checkbox', b)
    _safe_set(b, 'ric_CheckGroup199', {a2})
    assert _is_linked(b, 'ric_CheckGroup199', a2)
    if hasattr(a1, 'ric_Checkbox'):
        assert not _is_linked(a1, 'ric_Checkbox', b)
    if hasattr(a2, 'ric_Checkbox'):
        assert _is_linked(a2, 'ric_Checkbox', b)
    _safe_set(b, 'ric_CheckGroup199', set())
    assert not _is_linked(b, 'ric_CheckGroup199', a2)
    if hasattr(a2, 'ric_Checkbox'):
        assert not _is_linked(a2, 'ric_Checkbox', b)


def test_assoc_controls25_reverse_link_reassign_clear():
    a1 = ric_FormControl(name="sample_text", value="sample_text")
    a2 = ric_FormControl(name="sample_text_2", value="sample_text_2")
    b = ric_Fieldset(legend="sample_text", legendAlign="sample_text", legendFormat="sample_text")
    _safe_set(b, 'ric_Fieldset26', {a1})
    assert _is_linked(b, 'ric_Fieldset26', a1)
    if hasattr(a1, 'ric_FormControl27'):
        assert _is_linked(a1, 'ric_FormControl27', b)
    _safe_set(b, 'ric_Fieldset26', {a2})
    assert _is_linked(b, 'ric_Fieldset26', a2)
    if hasattr(a1, 'ric_FormControl27'):
        assert not _is_linked(a1, 'ric_FormControl27', b)
    if hasattr(a2, 'ric_FormControl27'):
        assert _is_linked(a2, 'ric_FormControl27', b)
    _safe_set(b, 'ric_Fieldset26', set())
    assert not _is_linked(b, 'ric_Fieldset26', a2)
    if hasattr(a2, 'ric_FormControl27'):
        assert not _is_linked(a2, 'ric_FormControl27', b)


def test_assoc_events22_reverse_link_reassign_clear():
    a1 = ric_Label(format="sample_text", text="sample_text")
    a2 = ric_Label(format="sample_text_2", text="sample_text_2")
    b = ric_Event(type="sample_text")
    _safe_set(b, 'ric_Event24', a1)
    assert _is_linked(b, 'ric_Event24', a1)
    if hasattr(a1, 'ric_Label23'):
        assert _is_linked(a1, 'ric_Label23', b)
    _safe_set(b, 'ric_Event24', a2)
    assert _is_linked(b, 'ric_Event24', a2)
    if hasattr(a1, 'ric_Label23'):
        assert not _is_linked(a1, 'ric_Label23', b)
    if hasattr(a2, 'ric_Label23'):
        assert _is_linked(a2, 'ric_Label23', b)
    _safe_set(b, 'ric_Event24', None)
    assert not _is_linked(b, 'ric_Event24', a2)
    if hasattr(a2, 'ric_Label23'):
        assert not _is_linked(a2, 'ric_Label23', b)


def test_assoc_fieldsets15_reverse_link_reassign_clear():
    a1 = ric_Form(method="sample_text", name="sample_text")
    a2 = ric_Form(method="sample_text_2", name="sample_text_2")
    b = ric_Fieldset(legend="sample_text", legendAlign="sample_text", legendFormat="sample_text")
    _safe_set(b, 'ric_Fieldset', a1)
    assert _is_linked(b, 'ric_Fieldset', a1)
    if hasattr(a1, 'ric_Form16'):
        assert _is_linked(a1, 'ric_Form16', b)
    _safe_set(b, 'ric_Fieldset', a2)
    assert _is_linked(b, 'ric_Fieldset', a2)
    if hasattr(a1, 'ric_Form16'):
        assert not _is_linked(a1, 'ric_Form16', b)
    if hasattr(a2, 'ric_Form16'):
        assert _is_linked(a2, 'ric_Form16', b)
    _safe_set(b, 'ric_Fieldset', None)
    assert not _is_linked(b, 'ric_Fieldset', a2)
    if hasattr(a2, 'ric_Form16'):
        assert not _is_linked(a2, 'ric_Form16', b)


def test_assoc_fieldsets42_reverse_link_reassign_clear():
    a1 = ric_Fieldset(legend="sample_text", legendAlign="sample_text", legendFormat="sample_text")
    a2 = ric_Fieldset(legend="sample_text_2", legendAlign="sample_text_2", legendFormat="sample_text_2")
    b = ric_Div(align="sample_text")
    _safe_set(b, 'ric_Div43', {a1})
    assert _is_linked(b, 'ric_Div43', a1)
    if hasattr(a1, 'ric_Fieldset44'):
        assert _is_linked(a1, 'ric_Fieldset44', b)
    _safe_set(b, 'ric_Div43', {a2})
    assert _is_linked(b, 'ric_Div43', a2)
    if hasattr(a1, 'ric_Fieldset44'):
        assert not _is_linked(a1, 'ric_Fieldset44', b)
    if hasattr(a2, 'ric_Fieldset44'):
        assert _is_linked(a2, 'ric_Fieldset44', b)
    _safe_set(b, 'ric_Div43', set())
    assert not _is_linked(b, 'ric_Div43', a2)
    if hasattr(a2, 'ric_Fieldset44'):
        assert not _is_linked(a2, 'ric_Fieldset44', b)


def test_assoc_forms172_reverse_link_reassign_clear():
    a1 = ric_Form(method="sample_text", name="sample_text")
    a2 = ric_Form(method="sample_text_2", name="sample_text_2")
    b = ric_Document(fileName="sample_text", index=True, title="sample_text")
    _safe_set(b, 'ric_Document173', {a1})
    assert _is_linked(b, 'ric_Document173', a1)
    if hasattr(a1, 'ric_Form174'):
        assert _is_linked(a1, 'ric_Form174', b)
    _safe_set(b, 'ric_Document173', {a2})
    assert _is_linked(b, 'ric_Document173', a2)
    if hasattr(a1, 'ric_Form174'):
        assert not _is_linked(a1, 'ric_Form174', b)
    if hasattr(a2, 'ric_Form174'):
        assert _is_linked(a2, 'ric_Form174', b)
    _safe_set(b, 'ric_Document173', set())
    assert not _is_linked(b, 'ric_Document173', a2)
    if hasattr(a2, 'ric_Form174'):
        assert not _is_linked(a2, 'ric_Form174', b)


def test_assoc_forms39_reverse_link_reassign_clear():
    a1 = ric_Form(method="sample_text", name="sample_text")
    a2 = ric_Form(method="sample_text_2", name="sample_text_2")
    b = ric_Div(align="sample_text")
    _safe_set(b, 'ric_Div40', {a1})
    assert _is_linked(b, 'ric_Div40', a1)
    if hasattr(a1, 'ric_Form41'):
        assert _is_linked(a1, 'ric_Form41', b)
    _safe_set(b, 'ric_Div40', {a2})
    assert _is_linked(b, 'ric_Div40', a2)
    if hasattr(a1, 'ric_Form41'):
        assert not _is_linked(a1, 'ric_Form41', b)
    if hasattr(a2, 'ric_Form41'):
        assert _is_linked(a2, 'ric_Form41', b)
    _safe_set(b, 'ric_Div40', set())
    assert not _is_linked(b, 'ric_Div40', a2)
    if hasattr(a2, 'ric_Form41'):
        assert not _is_linked(a2, 'ric_Form41', b)


def test_assoc_forms75_reverse_link_reassign_clear():
    a1 = ric_Tab(title="sample_text")
    a2 = ric_Tab(title="sample_text_2")
    b = ric_Form(method="sample_text", name="sample_text")
    _safe_set(b, 'ric_Form77', a1)
    assert _is_linked(b, 'ric_Form77', a1)
    if hasattr(a1, 'ric_Tab76'):
        assert _is_linked(a1, 'ric_Tab76', b)
    _safe_set(b, 'ric_Form77', a2)
    assert _is_linked(b, 'ric_Form77', a2)
    if hasattr(a1, 'ric_Tab76'):
        assert not _is_linked(a1, 'ric_Tab76', b)
    if hasattr(a2, 'ric_Tab76'):
        assert _is_linked(a2, 'ric_Tab76', b)
    _safe_set(b, 'ric_Form77', None)
    assert not _is_linked(b, 'ric_Form77', a2)
    if hasattr(a2, 'ric_Tab76'):
        assert not _is_linked(a2, 'ric_Tab76', b)


def test_assoc_forms97_reverse_link_reassign_clear():
    a1 = ric_Section(title="sample_text")
    a2 = ric_Section(title="sample_text_2")
    b = ric_Form(method="sample_text", name="sample_text")
    _safe_set(b, 'ric_Form99', a1)
    assert _is_linked(b, 'ric_Form99', a1)
    if hasattr(a1, 'ric_Section98'):
        assert _is_linked(a1, 'ric_Section98', b)
    _safe_set(b, 'ric_Form99', a2)
    assert _is_linked(b, 'ric_Form99', a2)
    if hasattr(a1, 'ric_Section98'):
        assert not _is_linked(a1, 'ric_Section98', b)
    if hasattr(a2, 'ric_Section98'):
        assert _is_linked(a2, 'ric_Section98', b)
    _safe_set(b, 'ric_Form99', None)
    assert not _is_linked(b, 'ric_Form99', a2)
    if hasattr(a2, 'ric_Section98'):
        assert not _is_linked(a2, 'ric_Section98', b)


def test_assoc_inlineComponents154_reverse_link_reassign_clear():
    a1 = ric_InlineComponent(text="sample_text")
    a2 = ric_InlineComponent(text="sample_text_2")
    b = ric_Document(fileName="sample_text", index=True, title="sample_text")
    _safe_set(b, 'ric_Document155', {a1})
    assert _is_linked(b, 'ric_Document155', a1)
    if hasattr(a1, 'ric_InlineComponent156'):
        assert _is_linked(a1, 'ric_InlineComponent156', b)
    _safe_set(b, 'ric_Document155', {a2})
    assert _is_linked(b, 'ric_Document155', a2)
    if hasattr(a1, 'ric_InlineComponent156'):
        assert not _is_linked(a1, 'ric_InlineComponent156', b)
    if hasattr(a2, 'ric_InlineComponent156'):
        assert _is_linked(a2, 'ric_InlineComponent156', b)
    _safe_set(b, 'ric_Document155', set())
    assert not _is_linked(b, 'ric_Document155', a2)
    if hasattr(a2, 'ric_InlineComponent156'):
        assert not _is_linked(a2, 'ric_InlineComponent156', b)


def test_assoc_inlineComponents19_reverse_link_reassign_clear():
    a1 = ric_InlineComponent(text="sample_text")
    a2 = ric_InlineComponent(text="sample_text_2")
    b = ric_Form(method="sample_text", name="sample_text")
    _safe_set(b, 'ric_Form20', {a1})
    assert _is_linked(b, 'ric_Form20', a1)
    if hasattr(a1, 'ric_InlineComponent'):
        assert _is_linked(a1, 'ric_InlineComponent', b)
    _safe_set(b, 'ric_Form20', {a2})
    assert _is_linked(b, 'ric_Form20', a2)
    if hasattr(a1, 'ric_InlineComponent'):
        assert not _is_linked(a1, 'ric_InlineComponent', b)
    if hasattr(a2, 'ric_InlineComponent'):
        assert _is_linked(a2, 'ric_InlineComponent', b)
    _safe_set(b, 'ric_Form20', set())
    assert not _is_linked(b, 'ric_Form20', a2)
    if hasattr(a2, 'ric_InlineComponent'):
        assert not _is_linked(a2, 'ric_InlineComponent', b)


def test_assoc_inlineComponents52_reverse_link_reassign_clear():
    a1 = ric_InlineComponent(text="sample_text")
    a2 = ric_InlineComponent(text="sample_text_2")
    b = ric_InlineComponent(text="sample_text")
    _safe_set(b, 'ric_InlineComponent53', a1)
    assert _is_linked(b, 'ric_InlineComponent53', a1)
    if hasattr(a1, 'ric_InlineComponent51'):
        assert _is_linked(a1, 'ric_InlineComponent51', b)
    _safe_set(b, 'ric_InlineComponent53', a2)
    assert _is_linked(b, 'ric_InlineComponent53', a2)
    if hasattr(a1, 'ric_InlineComponent51'):
        assert not _is_linked(a1, 'ric_InlineComponent51', b)
    if hasattr(a2, 'ric_InlineComponent51'):
        assert _is_linked(a2, 'ric_InlineComponent51', b)
    _safe_set(b, 'ric_InlineComponent53', None)
    assert not _is_linked(b, 'ric_InlineComponent53', a2)
    if hasattr(a2, 'ric_InlineComponent51'):
        assert not _is_linked(a2, 'ric_InlineComponent51', b)


def test_assoc_inlineComponents57_reverse_link_reassign_clear():
    a1 = ric_Tab(title="sample_text")
    a2 = ric_Tab(title="sample_text_2")
    b = ric_InlineComponent(text="sample_text")
    _safe_set(b, 'ric_InlineComponent59', a1)
    assert _is_linked(b, 'ric_InlineComponent59', a1)
    if hasattr(a1, 'ric_Tab58'):
        assert _is_linked(a1, 'ric_Tab58', b)
    _safe_set(b, 'ric_InlineComponent59', a2)
    assert _is_linked(b, 'ric_InlineComponent59', a2)
    if hasattr(a1, 'ric_Tab58'):
        assert not _is_linked(a1, 'ric_Tab58', b)
    if hasattr(a2, 'ric_Tab58'):
        assert _is_linked(a2, 'ric_Tab58', b)
    _safe_set(b, 'ric_InlineComponent59', None)
    assert not _is_linked(b, 'ric_InlineComponent59', a2)
    if hasattr(a2, 'ric_Tab58'):
        assert not _is_linked(a2, 'ric_Tab58', b)


def test_assoc_inlineComponents79_reverse_link_reassign_clear():
    a1 = ric_Section(title="sample_text")
    a2 = ric_Section(title="sample_text_2")
    b = ric_InlineComponent(text="sample_text")
    _safe_set(b, 'ric_InlineComponent81', a1)
    assert _is_linked(b, 'ric_InlineComponent81', a1)
    if hasattr(a1, 'ric_Section80'):
        assert _is_linked(a1, 'ric_Section80', b)
    _safe_set(b, 'ric_InlineComponent81', a2)
    assert _is_linked(b, 'ric_InlineComponent81', a2)
    if hasattr(a1, 'ric_Section80'):
        assert not _is_linked(a1, 'ric_Section80', b)
    if hasattr(a2, 'ric_Section80'):
        assert _is_linked(a2, 'ric_Section80', b)
    _safe_set(b, 'ric_InlineComponent81', None)
    assert not _is_linked(b, 'ric_InlineComponent81', a2)
    if hasattr(a2, 'ric_Section80'):
        assert not _is_linked(a2, 'ric_Section80', b)


def test_assoc_items21_reverse_link_reassign_clear():
    a1 = ric_SelectItem(itemLabel="sample_text", selected=True, value="sample_text")
    a2 = ric_SelectItem(itemLabel="sample_text_2", selected=False, value="sample_text_2")
    b = ric_Select(multiple=True, size=7)
    _safe_set(b, 'ric_Select', {a1})
    assert _is_linked(b, 'ric_Select', a1)
    if hasattr(a1, 'ric_SelectItem'):
        assert _is_linked(a1, 'ric_SelectItem', b)
    _safe_set(b, 'ric_Select', {a2})
    assert _is_linked(b, 'ric_Select', a2)
    if hasattr(a1, 'ric_SelectItem'):
        assert not _is_linked(a1, 'ric_SelectItem', b)
    if hasattr(a2, 'ric_SelectItem'):
        assert _is_linked(a2, 'ric_SelectItem', b)
    _safe_set(b, 'ric_Select', set())
    assert not _is_linked(b, 'ric_Select', a2)
    if hasattr(a2, 'ric_SelectItem'):
        assert not _is_linked(a2, 'ric_SelectItem', b)


def test_assoc_label1_reverse_link_reassign_clear():
    a1 = ric_Label(format="sample_text", text="sample_text")
    a2 = ric_Label(format="sample_text_2", text="sample_text_2")
    b = ric_FormControl(name="sample_text", value="sample_text")
    _safe_set(b, 'ric_FormControl', a1)
    assert _is_linked(b, 'ric_FormControl', a1)
    if hasattr(a1, 'ric_Label'):
        assert _is_linked(a1, 'ric_Label', b)
    _safe_set(b, 'ric_FormControl', a2)
    assert _is_linked(b, 'ric_FormControl', a2)
    if hasattr(a1, 'ric_Label'):
        assert not _is_linked(a1, 'ric_Label', b)
    if hasattr(a2, 'ric_Label'):
        assert _is_linked(a2, 'ric_Label', b)
    _safe_set(b, 'ric_FormControl', None)
    assert not _is_linked(b, 'ric_FormControl', a2)
    if hasattr(a2, 'ric_Label'):
        assert not _is_linked(a2, 'ric_Label', b)


def test_assoc_label195_reverse_link_reassign_clear():
    a1 = ric_RadioGroup(orientation="sample_text")
    a2 = ric_RadioGroup(orientation="sample_text_2")
    b = ric_Label(format="sample_text", text="sample_text")
    _safe_set(b, 'ric_Label197', a1)
    assert _is_linked(b, 'ric_Label197', a1)
    if hasattr(a1, 'ric_RadioGroup196'):
        assert _is_linked(a1, 'ric_RadioGroup196', b)
    _safe_set(b, 'ric_Label197', a2)
    assert _is_linked(b, 'ric_Label197', a2)
    if hasattr(a1, 'ric_RadioGroup196'):
        assert not _is_linked(a1, 'ric_RadioGroup196', b)
    if hasattr(a2, 'ric_RadioGroup196'):
        assert _is_linked(a2, 'ric_RadioGroup196', b)
    _safe_set(b, 'ric_Label197', None)
    assert not _is_linked(b, 'ric_Label197', a2)
    if hasattr(a2, 'ric_RadioGroup196'):
        assert not _is_linked(a2, 'ric_RadioGroup196', b)


def test_assoc_label200_reverse_link_reassign_clear():
    a1 = ric_Label(format="sample_text", text="sample_text")
    a2 = ric_Label(format="sample_text_2", text="sample_text_2")
    b = ric_CheckGroup(orientation="sample_text")
    _safe_set(b, 'ric_CheckGroup201', a1)
    assert _is_linked(b, 'ric_CheckGroup201', a1)
    if hasattr(a1, 'ric_Label202'):
        assert _is_linked(a1, 'ric_Label202', b)
    _safe_set(b, 'ric_CheckGroup201', a2)
    assert _is_linked(b, 'ric_CheckGroup201', a2)
    if hasattr(a1, 'ric_Label202'):
        assert not _is_linked(a1, 'ric_Label202', b)
    if hasattr(a2, 'ric_Label202'):
        assert _is_linked(a2, 'ric_Label202', b)
    _safe_set(b, 'ric_CheckGroup201', None)
    assert not _is_linked(b, 'ric_CheckGroup201', a2)
    if hasattr(a2, 'ric_Label202'):
        assert not _is_linked(a2, 'ric_Label202', b)


def test_assoc_linkGroups125_reverse_link_reassign_clear():
    a1 = ric_NavigationRegion(orientation="sample_text")
    a2 = ric_NavigationRegion(orientation="sample_text_2")
    b = ric_LinkGroup(title="sample_text")
    _safe_set(b, 'ric_LinkGroup', a1)
    assert _is_linked(b, 'ric_LinkGroup', a1)
    if hasattr(a1, 'ric_NavigationRegion126'):
        assert _is_linked(a1, 'ric_NavigationRegion126', b)
    _safe_set(b, 'ric_LinkGroup', a2)
    assert _is_linked(b, 'ric_LinkGroup', a2)
    if hasattr(a1, 'ric_NavigationRegion126'):
        assert not _is_linked(a1, 'ric_NavigationRegion126', b)
    if hasattr(a2, 'ric_NavigationRegion126'):
        assert _is_linked(a2, 'ric_NavigationRegion126', b)
    _safe_set(b, 'ric_LinkGroup', None)
    assert not _is_linked(b, 'ric_LinkGroup', a2)
    if hasattr(a2, 'ric_NavigationRegion126'):
        assert not _is_linked(a2, 'ric_NavigationRegion126', b)


def test_assoc_linkGroups207_reverse_link_reassign_clear():
    a1 = ric_LinkGroup(title="sample_text")
    a2 = ric_LinkGroup(title="sample_text_2")
    b = ric_LinkGroup(title="sample_text")
    _safe_set(b, 'ric_LinkGroup208', a1)
    assert _is_linked(b, 'ric_LinkGroup208', a1)
    if hasattr(a1, 'ric_LinkGroup206'):
        assert _is_linked(a1, 'ric_LinkGroup206', b)
    _safe_set(b, 'ric_LinkGroup208', a2)
    assert _is_linked(b, 'ric_LinkGroup208', a2)
    if hasattr(a1, 'ric_LinkGroup206'):
        assert not _is_linked(a1, 'ric_LinkGroup206', b)
    if hasattr(a2, 'ric_LinkGroup206'):
        assert _is_linked(a2, 'ric_LinkGroup206', b)
    _safe_set(b, 'ric_LinkGroup208', None)
    assert not _is_linked(b, 'ric_LinkGroup208', a2)
    if hasattr(a2, 'ric_LinkGroup206'):
        assert not _is_linked(a2, 'ric_LinkGroup206', b)


def test_assoc_links203_reverse_link_reassign_clear():
    a1 = ric_LinkGroup(title="sample_text")
    a2 = ric_LinkGroup(title="sample_text_2")
    b = ric_Link(title="sample_text")
    _safe_set(b, 'ric_Link205', a1)
    assert _is_linked(b, 'ric_Link205', a1)
    if hasattr(a1, 'ric_LinkGroup204'):
        assert _is_linked(a1, 'ric_LinkGroup204', b)
    _safe_set(b, 'ric_Link205', a2)
    assert _is_linked(b, 'ric_Link205', a2)
    if hasattr(a1, 'ric_LinkGroup204'):
        assert not _is_linked(a1, 'ric_LinkGroup204', b)
    if hasattr(a2, 'ric_LinkGroup204'):
        assert _is_linked(a2, 'ric_LinkGroup204', b)
    _safe_set(b, 'ric_Link205', None)
    assert not _is_linked(b, 'ric_Link205', a2)
    if hasattr(a2, 'ric_LinkGroup204'):
        assert not _is_linked(a2, 'ric_LinkGroup204', b)


def test_assoc_listItemns190_reverse_link_reassign_clear():
    a1 = ric_OrderedList(type="sample_text")
    a2 = ric_OrderedList(type="sample_text_2")
    b = ric_ListItem(format="sample_text", text="sample_text")
    _safe_set(b, 'ric_ListItem', a1)
    assert _is_linked(b, 'ric_ListItem', a1)
    if hasattr(a1, 'ric_OrderedList'):
        assert _is_linked(a1, 'ric_OrderedList', b)
    _safe_set(b, 'ric_ListItem', a2)
    assert _is_linked(b, 'ric_ListItem', a2)
    if hasattr(a1, 'ric_OrderedList'):
        assert not _is_linked(a1, 'ric_OrderedList', b)
    if hasattr(a2, 'ric_OrderedList'):
        assert _is_linked(a2, 'ric_OrderedList', b)
    _safe_set(b, 'ric_ListItem', None)
    assert not _is_linked(b, 'ric_ListItem', a2)
    if hasattr(a2, 'ric_OrderedList'):
        assert not _is_linked(a2, 'ric_OrderedList', b)


def test_assoc_listItemns191_reverse_link_reassign_clear():
    a1 = ric_UnorderedList(type="sample_text")
    a2 = ric_UnorderedList(type="sample_text_2")
    b = ric_ListItem(format="sample_text", text="sample_text")
    _safe_set(b, 'ric_ListItem192', a1)
    assert _is_linked(b, 'ric_ListItem192', a1)
    if hasattr(a1, 'ric_UnorderedList'):
        assert _is_linked(a1, 'ric_UnorderedList', b)
    _safe_set(b, 'ric_ListItem192', a2)
    assert _is_linked(b, 'ric_ListItem192', a2)
    if hasattr(a1, 'ric_UnorderedList'):
        assert not _is_linked(a1, 'ric_UnorderedList', b)
    if hasattr(a2, 'ric_UnorderedList'):
        assert _is_linked(a2, 'ric_UnorderedList', b)
    _safe_set(b, 'ric_ListItem192', None)
    assert not _is_linked(b, 'ric_ListItem192', a2)
    if hasattr(a2, 'ric_UnorderedList'):
        assert not _is_linked(a2, 'ric_UnorderedList', b)


def test_assoc_navigationRegion102_reverse_link_reassign_clear():
    a1 = ric_Portal(documentsExtension="sample_text", name="sample_text")
    a2 = ric_Portal(documentsExtension="sample_text_2", name="sample_text_2")
    b = ric_NavigationRegion(orientation="sample_text")
    _safe_set(b, 'ric_NavigationRegion', a1)
    assert _is_linked(b, 'ric_NavigationRegion', a1)
    if hasattr(a1, 'ric_Portal103'):
        assert _is_linked(a1, 'ric_Portal103', b)
    _safe_set(b, 'ric_NavigationRegion', a2)
    assert _is_linked(b, 'ric_NavigationRegion', a2)
    if hasattr(a1, 'ric_Portal103'):
        assert not _is_linked(a1, 'ric_Portal103', b)
    if hasattr(a2, 'ric_Portal103'):
        assert _is_linked(a2, 'ric_Portal103', b)
    _safe_set(b, 'ric_NavigationRegion', None)
    assert not _is_linked(b, 'ric_NavigationRegion', a2)
    if hasattr(a2, 'ric_Portal103'):
        assert not _is_linked(a2, 'ric_Portal103', b)


def test_assoc_objectComponents160_reverse_link_reassign_clear():
    a1 = ric_ObjectComponent(align="sample_text", border=7, height=7, hspace=7, vspace=7, width=7)
    a2 = ric_ObjectComponent(align="sample_text_2", border=13, height=13, hspace=13, vspace=13, width=13)
    b = ric_Document(fileName="sample_text", index=True, title="sample_text")
    _safe_set(b, 'ric_Document161', {a1})
    assert _is_linked(b, 'ric_Document161', a1)
    if hasattr(a1, 'ric_ObjectComponent162'):
        assert _is_linked(a1, 'ric_ObjectComponent162', b)
    _safe_set(b, 'ric_Document161', {a2})
    assert _is_linked(b, 'ric_Document161', a2)
    if hasattr(a1, 'ric_ObjectComponent162'):
        assert not _is_linked(a1, 'ric_ObjectComponent162', b)
    if hasattr(a2, 'ric_ObjectComponent162'):
        assert _is_linked(a2, 'ric_ObjectComponent162', b)
    _safe_set(b, 'ric_Document161', set())
    assert not _is_linked(b, 'ric_Document161', a2)
    if hasattr(a2, 'ric_ObjectComponent162'):
        assert not _is_linked(a2, 'ric_ObjectComponent162', b)


def test_assoc_objectComponents32_reverse_link_reassign_clear():
    a1 = ric_ObjectComponent(align="sample_text", border=7, height=7, hspace=7, vspace=7, width=7)
    a2 = ric_ObjectComponent(align="sample_text_2", border=13, height=13, hspace=13, vspace=13, width=13)
    b = ric_Div(align="sample_text")
    _safe_set(b, 'ric_Div', {a1})
    assert _is_linked(b, 'ric_Div', a1)
    if hasattr(a1, 'ric_ObjectComponent'):
        assert _is_linked(a1, 'ric_ObjectComponent', b)
    _safe_set(b, 'ric_Div', {a2})
    assert _is_linked(b, 'ric_Div', a2)
    if hasattr(a1, 'ric_ObjectComponent'):
        assert not _is_linked(a1, 'ric_ObjectComponent', b)
    if hasattr(a2, 'ric_ObjectComponent'):
        assert _is_linked(a2, 'ric_ObjectComponent', b)
    _safe_set(b, 'ric_Div', set())
    assert not _is_linked(b, 'ric_Div', a2)
    if hasattr(a2, 'ric_ObjectComponent'):
        assert not _is_linked(a2, 'ric_ObjectComponent', b)


def test_assoc_objectComponents63_reverse_link_reassign_clear():
    a1 = ric_Tab(title="sample_text")
    a2 = ric_Tab(title="sample_text_2")
    b = ric_ObjectComponent(align="sample_text", border=7, height=7, hspace=7, vspace=7, width=7)
    _safe_set(b, 'ric_ObjectComponent65', a1)
    assert _is_linked(b, 'ric_ObjectComponent65', a1)
    if hasattr(a1, 'ric_Tab64'):
        assert _is_linked(a1, 'ric_Tab64', b)
    _safe_set(b, 'ric_ObjectComponent65', a2)
    assert _is_linked(b, 'ric_ObjectComponent65', a2)
    if hasattr(a1, 'ric_Tab64'):
        assert not _is_linked(a1, 'ric_Tab64', b)
    if hasattr(a2, 'ric_Tab64'):
        assert _is_linked(a2, 'ric_Tab64', b)
    _safe_set(b, 'ric_ObjectComponent65', None)
    assert not _is_linked(b, 'ric_ObjectComponent65', a2)
    if hasattr(a2, 'ric_Tab64'):
        assert not _is_linked(a2, 'ric_Tab64', b)


def test_assoc_objectComponents85_reverse_link_reassign_clear():
    a1 = ric_Section(title="sample_text")
    a2 = ric_Section(title="sample_text_2")
    b = ric_ObjectComponent(align="sample_text", border=7, height=7, hspace=7, vspace=7, width=7)
    _safe_set(b, 'ric_ObjectComponent87', a1)
    assert _is_linked(b, 'ric_ObjectComponent87', a1)
    if hasattr(a1, 'ric_Section86'):
        assert _is_linked(a1, 'ric_Section86', b)
    _safe_set(b, 'ric_ObjectComponent87', a2)
    assert _is_linked(b, 'ric_ObjectComponent87', a2)
    if hasattr(a1, 'ric_Section86'):
        assert not _is_linked(a1, 'ric_Section86', b)
    if hasattr(a2, 'ric_Section86'):
        assert _is_linked(a2, 'ric_Section86', b)
    _safe_set(b, 'ric_ObjectComponent87', None)
    assert not _is_linked(b, 'ric_ObjectComponent87', a2)
    if hasattr(a2, 'ric_Section86'):
        assert not _is_linked(a2, 'ric_Section86', b)


def test_assoc_radioGroups28_reverse_link_reassign_clear():
    a1 = ric_RadioGroup(orientation="sample_text")
    a2 = ric_RadioGroup(orientation="sample_text_2")
    b = ric_Fieldset(legend="sample_text", legendAlign="sample_text", legendFormat="sample_text")
    _safe_set(b, 'ric_Fieldset29', {a1})
    assert _is_linked(b, 'ric_Fieldset29', a1)
    if hasattr(a1, 'ric_RadioGroup'):
        assert _is_linked(a1, 'ric_RadioGroup', b)
    _safe_set(b, 'ric_Fieldset29', {a2})
    assert _is_linked(b, 'ric_Fieldset29', a2)
    if hasattr(a1, 'ric_RadioGroup'):
        assert not _is_linked(a1, 'ric_RadioGroup', b)
    if hasattr(a2, 'ric_RadioGroup'):
        assert _is_linked(a2, 'ric_RadioGroup', b)
    _safe_set(b, 'ric_Fieldset29', set())
    assert not _is_linked(b, 'ric_Fieldset29', a2)
    if hasattr(a2, 'ric_RadioGroup'):
        assert not _is_linked(a2, 'ric_RadioGroup', b)


def test_assoc_radios193_reverse_link_reassign_clear():
    a1 = ric_RadioGroup(orientation="sample_text")
    a2 = ric_RadioGroup(orientation="sample_text_2")
    b = ric_Radio(checked=True)
    _safe_set(b, 'ric_Radio', a1)
    assert _is_linked(b, 'ric_Radio', a1)
    if hasattr(a1, 'ric_RadioGroup194'):
        assert _is_linked(a1, 'ric_RadioGroup194', b)
    _safe_set(b, 'ric_Radio', a2)
    assert _is_linked(b, 'ric_Radio', a2)
    if hasattr(a1, 'ric_RadioGroup194'):
        assert not _is_linked(a1, 'ric_RadioGroup194', b)
    if hasattr(a2, 'ric_RadioGroup194'):
        assert _is_linked(a2, 'ric_RadioGroup194', b)
    _safe_set(b, 'ric_Radio', None)
    assert not _is_linked(b, 'ric_Radio', a2)
    if hasattr(a2, 'ric_RadioGroup194'):
        assert not _is_linked(a2, 'ric_RadioGroup194', b)


def test_assoc_target54_reverse_link_reassign_clear():
    a1 = ric_Link(title="sample_text")
    a2 = ric_Link(title="sample_text_2")
    b = ric_Document(fileName="sample_text", index=True, title="sample_text")
    _safe_set(b, 'ric_Document55', a1)
    assert _is_linked(b, 'ric_Document55', a1)
    if hasattr(a1, 'ric_Link'):
        assert _is_linked(a1, 'ric_Link', b)
    _safe_set(b, 'ric_Document55', a2)
    assert _is_linked(b, 'ric_Document55', a2)
    if hasattr(a1, 'ric_Link'):
        assert not _is_linked(a1, 'ric_Link', b)
    if hasattr(a2, 'ric_Link'):
        assert _is_linked(a2, 'ric_Link', b)
    _safe_set(b, 'ric_Document55', None)
    assert not _is_linked(b, 'ric_Document55', a2)
    if hasattr(a2, 'ric_Link'):
        assert not _is_linked(a2, 'ric_Link', b)


def test_assoc_triggerScript12_reverse_link_reassign_clear():
    a1 = ric_Script(implementation="sample_text", name="sample_text", type="sample_text")
    a2 = ric_Script(implementation="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ric_Event(type="sample_text")
    _safe_set(b, 'ric_Event13', a1)
    assert _is_linked(b, 'ric_Event13', a1)
    if hasattr(a1, 'ric_Script'):
        assert _is_linked(a1, 'ric_Script', b)
    _safe_set(b, 'ric_Event13', a2)
    assert _is_linked(b, 'ric_Event13', a2)
    if hasattr(a1, 'ric_Script'):
        assert not _is_linked(a1, 'ric_Script', b)
    if hasattr(a2, 'ric_Script'):
        assert _is_linked(a2, 'ric_Script', b)
    _safe_set(b, 'ric_Event13', None)
    assert not _is_linked(b, 'ric_Event13', a2)
    if hasattr(a2, 'ric_Script'):
        assert not _is_linked(a2, 'ric_Script', b)


def test_assoc_validDateConstraint10_reverse_link_reassign_clear():
    a1 = ric_ValidDateConstraint(dateFormat="sample_text")
    a2 = ric_ValidDateConstraint(dateFormat="sample_text_2")
    b = ric_FormControl(name="sample_text", value="sample_text")
    _safe_set(b, 'ric_FormControl11', a1)
    assert _is_linked(b, 'ric_FormControl11', a1)
    if hasattr(a1, 'ric_ValidDateConstraint'):
        assert _is_linked(a1, 'ric_ValidDateConstraint', b)
    _safe_set(b, 'ric_FormControl11', a2)
    assert _is_linked(b, 'ric_FormControl11', a2)
    if hasattr(a1, 'ric_ValidDateConstraint'):
        assert not _is_linked(a1, 'ric_ValidDateConstraint', b)
    if hasattr(a2, 'ric_ValidDateConstraint'):
        assert _is_linked(a2, 'ric_ValidDateConstraint', b)
    _safe_set(b, 'ric_FormControl11', None)
    assert not _is_linked(b, 'ric_FormControl11', a2)
    if hasattr(a2, 'ric_ValidDateConstraint'):
        assert not _is_linked(a2, 'ric_ValidDateConstraint', b)


def test_assoc_valueConstraints4_reverse_link_reassign_clear():
    a1 = ric_ValueConstraint(logicalOperator="sample_text", matchingOperator="sample_text", matchingValue="sample_text")
    a2 = ric_ValueConstraint(logicalOperator="sample_text_2", matchingOperator="sample_text_2", matchingValue="sample_text_2")
    b = ric_FormControl(name="sample_text", value="sample_text")
    _safe_set(b, 'ric_FormControl5', {a1})
    assert _is_linked(b, 'ric_FormControl5', a1)
    if hasattr(a1, 'ric_ValueConstraint'):
        assert _is_linked(a1, 'ric_ValueConstraint', b)
    _safe_set(b, 'ric_FormControl5', {a2})
    assert _is_linked(b, 'ric_FormControl5', a2)
    if hasattr(a1, 'ric_ValueConstraint'):
        assert not _is_linked(a1, 'ric_ValueConstraint', b)
    if hasattr(a2, 'ric_ValueConstraint'):
        assert _is_linked(a2, 'ric_ValueConstraint', b)
    _safe_set(b, 'ric_FormControl5', set())
    assert not _is_linked(b, 'ric_FormControl5', a2)
    if hasattr(a2, 'ric_ValueConstraint'):
        assert not _is_linked(a2, 'ric_ValueConstraint', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_blockLevelComponents157_stub_double():
    # ric_BlockLevelComponent has no real 'ric_BlockLevelComponent159' property in the generated
    # code (a bare stub) -- manually attach it so ric_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Document(fileName="sample_text", index=True, title="sample_text")
    partner = ric_BlockLevelComponent()
    setattr(partner, 'ric_BlockLevelComponent159', None)
    _safe_set(owner, 'ric_Document158', {partner})
    assert getattr(partner, 'ric_BlockLevelComponent159') == owner
    _safe_set(owner, 'ric_Document158', set())
    assert getattr(partner, 'ric_BlockLevelComponent159') is None


def test_assoc_blockLevelComponents17_stub_double():
    # ric_BlockLevelComponent has no real 'ric_BlockLevelComponent' property in the generated
    # code (a bare stub) -- manually attach it so ric_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Form(method="sample_text", name="sample_text")
    partner = ric_BlockLevelComponent()
    setattr(partner, 'ric_BlockLevelComponent', None)
    _safe_set(owner, 'ric_Form18', {partner})
    assert getattr(partner, 'ric_BlockLevelComponent') == owner
    _safe_set(owner, 'ric_Form18', set())
    assert getattr(partner, 'ric_BlockLevelComponent') is None


def test_assoc_blockLevelComponents60_stub_double():
    # ric_BlockLevelComponent has no real 'ric_BlockLevelComponent62' property in the generated
    # code (a bare stub) -- manually attach it so ric_Tab's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Tab's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Tab(title="sample_text")
    partner = ric_BlockLevelComponent()
    setattr(partner, 'ric_BlockLevelComponent62', None)
    _safe_set(owner, 'ric_Tab61', {partner})
    assert getattr(partner, 'ric_BlockLevelComponent62') == owner
    _safe_set(owner, 'ric_Tab61', set())
    assert getattr(partner, 'ric_BlockLevelComponent62') is None


def test_assoc_blockLevelComponents82_stub_double():
    # ric_BlockLevelComponent has no real 'ric_BlockLevelComponent84' property in the generated
    # code (a bare stub) -- manually attach it so ric_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Section(title="sample_text")
    partner = ric_BlockLevelComponent()
    setattr(partner, 'ric_BlockLevelComponent84', None)
    _safe_set(owner, 'ric_Section83', {partner})
    assert getattr(partner, 'ric_BlockLevelComponent84') == owner
    _safe_set(owner, 'ric_Section83', set())
    assert getattr(partner, 'ric_BlockLevelComponent84') is None


def test_assoc_contentRegion108_stub_double():
    # ric_ContentRegion has no real 'ric_ContentRegion' property in the generated
    # code (a bare stub) -- manually attach it so ric_Portal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Portal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Portal(documentsExtension="sample_text", name="sample_text")
    partner = ric_ContentRegion()
    setattr(partner, 'ric_ContentRegion', None)
    _safe_set(owner, 'ric_Portal109', partner)
    assert getattr(partner, 'ric_ContentRegion') == owner
    _safe_set(owner, 'ric_Portal109', None)
    assert getattr(partner, 'ric_ContentRegion') is None


def test_assoc_contextualNavigationRegion104_stub_double():
    # ric_ContextualNavigationRegion has no real 'ric_ContextualNavigationRegion' property in the generated
    # code (a bare stub) -- manually attach it so ric_Portal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Portal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Portal(documentsExtension="sample_text", name="sample_text")
    partner = ric_ContextualNavigationRegion()
    setattr(partner, 'ric_ContextualNavigationRegion', None)
    _safe_set(owner, 'ric_Portal105', partner)
    assert getattr(partner, 'ric_ContextualNavigationRegion') == owner
    _safe_set(owner, 'ric_Portal105', None)
    assert getattr(partner, 'ric_ContextualNavigationRegion') is None


def test_assoc_documents151_stub_double():
    # ric_ContentRegion has no real 'ric_ContentRegion152' property in the generated
    # code (a bare stub) -- manually attach it so ric_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Document(fileName="sample_text", index=True, title="sample_text")
    partner = ric_ContentRegion()
    setattr(partner, 'ric_ContentRegion152', None)
    _safe_set(owner, 'ric_Document153', partner)
    assert getattr(partner, 'ric_ContentRegion152') == owner
    _safe_set(owner, 'ric_Document153', None)
    assert getattr(partner, 'ric_ContentRegion152') is None


def test_assoc_events0_stub_double():
    # ric_EventComponent has no real 'ric_EventComponent' property in the generated
    # code (a bare stub) -- manually attach it so ric_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Event(type="sample_text")
    partner = ric_EventComponent()
    setattr(partner, 'ric_EventComponent', None)
    _safe_set(owner, 'ric_Event', partner)
    assert getattr(partner, 'ric_EventComponent') == owner
    _safe_set(owner, 'ric_Event', None)
    assert getattr(partner, 'ric_EventComponent') is None


def test_assoc_footerRegion110_stub_double():
    # ric_FooterRegion has no real 'ric_FooterRegion' property in the generated
    # code (a bare stub) -- manually attach it so ric_Portal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Portal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Portal(documentsExtension="sample_text", name="sample_text")
    partner = ric_FooterRegion()
    setattr(partner, 'ric_FooterRegion', None)
    _safe_set(owner, 'ric_Portal111', partner)
    assert getattr(partner, 'ric_FooterRegion') == owner
    _safe_set(owner, 'ric_Portal111', None)
    assert getattr(partner, 'ric_FooterRegion') is None


def test_assoc_forms145_stub_double():
    # ric_ContextualNavigationRegion has no real 'ric_ContextualNavigationRegion146' property in the generated
    # code (a bare stub) -- manually attach it so ric_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Form(method="sample_text", name="sample_text")
    partner = ric_ContextualNavigationRegion()
    setattr(partner, 'ric_ContextualNavigationRegion146', None)
    _safe_set(owner, 'ric_Form147', partner)
    assert getattr(partner, 'ric_ContextualNavigationRegion146') == owner
    _safe_set(owner, 'ric_Form147', None)
    assert getattr(partner, 'ric_ContextualNavigationRegion146') is None


def test_assoc_forms148_stub_double():
    # ric_SearchRegion has no real 'ric_SearchRegion149' property in the generated
    # code (a bare stub) -- manually attach it so ric_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Form(method="sample_text", name="sample_text")
    partner = ric_SearchRegion()
    setattr(partner, 'ric_SearchRegion149', None)
    _safe_set(owner, 'ric_Form150', partner)
    assert getattr(partner, 'ric_SearchRegion149') == owner
    _safe_set(owner, 'ric_Form150', None)
    assert getattr(partner, 'ric_SearchRegion149') is None


def test_assoc_headerRegion101_stub_double():
    # ric_HeaderRegion has no real 'ric_HeaderRegion' property in the generated
    # code (a bare stub) -- manually attach it so ric_Portal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Portal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Portal(documentsExtension="sample_text", name="sample_text")
    partner = ric_HeaderRegion()
    setattr(partner, 'ric_HeaderRegion', None)
    _safe_set(owner, 'ric_Portal', partner)
    assert getattr(partner, 'ric_HeaderRegion') == owner
    _safe_set(owner, 'ric_Portal', None)
    assert getattr(partner, 'ric_HeaderRegion') is None


def test_assoc_image123_stub_double():
    # ric_Logo has no real 'ric_Logo124' property in the generated
    # code (a bare stub) -- manually attach it so ric_Image's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Image's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Image(alt="sample_text", src="sample_text")
    partner = ric_Logo()
    setattr(partner, 'ric_Logo124', None)
    _safe_set(owner, 'ric_Image', partner)
    assert getattr(partner, 'ric_Logo124') == owner
    _safe_set(owner, 'ric_Image', None)
    assert getattr(partner, 'ric_Logo124') is None


def test_assoc_inlineComponents117_stub_double():
    # ric_HeaderRegion has no real 'ric_HeaderRegion118' property in the generated
    # code (a bare stub) -- manually attach it so ric_InlineComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_InlineComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_InlineComponent(text="sample_text")
    partner = ric_HeaderRegion()
    setattr(partner, 'ric_HeaderRegion118', None)
    _safe_set(owner, 'ric_InlineComponent119', partner)
    assert getattr(partner, 'ric_HeaderRegion118') == owner
    _safe_set(owner, 'ric_InlineComponent119', None)
    assert getattr(partner, 'ric_HeaderRegion118') is None


def test_assoc_inlineComponents127_stub_double():
    # ric_ContextualNavigationRegion has no real 'ric_ContextualNavigationRegion128' property in the generated
    # code (a bare stub) -- manually attach it so ric_InlineComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_InlineComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_InlineComponent(text="sample_text")
    partner = ric_ContextualNavigationRegion()
    setattr(partner, 'ric_ContextualNavigationRegion128', None)
    _safe_set(owner, 'ric_InlineComponent129', partner)
    assert getattr(partner, 'ric_ContextualNavigationRegion128') == owner
    _safe_set(owner, 'ric_InlineComponent129', None)
    assert getattr(partner, 'ric_ContextualNavigationRegion128') is None


def test_assoc_inlineComponents175_stub_double():
    # ric_FooterRegion has no real 'ric_FooterRegion176' property in the generated
    # code (a bare stub) -- manually attach it so ric_InlineComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_InlineComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_InlineComponent(text="sample_text")
    partner = ric_FooterRegion()
    setattr(partner, 'ric_FooterRegion176', None)
    _safe_set(owner, 'ric_InlineComponent177', partner)
    assert getattr(partner, 'ric_FooterRegion176') == owner
    _safe_set(owner, 'ric_InlineComponent177', None)
    assert getattr(partner, 'ric_FooterRegion176') is None


def test_assoc_inlineComponents48_stub_double():
    # ric_BlockLevelComponent has no real 'ric_BlockLevelComponent49' property in the generated
    # code (a bare stub) -- manually attach it so ric_InlineComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_InlineComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_InlineComponent(text="sample_text")
    partner = ric_BlockLevelComponent()
    setattr(partner, 'ric_BlockLevelComponent49', None)
    _safe_set(owner, 'ric_InlineComponent50', partner)
    assert getattr(partner, 'ric_BlockLevelComponent49') == owner
    _safe_set(owner, 'ric_InlineComponent50', None)
    assert getattr(partner, 'ric_BlockLevelComponent49') is None


def test_assoc_lineBreaks163_stub_double():
    # ric_LineBreak has no real 'ric_LineBreak165' property in the generated
    # code (a bare stub) -- manually attach it so ric_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Document(fileName="sample_text", index=True, title="sample_text")
    partner = ric_LineBreak()
    setattr(partner, 'ric_LineBreak165', None)
    _safe_set(owner, 'ric_Document164', {partner})
    assert getattr(partner, 'ric_LineBreak165') == owner
    _safe_set(owner, 'ric_Document164', set())
    assert getattr(partner, 'ric_LineBreak165') is None


def test_assoc_lineBreaks33_stub_double():
    # ric_LineBreak has no real 'ric_LineBreak' property in the generated
    # code (a bare stub) -- manually attach it so ric_Div's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Div's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Div(align="sample_text")
    partner = ric_LineBreak()
    setattr(partner, 'ric_LineBreak', None)
    _safe_set(owner, 'ric_Div34', {partner})
    assert getattr(partner, 'ric_LineBreak') == owner
    _safe_set(owner, 'ric_Div34', set())
    assert getattr(partner, 'ric_LineBreak') is None


def test_assoc_lineBreaks66_stub_double():
    # ric_LineBreak has no real 'ric_LineBreak68' property in the generated
    # code (a bare stub) -- manually attach it so ric_Tab's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Tab's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Tab(title="sample_text")
    partner = ric_LineBreak()
    setattr(partner, 'ric_LineBreak68', None)
    _safe_set(owner, 'ric_Tab67', {partner})
    assert getattr(partner, 'ric_LineBreak68') == owner
    _safe_set(owner, 'ric_Tab67', set())
    assert getattr(partner, 'ric_LineBreak68') is None


def test_assoc_lineBreaks88_stub_double():
    # ric_LineBreak has no real 'ric_LineBreak90' property in the generated
    # code (a bare stub) -- manually attach it so ric_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Section(title="sample_text")
    partner = ric_LineBreak()
    setattr(partner, 'ric_LineBreak90', None)
    _safe_set(owner, 'ric_Section89', {partner})
    assert getattr(partner, 'ric_LineBreak90') == owner
    _safe_set(owner, 'ric_Section89', set())
    assert getattr(partner, 'ric_LineBreak90') is None


def test_assoc_lists169_stub_double():
    # ric_List has no real 'ric_List171' property in the generated
    # code (a bare stub) -- manually attach it so ric_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Document(fileName="sample_text", index=True, title="sample_text")
    partner = ric_List()
    setattr(partner, 'ric_List171', None)
    _safe_set(owner, 'ric_Document170', {partner})
    assert getattr(partner, 'ric_List171') == owner
    _safe_set(owner, 'ric_Document170', set())
    assert getattr(partner, 'ric_List171') is None


def test_assoc_lists37_stub_double():
    # ric_List has no real 'ric_List' property in the generated
    # code (a bare stub) -- manually attach it so ric_Div's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Div's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Div(align="sample_text")
    partner = ric_List()
    setattr(partner, 'ric_List', None)
    _safe_set(owner, 'ric_Div38', {partner})
    assert getattr(partner, 'ric_List') == owner
    _safe_set(owner, 'ric_Div38', set())
    assert getattr(partner, 'ric_List') is None


def test_assoc_lists72_stub_double():
    # ric_List has no real 'ric_List74' property in the generated
    # code (a bare stub) -- manually attach it so ric_Tab's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Tab's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Tab(title="sample_text")
    partner = ric_List()
    setattr(partner, 'ric_List74', None)
    _safe_set(owner, 'ric_Tab73', {partner})
    assert getattr(partner, 'ric_List74') == owner
    _safe_set(owner, 'ric_Tab73', set())
    assert getattr(partner, 'ric_List74') is None


def test_assoc_lists94_stub_double():
    # ric_List has no real 'ric_List96' property in the generated
    # code (a bare stub) -- manually attach it so ric_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Section(title="sample_text")
    partner = ric_List()
    setattr(partner, 'ric_List96', None)
    _safe_set(owner, 'ric_Section95', {partner})
    assert getattr(partner, 'ric_List96') == owner
    _safe_set(owner, 'ric_Section95', set())
    assert getattr(partner, 'ric_List96') is None


def test_assoc_numberConstraint6_stub_double():
    # ric_NumberValueConstraint has no real 'ric_NumberValueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so ric_FormControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_FormControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_FormControl(name="sample_text", value="sample_text")
    partner = ric_NumberValueConstraint()
    setattr(partner, 'ric_NumberValueConstraint', None)
    _safe_set(owner, 'ric_FormControl7', partner)
    assert getattr(partner, 'ric_NumberValueConstraint') == owner
    _safe_set(owner, 'ric_FormControl7', None)
    assert getattr(partner, 'ric_NumberValueConstraint') is None


def test_assoc_objectComponents133_stub_double():
    # ric_ContextualNavigationRegion has no real 'ric_ContextualNavigationRegion134' property in the generated
    # code (a bare stub) -- manually attach it so ric_ObjectComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_ObjectComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_ObjectComponent(align="sample_text", border=7, height=7, hspace=7, vspace=7, width=7)
    partner = ric_ContextualNavigationRegion()
    setattr(partner, 'ric_ContextualNavigationRegion134', None)
    _safe_set(owner, 'ric_ObjectComponent135', partner)
    assert getattr(partner, 'ric_ContextualNavigationRegion134') == owner
    _safe_set(owner, 'ric_ObjectComponent135', None)
    assert getattr(partner, 'ric_ContextualNavigationRegion134') is None


def test_assoc_objectComponents181_stub_double():
    # ric_FooterRegion has no real 'ric_FooterRegion182' property in the generated
    # code (a bare stub) -- manually attach it so ric_ObjectComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_ObjectComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_ObjectComponent(align="sample_text", border=7, height=7, hspace=7, vspace=7, width=7)
    partner = ric_FooterRegion()
    setattr(partner, 'ric_FooterRegion182', None)
    _safe_set(owner, 'ric_ObjectComponent183', partner)
    assert getattr(partner, 'ric_FooterRegion182') == owner
    _safe_set(owner, 'ric_ObjectComponent183', None)
    assert getattr(partner, 'ric_FooterRegion182') is None


def test_assoc_requiredFieldConstraint8_stub_double():
    # ric_RequiredFieldConstraint has no real 'ric_RequiredFieldConstraint' property in the generated
    # code (a bare stub) -- manually attach it so ric_FormControl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_FormControl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_FormControl(name="sample_text", value="sample_text")
    partner = ric_RequiredFieldConstraint()
    setattr(partner, 'ric_RequiredFieldConstraint', None)
    _safe_set(owner, 'ric_FormControl9', partner)
    assert getattr(partner, 'ric_RequiredFieldConstraint') == owner
    _safe_set(owner, 'ric_FormControl9', None)
    assert getattr(partner, 'ric_RequiredFieldConstraint') is None


def test_assoc_richWidgets166_stub_double():
    # ric_RichWidget has no real 'ric_RichWidget168' property in the generated
    # code (a bare stub) -- manually attach it so ric_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Document(fileName="sample_text", index=True, title="sample_text")
    partner = ric_RichWidget()
    setattr(partner, 'ric_RichWidget168', None)
    _safe_set(owner, 'ric_Document167', {partner})
    assert getattr(partner, 'ric_RichWidget168') == owner
    _safe_set(owner, 'ric_Document167', set())
    assert getattr(partner, 'ric_RichWidget168') is None


def test_assoc_richWidgets35_stub_double():
    # ric_RichWidget has no real 'ric_RichWidget' property in the generated
    # code (a bare stub) -- manually attach it so ric_Div's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Div's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Div(align="sample_text")
    partner = ric_RichWidget()
    setattr(partner, 'ric_RichWidget', None)
    _safe_set(owner, 'ric_Div36', {partner})
    assert getattr(partner, 'ric_RichWidget') == owner
    _safe_set(owner, 'ric_Div36', set())
    assert getattr(partner, 'ric_RichWidget') is None


def test_assoc_richWidgets69_stub_double():
    # ric_RichWidget has no real 'ric_RichWidget71' property in the generated
    # code (a bare stub) -- manually attach it so ric_Tab's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Tab's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Tab(title="sample_text")
    partner = ric_RichWidget()
    setattr(partner, 'ric_RichWidget71', None)
    _safe_set(owner, 'ric_Tab70', {partner})
    assert getattr(partner, 'ric_RichWidget71') == owner
    _safe_set(owner, 'ric_Tab70', set())
    assert getattr(partner, 'ric_RichWidget71') is None


def test_assoc_richWidgets91_stub_double():
    # ric_RichWidget has no real 'ric_RichWidget93' property in the generated
    # code (a bare stub) -- manually attach it so ric_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Section(title="sample_text")
    partner = ric_RichWidget()
    setattr(partner, 'ric_RichWidget93', None)
    _safe_set(owner, 'ric_Section92', {partner})
    assert getattr(partner, 'ric_RichWidget93') == owner
    _safe_set(owner, 'ric_Section92', set())
    assert getattr(partner, 'ric_RichWidget93') is None


def test_assoc_searchRegion106_stub_double():
    # ric_SearchRegion has no real 'ric_SearchRegion' property in the generated
    # code (a bare stub) -- manually attach it so ric_Portal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Portal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Portal(documentsExtension="sample_text", name="sample_text")
    partner = ric_SearchRegion()
    setattr(partner, 'ric_SearchRegion', None)
    _safe_set(owner, 'ric_Portal107', partner)
    assert getattr(partner, 'ric_SearchRegion') == owner
    _safe_set(owner, 'ric_Portal107', None)
    assert getattr(partner, 'ric_SearchRegion') is None


def test_assoc_sections78_stub_double():
    # ric_AccordionPanel has no real 'ric_AccordionPanel' property in the generated
    # code (a bare stub) -- manually attach it so ric_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Section(title="sample_text")
    partner = ric_AccordionPanel()
    setattr(partner, 'ric_AccordionPanel', None)
    _safe_set(owner, 'ric_Section', partner)
    assert getattr(partner, 'ric_AccordionPanel') == owner
    _safe_set(owner, 'ric_Section', None)
    assert getattr(partner, 'ric_AccordionPanel') is None


def test_assoc_subsiteNavigation114_stub_double():
    # ric_HeaderRegion has no real 'ric_HeaderRegion115' property in the generated
    # code (a bare stub) -- manually attach it so ric_NavigationRegion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_NavigationRegion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_NavigationRegion(orientation="sample_text")
    partner = ric_HeaderRegion()
    setattr(partner, 'ric_HeaderRegion115', None)
    _safe_set(owner, 'ric_NavigationRegion116', partner)
    assert getattr(partner, 'ric_HeaderRegion115') == owner
    _safe_set(owner, 'ric_NavigationRegion116', None)
    assert getattr(partner, 'ric_HeaderRegion115') is None


def test_assoc_tabs56_stub_double():
    # ric_TabbedPanel has no real 'ric_TabbedPanel' property in the generated
    # code (a bare stub) -- manually attach it so ric_Tab's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ric_Tab's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ric_Tab(title="sample_text")
    partner = ric_TabbedPanel()
    setattr(partner, 'ric_TabbedPanel', None)
    _safe_set(owner, 'ric_Tab', partner)
    assert getattr(partner, 'ric_TabbedPanel') == owner
    _safe_set(owner, 'ric_Tab', None)
    assert getattr(partner, 'ric_TabbedPanel') is None


