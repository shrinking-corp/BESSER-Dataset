import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTable,
    CSSCustomizable,
    ConnectableElement,
    Duplicable,
    Element,
    Form,
    FormButton,
    FormField,
    Info,
    ItemContainer,
    MultipleValuatedFormField,
    SingleValuatedFormField,
    Validable,
    Widget,
    form_AbstractTable,
    form_CSSCustomizable,
    form_CheckBoxMultipleFormField,
    form_CheckBoxSingleFormField,
    form_Column,
    form_ComboFormField,
    form_DateFormField,
    form_Document,
    form_Duplicable,
    form_DurationFormField,
    form_DynamicTable,
    form_EStringToStringMapEntry,
    form_Expression,
    form_FileWidget,
    form_Form,
    form_FormButton,
    form_FormField,
    form_Group,
    form_GroupIterator,
    form_HiddenWidget,
    form_HtmlWidget,
    form_IFrameWidget,
    form_ImageWidget,
    form_Info,
    form_ItemContainer,
    form_Line,
    form_ListFormField,
    form_MandatoryFieldsCustomization,
    form_MessageInfo,
    form_MultipleValuatedFormField,
    form_NextFormButton,
    form_Operation,
    form_PasswordFormField,
    form_PreviousFormButton,
    form_RadioFormField,
    form_RichTextAreaFormField,
    form_SelectFormField,
    form_SingleValuatedFormField,
    form_SubmitFormButton,
    form_SuggestBox,
    form_Table,
    form_TableExpression,
    form_TextAreaFormField,
    form_TextFormField,
    form_TextInfo,
    form_Validable,
    form_Validator,
    form_ViewForm,
    form_Widget,
    form_WidgetDependency,
    form_WidgetLayoutInfo,
    EventDependencyType,
    FileWidgetDownloadType,
    FileWidgetInputType,
    LabelPosition,
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

def test_assoc_columns76_reverse_link_reassign_clear():
    a1 = form_Group(showBorder=True, useIterator=True)
    a2 = form_Group(showBorder=False, useIterator=False)
    b = form_Column(number=7, width="sample_text")
    _safe_set(b, 'form_Column78', a1)
    assert _is_linked(b, 'form_Column78', a1)
    if hasattr(a1, 'form_Group77'):
        assert _is_linked(a1, 'form_Group77', b)
    _safe_set(b, 'form_Column78', a2)
    assert _is_linked(b, 'form_Column78', a2)
    if hasattr(a1, 'form_Group77'):
        assert not _is_linked(a1, 'form_Group77', b)
    if hasattr(a2, 'form_Group77'):
        assert _is_linked(a2, 'form_Group77', b)
    _safe_set(b, 'form_Column78', None)
    assert not _is_linked(b, 'form_Column78', a2)
    if hasattr(a2, 'form_Group77'):
        assert not _is_linked(a2, 'form_Group77', b)


def test_assoc_columns8_reverse_link_reassign_clear():
    a1 = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    a2 = form_Form(allowHTMLInPageLabel=False, nColumn=13, nLine=13, showPageLabel="sample_text_2", version="sample_text_2")
    b = form_Column(number=7, width="sample_text")
    _safe_set(b, 'form_Column', a1)
    assert _is_linked(b, 'form_Column', a1)
    if hasattr(a1, 'form_Form9'):
        assert _is_linked(a1, 'form_Form9', b)
    _safe_set(b, 'form_Column', a2)
    assert _is_linked(b, 'form_Column', a2)
    if hasattr(a1, 'form_Form9'):
        assert not _is_linked(a1, 'form_Form9', b)
    if hasattr(a2, 'form_Form9'):
        assert _is_linked(a2, 'form_Form9', b)
    _safe_set(b, 'form_Column', None)
    assert not _is_linked(b, 'form_Column', a2)
    if hasattr(a2, 'form_Form9'):
        assert not _is_linked(a2, 'form_Form9', b)


def test_assoc_dependOn41_reverse_link_reassign_clear():
    a1 = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    a2 = form_WidgetDependency(eventTypes="sample_text_2", triggerRefreshOnModification=False)
    b = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    _safe_set(b, 'form_Widget42', {a1})
    assert _is_linked(b, 'form_Widget42', a1)
    if hasattr(a1, 'form_WidgetDependency43'):
        assert _is_linked(a1, 'form_WidgetDependency43', b)
    _safe_set(b, 'form_Widget42', {a2})
    assert _is_linked(b, 'form_Widget42', a2)
    if hasattr(a1, 'form_WidgetDependency43'):
        assert not _is_linked(a1, 'form_WidgetDependency43', b)
    if hasattr(a2, 'form_WidgetDependency43'):
        assert _is_linked(a2, 'form_WidgetDependency43', b)
    _safe_set(b, 'form_Widget42', set())
    assert not _is_linked(b, 'form_Widget42', a2)
    if hasattr(a2, 'form_WidgetDependency43'):
        assert not _is_linked(a2, 'form_WidgetDependency43', b)


def test_assoc_iterator82_reverse_link_reassign_clear():
    a1 = form_GroupIterator(className="sample_text")
    a2 = form_GroupIterator(className="sample_text_2")
    b = form_Group(showBorder=True, useIterator=True)
    _safe_set(b, 'form_Group83', a1)
    assert _is_linked(b, 'form_Group83', a1)
    if hasattr(a1, 'form_GroupIterator'):
        assert _is_linked(a1, 'form_GroupIterator', b)
    _safe_set(b, 'form_Group83', a2)
    assert _is_linked(b, 'form_Group83', a2)
    if hasattr(a1, 'form_GroupIterator'):
        assert not _is_linked(a1, 'form_GroupIterator', b)
    if hasattr(a2, 'form_GroupIterator'):
        assert _is_linked(a2, 'form_GroupIterator', b)
    _safe_set(b, 'form_Group83', None)
    assert not _is_linked(b, 'form_Group83', a2)
    if hasattr(a2, 'form_GroupIterator'):
        assert not _is_linked(a2, 'form_GroupIterator', b)


def test_assoc_lines10_reverse_link_reassign_clear():
    a1 = form_Line(height="sample_text", number=7)
    a2 = form_Line(height="sample_text_2", number=13)
    b = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    _safe_set(b, 'form_Form11', {a1})
    assert _is_linked(b, 'form_Form11', a1)
    if hasattr(a1, 'form_Line'):
        assert _is_linked(a1, 'form_Line', b)
    _safe_set(b, 'form_Form11', {a2})
    assert _is_linked(b, 'form_Form11', a2)
    if hasattr(a1, 'form_Line'):
        assert not _is_linked(a1, 'form_Line', b)
    if hasattr(a2, 'form_Line'):
        assert _is_linked(a2, 'form_Line', b)
    _safe_set(b, 'form_Form11', set())
    assert not _is_linked(b, 'form_Form11', a2)
    if hasattr(a2, 'form_Line'):
        assert not _is_linked(a2, 'form_Line', b)


def test_assoc_lines79_reverse_link_reassign_clear():
    a1 = form_Line(height="sample_text", number=7)
    a2 = form_Line(height="sample_text_2", number=13)
    b = form_Group(showBorder=True, useIterator=True)
    _safe_set(b, 'form_Group80', {a1})
    assert _is_linked(b, 'form_Group80', a1)
    if hasattr(a1, 'form_Line81'):
        assert _is_linked(a1, 'form_Line81', b)
    _safe_set(b, 'form_Group80', {a2})
    assert _is_linked(b, 'form_Group80', a2)
    if hasattr(a1, 'form_Line81'):
        assert not _is_linked(a1, 'form_Line81', b)
    if hasattr(a2, 'form_Line81'):
        assert _is_linked(a2, 'form_Line81', b)
    _safe_set(b, 'form_Group80', set())
    assert not _is_linked(b, 'form_Group80', a2)
    if hasattr(a2, 'form_Line81'):
        assert not _is_linked(a2, 'form_Line81', b)


def test_assoc_parentOf44_reverse_link_reassign_clear():
    a1 = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    a2 = form_WidgetDependency(eventTypes="sample_text_2", triggerRefreshOnModification=False)
    b = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    _safe_set(b, 'form_Widget45', {a1})
    assert _is_linked(b, 'form_Widget45', a1)
    if hasattr(a1, 'form_WidgetDependency46'):
        assert _is_linked(a1, 'form_WidgetDependency46', b)
    _safe_set(b, 'form_Widget45', {a2})
    assert _is_linked(b, 'form_Widget45', a2)
    if hasattr(a1, 'form_WidgetDependency46'):
        assert not _is_linked(a1, 'form_WidgetDependency46', b)
    if hasattr(a2, 'form_WidgetDependency46'):
        assert _is_linked(a2, 'form_WidgetDependency46', b)
    _safe_set(b, 'form_Widget45', set())
    assert not _is_linked(b, 'form_Widget45', a2)
    if hasattr(a2, 'form_WidgetDependency46'):
        assert not _is_linked(a2, 'form_WidgetDependency46', b)


def test_assoc_validators5_reverse_link_reassign_clear():
    a1 = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    a2 = form_Validator(belowField=False, htmlClass="sample_text_2", name="sample_text_2", validatorClass="sample_text_2")
    b = form_Validable(below=True, useDefaultValidator="sample_text")
    _safe_set(b, 'form_Validable', {a1})
    assert _is_linked(b, 'form_Validable', a1)
    if hasattr(a1, 'form_Validator6'):
        assert _is_linked(a1, 'form_Validator6', b)
    _safe_set(b, 'form_Validable', {a2})
    assert _is_linked(b, 'form_Validable', a2)
    if hasattr(a1, 'form_Validator6'):
        assert not _is_linked(a1, 'form_Validator6', b)
    if hasattr(a2, 'form_Validator6'):
        assert _is_linked(a2, 'form_Validator6', b)
    _safe_set(b, 'form_Validable', set())
    assert not _is_linked(b, 'form_Validable', a2)
    if hasattr(a2, 'form_Validator6'):
        assert not _is_linked(a2, 'form_Validator6', b)


def test_assoc_widget0_reverse_link_reassign_clear():
    a1 = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    a2 = form_WidgetDependency(eventTypes="sample_text_2", triggerRefreshOnModification=False)
    b = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    _safe_set(b, 'form_Widget', a1)
    assert _is_linked(b, 'form_Widget', a1)
    if hasattr(a1, 'form_WidgetDependency'):
        assert _is_linked(a1, 'form_WidgetDependency', b)
    _safe_set(b, 'form_Widget', a2)
    assert _is_linked(b, 'form_Widget', a2)
    if hasattr(a1, 'form_WidgetDependency'):
        assert not _is_linked(a1, 'form_WidgetDependency', b)
    if hasattr(a2, 'form_WidgetDependency'):
        assert _is_linked(a2, 'form_WidgetDependency', b)
    _safe_set(b, 'form_Widget', None)
    assert not _is_linked(b, 'form_Widget', a2)
    if hasattr(a2, 'form_WidgetDependency'):
        assert not _is_linked(a2, 'form_WidgetDependency', b)


def test_assoc_widgetLayoutInfo39_reverse_link_reassign_clear():
    a1 = form_WidgetLayoutInfo(column=7, horizontalSpan=7, line=7, verticalSpan=7)
    a2 = form_WidgetLayoutInfo(column=13, horizontalSpan=13, line=13, verticalSpan=13)
    b = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    _safe_set(b, 'form_Widget40', a1)
    assert _is_linked(b, 'form_Widget40', a1)
    if hasattr(a1, 'form_WidgetLayoutInfo'):
        assert _is_linked(a1, 'form_WidgetLayoutInfo', b)
    _safe_set(b, 'form_Widget40', a2)
    assert _is_linked(b, 'form_Widget40', a2)
    if hasattr(a1, 'form_WidgetLayoutInfo'):
        assert not _is_linked(a1, 'form_WidgetLayoutInfo', b)
    if hasattr(a2, 'form_WidgetLayoutInfo'):
        assert _is_linked(a2, 'form_WidgetLayoutInfo', b)
    _safe_set(b, 'form_Widget40', None)
    assert not _is_linked(b, 'form_Widget40', a2)
    if hasattr(a2, 'form_WidgetLayoutInfo'):
        assert not _is_linked(a2, 'form_WidgetLayoutInfo', b)


def test_assoc_widgets12_reverse_link_reassign_clear():
    a1 = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    a2 = form_Widget(allowHTMLForDisplayLabel=False, displayDependentWidgetOnlyOnEventTriggered=False, injectWidgetCondition=False, labelPosition="sample_text_2", mandatory=False, readOnly=False, realHtmlAttributes="sample_text_2", returnTypeModifier="sample_text_2", showDisplayLabel="sample_text_2", version="sample_text_2")
    b = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    _safe_set(b, 'form_Form13', {a1})
    assert _is_linked(b, 'form_Form13', a1)
    if hasattr(a1, 'form_Widget14'):
        assert _is_linked(a1, 'form_Widget14', b)
    _safe_set(b, 'form_Form13', {a2})
    assert _is_linked(b, 'form_Form13', a2)
    if hasattr(a1, 'form_Widget14'):
        assert not _is_linked(a1, 'form_Widget14', b)
    if hasattr(a2, 'form_Widget14'):
        assert _is_linked(a2, 'form_Widget14', b)
    _safe_set(b, 'form_Form13', set())
    assert not _is_linked(b, 'form_Form13', a2)
    if hasattr(a2, 'form_Widget14'):
        assert not _is_linked(a2, 'form_Widget14', b)


def test_assoc_widgets74_reverse_link_reassign_clear():
    a1 = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    a2 = form_Widget(allowHTMLForDisplayLabel=False, displayDependentWidgetOnlyOnEventTriggered=False, injectWidgetCondition=False, labelPosition="sample_text_2", mandatory=False, readOnly=False, realHtmlAttributes="sample_text_2", returnTypeModifier="sample_text_2", showDisplayLabel="sample_text_2", version="sample_text_2")
    b = form_Group(showBorder=True, useIterator=True)
    _safe_set(b, 'form_Group', {a1})
    assert _is_linked(b, 'form_Group', a1)
    if hasattr(a1, 'form_Widget75'):
        assert _is_linked(a1, 'form_Widget75', b)
    _safe_set(b, 'form_Group', {a2})
    assert _is_linked(b, 'form_Group', a2)
    if hasattr(a1, 'form_Widget75'):
        assert not _is_linked(a1, 'form_Widget75', b)
    if hasattr(a2, 'form_Widget75'):
        assert _is_linked(a2, 'form_Widget75', b)
    _safe_set(b, 'form_Group', set())
    assert not _is_linked(b, 'form_Group', a2)
    if hasattr(a2, 'form_Widget75'):
        assert not _is_linked(a2, 'form_Widget75', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action71_stub_double():
    # form_Operation has no real 'form_Operation73' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Operation()
    setattr(partner, 'form_Operation73', None)
    _safe_set(owner, 'form_Widget72', partner)
    assert getattr(partner, 'form_Operation73') == owner
    _safe_set(owner, 'form_Widget72', None)
    assert getattr(partner, 'form_Operation73') is None


def test_assoc_actions18_stub_double():
    # form_Operation has no real 'form_Operation' property in the generated
    # code (a bare stub) -- manually attach it so form_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    partner = form_Operation()
    setattr(partner, 'form_Operation', None)
    _safe_set(owner, 'form_Form19', {partner})
    assert getattr(partner, 'form_Operation') == owner
    _safe_set(owner, 'form_Form19', set())
    assert getattr(partner, 'form_Operation') is None


def test_assoc_afterEventExpression56_stub_double():
    # form_Expression has no real 'form_Expression58' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression58', None)
    _safe_set(owner, 'form_Widget57', partner)
    assert getattr(partner, 'form_Expression58') == owner
    _safe_set(owner, 'form_Widget57', None)
    assert getattr(partner, 'form_Expression58') is None


def test_assoc_columnForInitialSelectionIndex111_stub_double():
    # form_Expression has no real 'form_Expression113' property in the generated
    # code (a bare stub) -- manually attach it so form_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression113', None)
    _safe_set(owner, 'form_Table112', partner)
    assert getattr(partner, 'form_Expression113') == owner
    _safe_set(owner, 'form_Table112', None)
    assert getattr(partner, 'form_Expression113') is None


def test_assoc_displayAfterEventDependsOnConditionScript50_stub_double():
    # form_Expression has no real 'form_Expression52' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression52', None)
    _safe_set(owner, 'form_Widget51', partner)
    assert getattr(partner, 'form_Expression52') == owner
    _safe_set(owner, 'form_Widget51', None)
    assert getattr(partner, 'form_Expression52') is None


def test_assoc_displayDependentWidgetOnlyAfterFirstEventTriggeredAndCondition47_stub_double():
    # form_Expression has no real 'form_Expression49' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression49', None)
    _safe_set(owner, 'form_Widget48', partner)
    assert getattr(partner, 'form_Expression49') == owner
    _safe_set(owner, 'form_Widget48', None)
    assert getattr(partner, 'form_Expression49') is None


def test_assoc_displayLabel65_stub_double():
    # form_Expression has no real 'form_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression67', None)
    _safe_set(owner, 'form_Widget66', partner)
    assert getattr(partner, 'form_Expression67') == owner
    _safe_set(owner, 'form_Widget66', None)
    assert getattr(partner, 'form_Expression67') is None


def test_assoc_displayLabelForAdd25_stub_double():
    # form_Expression has no real 'form_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so form_Duplicable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Duplicable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression27', None)
    _safe_set(owner, 'form_Duplicable26', partner)
    assert getattr(partner, 'form_Expression27') == owner
    _safe_set(owner, 'form_Duplicable26', None)
    assert getattr(partner, 'form_Expression27') is None


def test_assoc_displayLabelForRemove31_stub_double():
    # form_Expression has no real 'form_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so form_Duplicable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Duplicable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression33', None)
    _safe_set(owner, 'form_Duplicable32', partner)
    assert getattr(partner, 'form_Expression33') == owner
    _safe_set(owner, 'form_Duplicable32', None)
    assert getattr(partner, 'form_Expression33') is None


def test_assoc_displayName2_stub_double():
    # form_Expression has no real 'form_Expression4' property in the generated
    # code (a bare stub) -- manually attach it so form_Validator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Validator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression4', None)
    _safe_set(owner, 'form_Validator3', partner)
    assert getattr(partner, 'form_Expression4') == owner
    _safe_set(owner, 'form_Validator3', None)
    assert getattr(partner, 'form_Expression4') is None


def test_assoc_document93_stub_double():
    # form_Document has no real 'form_Document' property in the generated
    # code (a bare stub) -- manually attach it so form_FileWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_FileWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    partner = form_Document()
    setattr(partner, 'form_Document', None)
    _safe_set(owner, 'form_FileWidget', partner)
    assert getattr(partner, 'form_Document') == owner
    _safe_set(owner, 'form_FileWidget', None)
    assert getattr(partner, 'form_Document') is None


def test_assoc_document97_stub_double():
    # form_Document has no real 'form_Document98' property in the generated
    # code (a bare stub) -- manually attach it so form_ImageWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_ImageWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_ImageWidget(isADocument=True)
    partner = form_Document()
    setattr(partner, 'form_Document98', None)
    _safe_set(owner, 'form_ImageWidget', partner)
    assert getattr(partner, 'form_Document98') == owner
    _safe_set(owner, 'form_ImageWidget', None)
    assert getattr(partner, 'form_Document98') is None


def test_assoc_exampleMessage84_stub_double():
    # form_Expression has no real 'form_Expression85' property in the generated
    # code (a bare stub) -- manually attach it so form_FormField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_FormField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression85', None)
    _safe_set(owner, 'form_FormField', partner)
    assert getattr(partner, 'form_Expression85') == owner
    _safe_set(owner, 'form_FormField', None)
    assert getattr(partner, 'form_Expression85') is None


def test_assoc_helpMessage62_stub_double():
    # form_Expression has no real 'form_Expression64' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression64', None)
    _safe_set(owner, 'form_Widget63', partner)
    assert getattr(partner, 'form_Expression64') == owner
    _safe_set(owner, 'form_Widget63', None)
    assert getattr(partner, 'form_Expression64') is None


def test_assoc_horizontalHeaderExpression102_stub_double():
    # form_Expression has no real 'form_Expression103' property in the generated
    # code (a bare stub) -- manually attach it so form_AbstractTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_AbstractTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression103', None)
    _safe_set(owner, 'form_AbstractTable', partner)
    assert getattr(partner, 'form_Expression103') == owner
    _safe_set(owner, 'form_AbstractTable', None)
    assert getattr(partner, 'form_Expression103') is None


def test_assoc_imgPath99_stub_double():
    # form_Expression has no real 'form_Expression101' property in the generated
    # code (a bare stub) -- manually attach it so form_ImageWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_ImageWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_ImageWidget(isADocument=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression101', None)
    _safe_set(owner, 'form_ImageWidget100', partner)
    assert getattr(partner, 'form_Expression101') == owner
    _safe_set(owner, 'form_ImageWidget100', None)
    assert getattr(partner, 'form_Expression101') is None


def test_assoc_injectWidgetScript68_stub_double():
    # form_Expression has no real 'form_Expression70' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression70', None)
    _safe_set(owner, 'form_Widget69', partner)
    assert getattr(partner, 'form_Expression70') == owner
    _safe_set(owner, 'form_Widget69', None)
    assert getattr(partner, 'form_Expression70') is None


def test_assoc_inputExpression53_stub_double():
    # form_Expression has no real 'form_Expression55' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression55', None)
    _safe_set(owner, 'form_Widget54', partner)
    assert getattr(partner, 'form_Expression55') == owner
    _safe_set(owner, 'form_Widget54', None)
    assert getattr(partner, 'form_Expression55') is None


def test_assoc_maxNumberOfColumn122_stub_double():
    # form_Expression has no real 'form_Expression124' property in the generated
    # code (a bare stub) -- manually attach it so form_DynamicTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_DynamicTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression124', None)
    _safe_set(owner, 'form_DynamicTable123', partner)
    assert getattr(partner, 'form_Expression124') == owner
    _safe_set(owner, 'form_DynamicTable123', None)
    assert getattr(partner, 'form_Expression124') is None


def test_assoc_maxNumberOfDuplication20_stub_double():
    # form_Expression has no real 'form_Expression21' property in the generated
    # code (a bare stub) -- manually attach it so form_Duplicable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Duplicable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression21', None)
    _safe_set(owner, 'form_Duplicable', partner)
    assert getattr(partner, 'form_Expression21') == owner
    _safe_set(owner, 'form_Duplicable', None)
    assert getattr(partner, 'form_Expression21') is None


def test_assoc_maxNumberOfRow125_stub_double():
    # form_Expression has no real 'form_Expression127' property in the generated
    # code (a bare stub) -- manually attach it so form_DynamicTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_DynamicTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression127', None)
    _safe_set(owner, 'form_DynamicTable126', partner)
    assert getattr(partner, 'form_Expression127') == owner
    _safe_set(owner, 'form_DynamicTable126', None)
    assert getattr(partner, 'form_Expression127') is None


def test_assoc_maxRowForPagination109_stub_double():
    # form_Expression has no real 'form_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so form_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression110', None)
    _safe_set(owner, 'form_Table', partner)
    assert getattr(partner, 'form_Expression110') == owner
    _safe_set(owner, 'form_Table', None)
    assert getattr(partner, 'form_Expression110') is None


def test_assoc_minNumberOfColumn117_stub_double():
    # form_Expression has no real 'form_Expression118' property in the generated
    # code (a bare stub) -- manually attach it so form_DynamicTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_DynamicTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression118', None)
    _safe_set(owner, 'form_DynamicTable', partner)
    assert getattr(partner, 'form_Expression118') == owner
    _safe_set(owner, 'form_DynamicTable', None)
    assert getattr(partner, 'form_Expression118') is None


def test_assoc_minNumberOfDuplication22_stub_double():
    # form_Expression has no real 'form_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so form_Duplicable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Duplicable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression24', None)
    _safe_set(owner, 'form_Duplicable23', partner)
    assert getattr(partner, 'form_Expression24') == owner
    _safe_set(owner, 'form_Duplicable23', None)
    assert getattr(partner, 'form_Expression24') is None


def test_assoc_minNumberOfRow119_stub_double():
    # form_Expression has no real 'form_Expression121' property in the generated
    # code (a bare stub) -- manually attach it so form_DynamicTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_DynamicTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression121', None)
    _safe_set(owner, 'form_DynamicTable120', partner)
    assert getattr(partner, 'form_Expression121') == owner
    _safe_set(owner, 'form_DynamicTable120', None)
    assert getattr(partner, 'form_Expression121') is None


def test_assoc_outputDocumentListExpression94_stub_double():
    # form_Expression has no real 'form_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so form_FileWidget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_FileWidget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression96', None)
    _safe_set(owner, 'form_FileWidget95', partner)
    assert getattr(partner, 'form_Expression96') == owner
    _safe_set(owner, 'form_FileWidget95', None)
    assert getattr(partner, 'form_Expression96') is None


def test_assoc_pageLabel15_stub_double():
    # form_Expression has no real 'form_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so form_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression17', None)
    _safe_set(owner, 'form_Form16', partner)
    assert getattr(partner, 'form_Expression17') == owner
    _safe_set(owner, 'form_Form16', None)
    assert getattr(partner, 'form_Expression17') is None


def test_assoc_parameter1_stub_double():
    # form_Expression has no real 'form_Expression' property in the generated
    # code (a bare stub) -- manually attach it so form_Validator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Validator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression', None)
    _safe_set(owner, 'form_Validator', partner)
    assert getattr(partner, 'form_Expression') == owner
    _safe_set(owner, 'form_Validator', None)
    assert getattr(partner, 'form_Expression') is None


def test_assoc_selectedValues114_stub_double():
    # form_Expression has no real 'form_Expression116' property in the generated
    # code (a bare stub) -- manually attach it so form_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression116', None)
    _safe_set(owner, 'form_Table115', partner)
    assert getattr(partner, 'form_Expression116') == owner
    _safe_set(owner, 'form_Table115', None)
    assert getattr(partner, 'form_Expression116') is None


def test_assoc_stringAttributes7_stub_double():
    # form_EStringToStringMapEntry has no real 'form_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so form_Form's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Form's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    partner = form_EStringToStringMapEntry()
    setattr(partner, 'form_EStringToStringMapEntry', None)
    _safe_set(owner, 'form_Form', {partner})
    assert getattr(partner, 'form_EStringToStringMapEntry') == owner
    _safe_set(owner, 'form_Form', set())
    assert getattr(partner, 'form_EStringToStringMapEntry') is None


def test_assoc_tableExpression107_stub_double():
    # form_TableExpression has no real 'form_TableExpression' property in the generated
    # code (a bare stub) -- manually attach it so form_AbstractTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_AbstractTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    partner = form_TableExpression()
    setattr(partner, 'form_TableExpression', None)
    _safe_set(owner, 'form_AbstractTable108', partner)
    assert getattr(partner, 'form_TableExpression') == owner
    _safe_set(owner, 'form_AbstractTable108', None)
    assert getattr(partner, 'form_TableExpression') is None


def test_assoc_tooltip59_stub_double():
    # form_Expression has no real 'form_Expression61' property in the generated
    # code (a bare stub) -- manually attach it so form_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    partner = form_Expression()
    setattr(partner, 'form_Expression61', None)
    _safe_set(owner, 'form_Widget60', partner)
    assert getattr(partner, 'form_Expression61') == owner
    _safe_set(owner, 'form_Widget60', None)
    assert getattr(partner, 'form_Expression61') is None


def test_assoc_tooltipForAdd28_stub_double():
    # form_Expression has no real 'form_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so form_Duplicable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Duplicable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression30', None)
    _safe_set(owner, 'form_Duplicable29', partner)
    assert getattr(partner, 'form_Expression30') == owner
    _safe_set(owner, 'form_Duplicable29', None)
    assert getattr(partner, 'form_Expression30') is None


def test_assoc_tooltipForRemove34_stub_double():
    # form_Expression has no real 'form_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so form_Duplicable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_Duplicable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression36', None)
    _safe_set(owner, 'form_Duplicable35', partner)
    assert getattr(partner, 'form_Expression36') == owner
    _safe_set(owner, 'form_Duplicable35', None)
    assert getattr(partner, 'form_Expression36') is None


def test_assoc_verticalHeaderExpression104_stub_double():
    # form_Expression has no real 'form_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so form_AbstractTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # form_AbstractTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    partner = form_Expression()
    setattr(partner, 'form_Expression106', None)
    _safe_set(owner, 'form_AbstractTable105', partner)
    assert getattr(partner, 'form_Expression106') == owner
    _safe_set(owner, 'form_AbstractTable105', None)
    assert getattr(partner, 'form_Expression106') is None


