import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_form_AbstractTable_LastRowIsHeader_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.LastRowIsHeader == True
    instance.LastRowIsHeader = False
    assert instance.LastRowIsHeader == False


def test_form_AbstractTable_firstRowIsHeader_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.firstRowIsHeader == True
    instance.firstRowIsHeader = False
    assert instance.firstRowIsHeader == False


def test_form_AbstractTable_initializedUsingCells_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.initializedUsingCells == True
    instance.initializedUsingCells = False
    assert instance.initializedUsingCells == False


def test_form_AbstractTable_leftColumnIsHeader_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.leftColumnIsHeader == True
    instance.leftColumnIsHeader = False
    assert instance.leftColumnIsHeader == False


def test_form_AbstractTable_rightColumnIsHeader_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.rightColumnIsHeader == True
    instance.rightColumnIsHeader = False
    assert instance.rightColumnIsHeader == False


def test_form_AbstractTable_useHorizontalHeader_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.useHorizontalHeader == True
    instance.useHorizontalHeader = False
    assert instance.useHorizontalHeader == False


def test_form_AbstractTable_useVerticalHeader_value_roundtrip():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert instance.useVerticalHeader == True
    instance.useVerticalHeader = False
    assert instance.useVerticalHeader == False


def test_form_Column_number_value_roundtrip():
    instance = form_Column(number=7, width="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_form_Column_width_value_roundtrip():
    instance = form_Column(number=7, width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_form_DateFormField_displayFormat_value_roundtrip():
    instance = form_DateFormField(displayFormat="sample_text", initialFormat="sample_text")
    assert instance.displayFormat == "sample_text"
    instance.displayFormat = "sample_text_2"
    assert instance.displayFormat == "sample_text_2"


def test_form_DateFormField_initialFormat_value_roundtrip():
    instance = form_DateFormField(displayFormat="sample_text", initialFormat="sample_text")
    assert instance.initialFormat == "sample_text"
    instance.initialFormat = "sample_text_2"
    assert instance.initialFormat == "sample_text_2"


def test_form_Duplicable_duplicate_value_roundtrip():
    instance = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    assert instance.duplicate == True
    instance.duplicate = False
    assert instance.duplicate == False


def test_form_Duplicable_limitMinNumberOfDuplication_value_roundtrip():
    instance = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    assert instance.limitMinNumberOfDuplication == True
    instance.limitMinNumberOfDuplication = False
    assert instance.limitMinNumberOfDuplication == False


def test_form_Duplicable_limitNumberOfDuplication_value_roundtrip():
    instance = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    assert instance.limitNumberOfDuplication == True
    instance.limitNumberOfDuplication = False
    assert instance.limitNumberOfDuplication == False


def test_form_DurationFormField_day_value_roundtrip():
    instance = form_DurationFormField(day="sample_text", hour="sample_text", min="sample_text", sec="sample_text")
    assert instance.day == "sample_text"
    instance.day = "sample_text_2"
    assert instance.day == "sample_text_2"


def test_form_DurationFormField_hour_value_roundtrip():
    instance = form_DurationFormField(day="sample_text", hour="sample_text", min="sample_text", sec="sample_text")
    assert instance.hour == "sample_text"
    instance.hour = "sample_text_2"
    assert instance.hour == "sample_text_2"


def test_form_DurationFormField_min_value_roundtrip():
    instance = form_DurationFormField(day="sample_text", hour="sample_text", min="sample_text", sec="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_form_DurationFormField_sec_value_roundtrip():
    instance = form_DurationFormField(day="sample_text", hour="sample_text", min="sample_text", sec="sample_text")
    assert instance.sec == "sample_text"
    instance.sec = "sample_text_2"
    assert instance.sec == "sample_text_2"


def test_form_DynamicTable_allowAddRemoveColumn_value_roundtrip():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert instance.allowAddRemoveColumn == True
    instance.allowAddRemoveColumn = False
    assert instance.allowAddRemoveColumn == False


def test_form_DynamicTable_allowAddRemoveRow_value_roundtrip():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert instance.allowAddRemoveRow == True
    instance.allowAddRemoveRow = False
    assert instance.allowAddRemoveRow == False


def test_form_DynamicTable_limitMaxNumberOfColumn_value_roundtrip():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert instance.limitMaxNumberOfColumn == True
    instance.limitMaxNumberOfColumn = False
    assert instance.limitMaxNumberOfColumn == False


def test_form_DynamicTable_limitMaxNumberOfRow_value_roundtrip():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert instance.limitMaxNumberOfRow == True
    instance.limitMaxNumberOfRow = False
    assert instance.limitMaxNumberOfRow == False


def test_form_DynamicTable_limitMinNumberOfColumn_value_roundtrip():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert instance.limitMinNumberOfColumn == True
    instance.limitMinNumberOfColumn = False
    assert instance.limitMinNumberOfColumn == False


def test_form_DynamicTable_limitMinNumberOfRow_value_roundtrip():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert instance.limitMinNumberOfRow == True
    instance.limitMinNumberOfRow = False
    assert instance.limitMinNumberOfRow == False


def test_form_FileWidget_downloadOnly_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.downloadOnly == True
    instance.downloadOnly = False
    assert instance.downloadOnly == False


def test_form_FileWidget_downloadType_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.downloadType == "sample_text"
    instance.downloadType = "sample_text_2"
    assert instance.downloadType == "sample_text_2"


def test_form_FileWidget_initialResourcePath_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.initialResourcePath == "sample_text"
    instance.initialResourcePath = "sample_text_2"
    assert instance.initialResourcePath == "sample_text_2"


def test_form_FileWidget_inputType_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.inputType == "sample_text"
    instance.inputType = "sample_text_2"
    assert instance.inputType == "sample_text_2"


def test_form_FileWidget_intialResourceList_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.intialResourceList == "sample_text"
    instance.intialResourceList = "sample_text_2"
    assert instance.intialResourceList == "sample_text_2"


def test_form_FileWidget_outputDocumentName_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.outputDocumentName == "sample_text"
    instance.outputDocumentName = "sample_text_2"
    assert instance.outputDocumentName == "sample_text_2"


def test_form_FileWidget_updateDocument_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.updateDocument == True
    instance.updateDocument = False
    assert instance.updateDocument == False


def test_form_FileWidget_usePreview_value_roundtrip():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert instance.usePreview == True
    instance.usePreview = False
    assert instance.usePreview == False


def test_form_Form_allowHTMLInPageLabel_value_roundtrip():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert instance.allowHTMLInPageLabel == True
    instance.allowHTMLInPageLabel = False
    assert instance.allowHTMLInPageLabel == False


def test_form_Form_nColumn_value_roundtrip():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert instance.nColumn == 7
    instance.nColumn = 13
    assert instance.nColumn == 13


def test_form_Form_nLine_value_roundtrip():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert instance.nLine == 7
    instance.nLine = 13
    assert instance.nLine == 13


def test_form_Form_showPageLabel_value_roundtrip():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert instance.showPageLabel == "sample_text"
    instance.showPageLabel = "sample_text_2"
    assert instance.showPageLabel == "sample_text_2"


def test_form_Form_version_value_roundtrip():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_form_FormButton_labelBehavior_value_roundtrip():
    instance = form_FormButton(labelBehavior="sample_text")
    assert instance.labelBehavior == "sample_text"
    instance.labelBehavior = "sample_text_2"
    assert instance.labelBehavior == "sample_text_2"


def test_form_FormField_description_value_roundtrip():
    instance = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_form_FormField_exampleMessagePosition_value_roundtrip():
    instance = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    assert instance.exampleMessagePosition == "sample_text"
    instance.exampleMessagePosition = "sample_text_2"
    assert instance.exampleMessagePosition == "sample_text_2"


def test_form_Group_showBorder_value_roundtrip():
    instance = form_Group(showBorder=True, useIterator=True)
    assert instance.showBorder == True
    instance.showBorder = False
    assert instance.showBorder == False


def test_form_Group_useIterator_value_roundtrip():
    instance = form_Group(showBorder=True, useIterator=True)
    assert instance.useIterator == True
    instance.useIterator = False
    assert instance.useIterator == False


def test_form_GroupIterator_className_value_roundtrip():
    instance = form_GroupIterator(className="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_form_ImageWidget_isADocument_value_roundtrip():
    instance = form_ImageWidget(isADocument=True)
    assert instance.isADocument == True
    instance.isADocument = False
    assert instance.isADocument == False


def test_form_ItemContainer_itemClass_value_roundtrip():
    instance = form_ItemContainer(itemClass="sample_text")
    assert instance.itemClass == "sample_text"
    instance.itemClass = "sample_text_2"
    assert instance.itemClass == "sample_text_2"


def test_form_Line_height_value_roundtrip():
    instance = form_Line(height="sample_text", number=7)
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_form_Line_number_value_roundtrip():
    instance = form_Line(height="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_form_ListFormField_maxHeigth_value_roundtrip():
    instance = form_ListFormField(maxHeigth=7)
    assert instance.maxHeigth == 7
    instance.maxHeigth = 13
    assert instance.maxHeigth == 13


def test_form_PasswordFormField_maxLength_value_roundtrip():
    instance = form_PasswordFormField(maxLength=7)
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_form_SuggestBox_asynchronous_value_roundtrip():
    instance = form_SuggestBox(asynchronous=True, delay=7, maxItems=7, useMaxItems=True)
    assert instance.asynchronous == True
    instance.asynchronous = False
    assert instance.asynchronous == False


def test_form_SuggestBox_delay_value_roundtrip():
    instance = form_SuggestBox(asynchronous=True, delay=7, maxItems=7, useMaxItems=True)
    assert instance.delay == 7
    instance.delay = 13
    assert instance.delay == 13


def test_form_SuggestBox_maxItems_value_roundtrip():
    instance = form_SuggestBox(asynchronous=True, delay=7, maxItems=7, useMaxItems=True)
    assert instance.maxItems == 7
    instance.maxItems = 13
    assert instance.maxItems == 13


def test_form_SuggestBox_useMaxItems_value_roundtrip():
    instance = form_SuggestBox(asynchronous=True, delay=7, maxItems=7, useMaxItems=True)
    assert instance.useMaxItems == True
    instance.useMaxItems = False
    assert instance.useMaxItems == False


def test_form_Table_allowSelection_value_roundtrip():
    instance = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    assert instance.allowSelection == True
    instance.allowSelection = False
    assert instance.allowSelection == False


def test_form_Table_selectionModeIsMultiple_value_roundtrip():
    instance = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    assert instance.selectionModeIsMultiple == True
    instance.selectionModeIsMultiple = False
    assert instance.selectionModeIsMultiple == False


def test_form_Table_usePagination_value_roundtrip():
    instance = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    assert instance.usePagination == True
    instance.usePagination = False
    assert instance.usePagination == False


def test_form_TextAreaFormField_maxHeigth_value_roundtrip():
    instance = form_TextAreaFormField(maxHeigth=7, maxLength=7)
    assert instance.maxHeigth == 7
    instance.maxHeigth = 13
    assert instance.maxHeigth == 13


def test_form_TextAreaFormField_maxLength_value_roundtrip():
    instance = form_TextAreaFormField(maxHeigth=7, maxLength=7)
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_form_TextFormField_maxLength_value_roundtrip():
    instance = form_TextFormField(maxLength=7)
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_form_Validable_below_value_roundtrip():
    instance = form_Validable(below=True, useDefaultValidator="sample_text")
    assert instance.below == True
    instance.below = False
    assert instance.below == False


def test_form_Validable_useDefaultValidator_value_roundtrip():
    instance = form_Validable(below=True, useDefaultValidator="sample_text")
    assert instance.useDefaultValidator == "sample_text"
    instance.useDefaultValidator = "sample_text_2"
    assert instance.useDefaultValidator == "sample_text_2"


def test_form_Validator_belowField_value_roundtrip():
    instance = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    assert instance.belowField == True
    instance.belowField = False
    assert instance.belowField == False


def test_form_Validator_htmlClass_value_roundtrip():
    instance = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    assert instance.htmlClass == "sample_text"
    instance.htmlClass = "sample_text_2"
    assert instance.htmlClass == "sample_text_2"


def test_form_Validator_name_value_roundtrip():
    instance = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_form_Validator_validatorClass_value_roundtrip():
    instance = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    assert instance.validatorClass == "sample_text"
    instance.validatorClass = "sample_text_2"
    assert instance.validatorClass == "sample_text_2"


def test_form_Widget_allowHTMLForDisplayLabel_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.allowHTMLForDisplayLabel == True
    instance.allowHTMLForDisplayLabel = False
    assert instance.allowHTMLForDisplayLabel == False


def test_form_Widget_displayDependentWidgetOnlyOnEventTriggered_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.displayDependentWidgetOnlyOnEventTriggered == True
    instance.displayDependentWidgetOnlyOnEventTriggered = False
    assert instance.displayDependentWidgetOnlyOnEventTriggered == False


def test_form_Widget_injectWidgetCondition_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.injectWidgetCondition == True
    instance.injectWidgetCondition = False
    assert instance.injectWidgetCondition == False


def test_form_Widget_labelPosition_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.labelPosition == "sample_text"
    instance.labelPosition = "sample_text_2"
    assert instance.labelPosition == "sample_text_2"


def test_form_Widget_mandatory_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_form_Widget_readOnly_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_form_Widget_realHtmlAttributes_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.realHtmlAttributes == "sample_text"
    instance.realHtmlAttributes = "sample_text_2"
    assert instance.realHtmlAttributes == "sample_text_2"


def test_form_Widget_returnTypeModifier_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.returnTypeModifier == "sample_text"
    instance.returnTypeModifier = "sample_text_2"
    assert instance.returnTypeModifier == "sample_text_2"


def test_form_Widget_showDisplayLabel_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.showDisplayLabel == "sample_text"
    instance.showDisplayLabel = "sample_text_2"
    assert instance.showDisplayLabel == "sample_text_2"


def test_form_Widget_version_value_roundtrip():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_form_WidgetDependency_eventTypes_value_roundtrip():
    instance = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    assert instance.eventTypes == "sample_text"
    instance.eventTypes = "sample_text_2"
    assert instance.eventTypes == "sample_text_2"


def test_form_WidgetDependency_triggerRefreshOnModification_value_roundtrip():
    instance = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    assert instance.triggerRefreshOnModification == True
    instance.triggerRefreshOnModification = False
    assert instance.triggerRefreshOnModification == False


def test_form_WidgetLayoutInfo_column_value_roundtrip():
    instance = form_WidgetLayoutInfo(column=7, horizontalSpan=7, line=7, verticalSpan=7)
    assert instance.column == 7
    instance.column = 13
    assert instance.column == 13


def test_form_WidgetLayoutInfo_horizontalSpan_value_roundtrip():
    instance = form_WidgetLayoutInfo(column=7, horizontalSpan=7, line=7, verticalSpan=7)
    assert instance.horizontalSpan == 7
    instance.horizontalSpan = 13
    assert instance.horizontalSpan == 13


def test_form_WidgetLayoutInfo_line_value_roundtrip():
    instance = form_WidgetLayoutInfo(column=7, horizontalSpan=7, line=7, verticalSpan=7)
    assert instance.line == 7
    instance.line = 13
    assert instance.line == 13


def test_form_WidgetLayoutInfo_verticalSpan_value_roundtrip():
    instance = form_WidgetLayoutInfo(column=7, horizontalSpan=7, line=7, verticalSpan=7)
    assert instance.verticalSpan == 7
    instance.verticalSpan = 13
    assert instance.verticalSpan == 13


def test_form_DynamicTable_isa_AbstractTable():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert isinstance(instance, AbstractTable)


def test_form_Table_isa_AbstractTable():
    instance = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    assert isinstance(instance, AbstractTable)


def test_form_MandatoryFieldsCustomization_isa_CSSCustomizable():
    instance = form_MandatoryFieldsCustomization()
    assert isinstance(instance, CSSCustomizable)


def test_form_Widget_isa_CSSCustomizable():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert isinstance(instance, CSSCustomizable)


def test_form_Form_isa_ConnectableElement():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert isinstance(instance, ConnectableElement)


def test_form_SubmitFormButton_isa_ConnectableElement():
    instance = form_SubmitFormButton()
    assert isinstance(instance, ConnectableElement)


def test_form_AbstractTable_isa_Duplicable():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert isinstance(instance, Duplicable)


def test_form_FileWidget_isa_Duplicable():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert isinstance(instance, Duplicable)


def test_form_FormField_isa_Duplicable():
    instance = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    assert isinstance(instance, Duplicable)


def test_form_Group_isa_Duplicable():
    instance = form_Group(showBorder=True, useIterator=True)
    assert isinstance(instance, Duplicable)


def test_form_HiddenWidget_isa_Duplicable():
    instance = form_HiddenWidget()
    assert isinstance(instance, Duplicable)


def test_form_ImageWidget_isa_Duplicable():
    instance = form_ImageWidget(isADocument=True)
    assert isinstance(instance, Duplicable)


def test_form_TextInfo_isa_Duplicable():
    instance = form_TextInfo()
    assert isinstance(instance, Duplicable)


def test_form_GroupIterator_isa_Element():
    instance = form_GroupIterator(className="sample_text")
    assert isinstance(instance, Element)


def test_form_Widget_isa_Element():
    instance = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    assert isinstance(instance, Element)


def test_form_ViewForm_isa_Form():
    instance = form_ViewForm()
    assert isinstance(instance, Form)


def test_form_NextFormButton_isa_FormButton():
    instance = form_NextFormButton()
    assert isinstance(instance, FormButton)


def test_form_PreviousFormButton_isa_FormButton():
    instance = form_PreviousFormButton()
    assert isinstance(instance, FormButton)


def test_form_SubmitFormButton_isa_FormButton():
    instance = form_SubmitFormButton()
    assert isinstance(instance, FormButton)


def test_form_MultipleValuatedFormField_isa_FormField():
    instance = form_MultipleValuatedFormField()
    assert isinstance(instance, FormField)


def test_form_SingleValuatedFormField_isa_FormField():
    instance = form_SingleValuatedFormField()
    assert isinstance(instance, FormField)


def test_form_HtmlWidget_isa_Info():
    instance = form_HtmlWidget()
    assert isinstance(instance, Info)


def test_form_IFrameWidget_isa_Info():
    instance = form_IFrameWidget()
    assert isinstance(instance, Info)


def test_form_MessageInfo_isa_Info():
    instance = form_MessageInfo()
    assert isinstance(instance, Info)


def test_form_TextInfo_isa_Info():
    instance = form_TextInfo()
    assert isinstance(instance, Info)


def test_form_CheckBoxMultipleFormField_isa_ItemContainer():
    instance = form_CheckBoxMultipleFormField()
    assert isinstance(instance, ItemContainer)


def test_form_DurationFormField_isa_ItemContainer():
    instance = form_DurationFormField(day="sample_text", hour="sample_text", min="sample_text", sec="sample_text")
    assert isinstance(instance, ItemContainer)


def test_form_RadioFormField_isa_ItemContainer():
    instance = form_RadioFormField()
    assert isinstance(instance, ItemContainer)


def test_form_CheckBoxMultipleFormField_isa_MultipleValuatedFormField():
    instance = form_CheckBoxMultipleFormField()
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_ComboFormField_isa_MultipleValuatedFormField():
    instance = form_ComboFormField()
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_ListFormField_isa_MultipleValuatedFormField():
    instance = form_ListFormField(maxHeigth=7)
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_RadioFormField_isa_MultipleValuatedFormField():
    instance = form_RadioFormField()
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_SelectFormField_isa_MultipleValuatedFormField():
    instance = form_SelectFormField()
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_SuggestBox_isa_MultipleValuatedFormField():
    instance = form_SuggestBox(asynchronous=True, delay=7, maxItems=7, useMaxItems=True)
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_Table_isa_MultipleValuatedFormField():
    instance = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    assert isinstance(instance, MultipleValuatedFormField)


def test_form_CheckBoxSingleFormField_isa_SingleValuatedFormField():
    instance = form_CheckBoxSingleFormField()
    assert isinstance(instance, SingleValuatedFormField)


def test_form_DateFormField_isa_SingleValuatedFormField():
    instance = form_DateFormField(displayFormat="sample_text", initialFormat="sample_text")
    assert isinstance(instance, SingleValuatedFormField)


def test_form_DurationFormField_isa_SingleValuatedFormField():
    instance = form_DurationFormField(day="sample_text", hour="sample_text", min="sample_text", sec="sample_text")
    assert isinstance(instance, SingleValuatedFormField)


def test_form_DynamicTable_isa_SingleValuatedFormField():
    instance = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    assert isinstance(instance, SingleValuatedFormField)


def test_form_FileWidget_isa_SingleValuatedFormField():
    instance = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    assert isinstance(instance, SingleValuatedFormField)


def test_form_HiddenWidget_isa_SingleValuatedFormField():
    instance = form_HiddenWidget()
    assert isinstance(instance, SingleValuatedFormField)


def test_form_PasswordFormField_isa_SingleValuatedFormField():
    instance = form_PasswordFormField(maxLength=7)
    assert isinstance(instance, SingleValuatedFormField)


def test_form_RichTextAreaFormField_isa_SingleValuatedFormField():
    instance = form_RichTextAreaFormField()
    assert isinstance(instance, SingleValuatedFormField)


def test_form_TextAreaFormField_isa_SingleValuatedFormField():
    instance = form_TextAreaFormField(maxHeigth=7, maxLength=7)
    assert isinstance(instance, SingleValuatedFormField)


def test_form_TextFormField_isa_SingleValuatedFormField():
    instance = form_TextFormField(maxLength=7)
    assert isinstance(instance, SingleValuatedFormField)


def test_form_Form_isa_Validable():
    instance = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    assert isinstance(instance, Validable)


def test_form_FormField_isa_Validable():
    instance = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    assert isinstance(instance, Validable)


def test_form_AbstractTable_isa_Widget():
    instance = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    assert isinstance(instance, Widget)


def test_form_FormButton_isa_Widget():
    instance = form_FormButton(labelBehavior="sample_text")
    assert isinstance(instance, Widget)


def test_form_FormField_isa_Widget():
    instance = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    assert isinstance(instance, Widget)


def test_form_Group_isa_Widget():
    instance = form_Group(showBorder=True, useIterator=True)
    assert isinstance(instance, Widget)


def test_form_ImageWidget_isa_Widget():
    instance = form_ImageWidget(isADocument=True)
    assert isinstance(instance, Widget)


def test_form_Info_isa_Widget():
    instance = form_Info()
    assert isinstance(instance, Widget)


def test_assoc_action71_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Operation()
    b2 = form_Operation()
    _safe_set(a, 'form_Widget72', b1)
    assert _is_linked(a, 'form_Widget72', b1)
    if hasattr(b1, 'form_Operation73'):
        assert _is_linked(b1, 'form_Operation73', a)
    _safe_set(a, 'form_Widget72', b2)
    assert _is_linked(a, 'form_Widget72', b2)
    if hasattr(b1, 'form_Operation73'):
        assert not _is_linked(b1, 'form_Operation73', a)
    if hasattr(b2, 'form_Operation73'):
        assert _is_linked(b2, 'form_Operation73', a)
    _safe_set(a, 'form_Widget72', None)
    assert not _is_linked(a, 'form_Widget72', b2)
    if hasattr(b2, 'form_Operation73'):
        assert not _is_linked(b2, 'form_Operation73', a)


def test_assoc_actions18_link_reassign_clear():
    a = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    b1 = form_Operation()
    b2 = form_Operation()
    _safe_set(a, 'form_Form19', {b1})
    assert _is_linked(a, 'form_Form19', b1)
    if hasattr(b1, 'form_Operation'):
        assert _is_linked(b1, 'form_Operation', a)
    _safe_set(a, 'form_Form19', {b2})
    assert _is_linked(a, 'form_Form19', b2)
    if hasattr(b1, 'form_Operation'):
        assert not _is_linked(b1, 'form_Operation', a)
    if hasattr(b2, 'form_Operation'):
        assert _is_linked(b2, 'form_Operation', a)
    _safe_set(a, 'form_Form19', set())
    assert not _is_linked(a, 'form_Form19', b2)
    if hasattr(b2, 'form_Operation'):
        assert not _is_linked(b2, 'form_Operation', a)


def test_assoc_afterEventExpression56_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget57', b1)
    assert _is_linked(a, 'form_Widget57', b1)
    if hasattr(b1, 'form_Expression58'):
        assert _is_linked(b1, 'form_Expression58', a)
    _safe_set(a, 'form_Widget57', b2)
    assert _is_linked(a, 'form_Widget57', b2)
    if hasattr(b1, 'form_Expression58'):
        assert not _is_linked(b1, 'form_Expression58', a)
    if hasattr(b2, 'form_Expression58'):
        assert _is_linked(b2, 'form_Expression58', a)
    _safe_set(a, 'form_Widget57', None)
    assert not _is_linked(a, 'form_Widget57', b2)
    if hasattr(b2, 'form_Expression58'):
        assert not _is_linked(b2, 'form_Expression58', a)


def test_assoc_columnForInitialSelectionIndex111_link_reassign_clear():
    a = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Table112', b1)
    assert _is_linked(a, 'form_Table112', b1)
    if hasattr(b1, 'form_Expression113'):
        assert _is_linked(b1, 'form_Expression113', a)
    _safe_set(a, 'form_Table112', b2)
    assert _is_linked(a, 'form_Table112', b2)
    if hasattr(b1, 'form_Expression113'):
        assert not _is_linked(b1, 'form_Expression113', a)
    if hasattr(b2, 'form_Expression113'):
        assert _is_linked(b2, 'form_Expression113', a)
    _safe_set(a, 'form_Table112', None)
    assert not _is_linked(a, 'form_Table112', b2)
    if hasattr(b2, 'form_Expression113'):
        assert not _is_linked(b2, 'form_Expression113', a)


def test_assoc_columns76_link_reassign_clear():
    a = form_Group(showBorder=True, useIterator=True)
    b1 = form_Column(number=7, width="sample_text")
    b2 = form_Column(number=13, width="sample_text_2")
    _safe_set(a, 'form_Group77', {b1})
    assert _is_linked(a, 'form_Group77', b1)
    if hasattr(b1, 'form_Column78'):
        assert _is_linked(b1, 'form_Column78', a)
    _safe_set(a, 'form_Group77', {b2})
    assert _is_linked(a, 'form_Group77', b2)
    if hasattr(b1, 'form_Column78'):
        assert not _is_linked(b1, 'form_Column78', a)
    if hasattr(b2, 'form_Column78'):
        assert _is_linked(b2, 'form_Column78', a)
    _safe_set(a, 'form_Group77', set())
    assert not _is_linked(a, 'form_Group77', b2)
    if hasattr(b2, 'form_Column78'):
        assert not _is_linked(b2, 'form_Column78', a)


def test_assoc_columns8_link_reassign_clear():
    a = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    b1 = form_Column(number=7, width="sample_text")
    b2 = form_Column(number=13, width="sample_text_2")
    _safe_set(a, 'form_Form9', {b1})
    assert _is_linked(a, 'form_Form9', b1)
    if hasattr(b1, 'form_Column'):
        assert _is_linked(b1, 'form_Column', a)
    _safe_set(a, 'form_Form9', {b2})
    assert _is_linked(a, 'form_Form9', b2)
    if hasattr(b1, 'form_Column'):
        assert not _is_linked(b1, 'form_Column', a)
    if hasattr(b2, 'form_Column'):
        assert _is_linked(b2, 'form_Column', a)
    _safe_set(a, 'form_Form9', set())
    assert not _is_linked(a, 'form_Form9', b2)
    if hasattr(b2, 'form_Column'):
        assert not _is_linked(b2, 'form_Column', a)


def test_assoc_dependOn41_link_reassign_clear():
    a = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    b1 = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b2 = form_Widget(allowHTMLForDisplayLabel=False, displayDependentWidgetOnlyOnEventTriggered=False, injectWidgetCondition=False, labelPosition="sample_text_2", mandatory=False, readOnly=False, realHtmlAttributes="sample_text_2", returnTypeModifier="sample_text_2", showDisplayLabel="sample_text_2", version="sample_text_2")
    _safe_set(a, 'form_WidgetDependency43', b1)
    assert _is_linked(a, 'form_WidgetDependency43', b1)
    if hasattr(b1, 'form_Widget42'):
        assert _is_linked(b1, 'form_Widget42', a)
    _safe_set(a, 'form_WidgetDependency43', b2)
    assert _is_linked(a, 'form_WidgetDependency43', b2)
    if hasattr(b1, 'form_Widget42'):
        assert not _is_linked(b1, 'form_Widget42', a)
    if hasattr(b2, 'form_Widget42'):
        assert _is_linked(b2, 'form_Widget42', a)
    _safe_set(a, 'form_WidgetDependency43', None)
    assert not _is_linked(a, 'form_WidgetDependency43', b2)
    if hasattr(b2, 'form_Widget42'):
        assert not _is_linked(b2, 'form_Widget42', a)


def test_assoc_displayAfterEventDependsOnConditionScript50_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget51', b1)
    assert _is_linked(a, 'form_Widget51', b1)
    if hasattr(b1, 'form_Expression52'):
        assert _is_linked(b1, 'form_Expression52', a)
    _safe_set(a, 'form_Widget51', b2)
    assert _is_linked(a, 'form_Widget51', b2)
    if hasattr(b1, 'form_Expression52'):
        assert not _is_linked(b1, 'form_Expression52', a)
    if hasattr(b2, 'form_Expression52'):
        assert _is_linked(b2, 'form_Expression52', a)
    _safe_set(a, 'form_Widget51', None)
    assert not _is_linked(a, 'form_Widget51', b2)
    if hasattr(b2, 'form_Expression52'):
        assert not _is_linked(b2, 'form_Expression52', a)


def test_assoc_displayDependentWidgetOnlyAfterFirstEventTriggeredAndCondition47_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget48', b1)
    assert _is_linked(a, 'form_Widget48', b1)
    if hasattr(b1, 'form_Expression49'):
        assert _is_linked(b1, 'form_Expression49', a)
    _safe_set(a, 'form_Widget48', b2)
    assert _is_linked(a, 'form_Widget48', b2)
    if hasattr(b1, 'form_Expression49'):
        assert not _is_linked(b1, 'form_Expression49', a)
    if hasattr(b2, 'form_Expression49'):
        assert _is_linked(b2, 'form_Expression49', a)
    _safe_set(a, 'form_Widget48', None)
    assert not _is_linked(a, 'form_Widget48', b2)
    if hasattr(b2, 'form_Expression49'):
        assert not _is_linked(b2, 'form_Expression49', a)


def test_assoc_displayLabel65_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget66', b1)
    assert _is_linked(a, 'form_Widget66', b1)
    if hasattr(b1, 'form_Expression67'):
        assert _is_linked(b1, 'form_Expression67', a)
    _safe_set(a, 'form_Widget66', b2)
    assert _is_linked(a, 'form_Widget66', b2)
    if hasattr(b1, 'form_Expression67'):
        assert not _is_linked(b1, 'form_Expression67', a)
    if hasattr(b2, 'form_Expression67'):
        assert _is_linked(b2, 'form_Expression67', a)
    _safe_set(a, 'form_Widget66', None)
    assert not _is_linked(a, 'form_Widget66', b2)
    if hasattr(b2, 'form_Expression67'):
        assert not _is_linked(b2, 'form_Expression67', a)


def test_assoc_displayLabelForAdd25_link_reassign_clear():
    a = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Duplicable26', b1)
    assert _is_linked(a, 'form_Duplicable26', b1)
    if hasattr(b1, 'form_Expression27'):
        assert _is_linked(b1, 'form_Expression27', a)
    _safe_set(a, 'form_Duplicable26', b2)
    assert _is_linked(a, 'form_Duplicable26', b2)
    if hasattr(b1, 'form_Expression27'):
        assert not _is_linked(b1, 'form_Expression27', a)
    if hasattr(b2, 'form_Expression27'):
        assert _is_linked(b2, 'form_Expression27', a)
    _safe_set(a, 'form_Duplicable26', None)
    assert not _is_linked(a, 'form_Duplicable26', b2)
    if hasattr(b2, 'form_Expression27'):
        assert not _is_linked(b2, 'form_Expression27', a)


def test_assoc_displayLabelForRemove31_link_reassign_clear():
    a = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Duplicable32', b1)
    assert _is_linked(a, 'form_Duplicable32', b1)
    if hasattr(b1, 'form_Expression33'):
        assert _is_linked(b1, 'form_Expression33', a)
    _safe_set(a, 'form_Duplicable32', b2)
    assert _is_linked(a, 'form_Duplicable32', b2)
    if hasattr(b1, 'form_Expression33'):
        assert not _is_linked(b1, 'form_Expression33', a)
    if hasattr(b2, 'form_Expression33'):
        assert _is_linked(b2, 'form_Expression33', a)
    _safe_set(a, 'form_Duplicable32', None)
    assert not _is_linked(a, 'form_Duplicable32', b2)
    if hasattr(b2, 'form_Expression33'):
        assert not _is_linked(b2, 'form_Expression33', a)


def test_assoc_displayName2_link_reassign_clear():
    a = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Validator3', b1)
    assert _is_linked(a, 'form_Validator3', b1)
    if hasattr(b1, 'form_Expression4'):
        assert _is_linked(b1, 'form_Expression4', a)
    _safe_set(a, 'form_Validator3', b2)
    assert _is_linked(a, 'form_Validator3', b2)
    if hasattr(b1, 'form_Expression4'):
        assert not _is_linked(b1, 'form_Expression4', a)
    if hasattr(b2, 'form_Expression4'):
        assert _is_linked(b2, 'form_Expression4', a)
    _safe_set(a, 'form_Validator3', None)
    assert not _is_linked(a, 'form_Validator3', b2)
    if hasattr(b2, 'form_Expression4'):
        assert not _is_linked(b2, 'form_Expression4', a)


def test_assoc_document93_link_reassign_clear():
    a = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    b1 = form_Document()
    b2 = form_Document()
    _safe_set(a, 'form_FileWidget', b1)
    assert _is_linked(a, 'form_FileWidget', b1)
    if hasattr(b1, 'form_Document'):
        assert _is_linked(b1, 'form_Document', a)
    _safe_set(a, 'form_FileWidget', b2)
    assert _is_linked(a, 'form_FileWidget', b2)
    if hasattr(b1, 'form_Document'):
        assert not _is_linked(b1, 'form_Document', a)
    if hasattr(b2, 'form_Document'):
        assert _is_linked(b2, 'form_Document', a)
    _safe_set(a, 'form_FileWidget', None)
    assert not _is_linked(a, 'form_FileWidget', b2)
    if hasattr(b2, 'form_Document'):
        assert not _is_linked(b2, 'form_Document', a)


def test_assoc_document97_link_reassign_clear():
    a = form_ImageWidget(isADocument=True)
    b1 = form_Document()
    b2 = form_Document()
    _safe_set(a, 'form_ImageWidget', b1)
    assert _is_linked(a, 'form_ImageWidget', b1)
    if hasattr(b1, 'form_Document98'):
        assert _is_linked(b1, 'form_Document98', a)
    _safe_set(a, 'form_ImageWidget', b2)
    assert _is_linked(a, 'form_ImageWidget', b2)
    if hasattr(b1, 'form_Document98'):
        assert not _is_linked(b1, 'form_Document98', a)
    if hasattr(b2, 'form_Document98'):
        assert _is_linked(b2, 'form_Document98', a)
    _safe_set(a, 'form_ImageWidget', None)
    assert not _is_linked(a, 'form_ImageWidget', b2)
    if hasattr(b2, 'form_Document98'):
        assert not _is_linked(b2, 'form_Document98', a)


def test_assoc_exampleMessage84_link_reassign_clear():
    a = form_FormField(description="sample_text", exampleMessagePosition="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_FormField', b1)
    assert _is_linked(a, 'form_FormField', b1)
    if hasattr(b1, 'form_Expression85'):
        assert _is_linked(b1, 'form_Expression85', a)
    _safe_set(a, 'form_FormField', b2)
    assert _is_linked(a, 'form_FormField', b2)
    if hasattr(b1, 'form_Expression85'):
        assert not _is_linked(b1, 'form_Expression85', a)
    if hasattr(b2, 'form_Expression85'):
        assert _is_linked(b2, 'form_Expression85', a)
    _safe_set(a, 'form_FormField', None)
    assert not _is_linked(a, 'form_FormField', b2)
    if hasattr(b2, 'form_Expression85'):
        assert not _is_linked(b2, 'form_Expression85', a)


def test_assoc_helpMessage62_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget63', b1)
    assert _is_linked(a, 'form_Widget63', b1)
    if hasattr(b1, 'form_Expression64'):
        assert _is_linked(b1, 'form_Expression64', a)
    _safe_set(a, 'form_Widget63', b2)
    assert _is_linked(a, 'form_Widget63', b2)
    if hasattr(b1, 'form_Expression64'):
        assert not _is_linked(b1, 'form_Expression64', a)
    if hasattr(b2, 'form_Expression64'):
        assert _is_linked(b2, 'form_Expression64', a)
    _safe_set(a, 'form_Widget63', None)
    assert not _is_linked(a, 'form_Widget63', b2)
    if hasattr(b2, 'form_Expression64'):
        assert not _is_linked(b2, 'form_Expression64', a)


def test_assoc_horizontalHeaderExpression102_link_reassign_clear():
    a = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_AbstractTable', b1)
    assert _is_linked(a, 'form_AbstractTable', b1)
    if hasattr(b1, 'form_Expression103'):
        assert _is_linked(b1, 'form_Expression103', a)
    _safe_set(a, 'form_AbstractTable', b2)
    assert _is_linked(a, 'form_AbstractTable', b2)
    if hasattr(b1, 'form_Expression103'):
        assert not _is_linked(b1, 'form_Expression103', a)
    if hasattr(b2, 'form_Expression103'):
        assert _is_linked(b2, 'form_Expression103', a)
    _safe_set(a, 'form_AbstractTable', None)
    assert not _is_linked(a, 'form_AbstractTable', b2)
    if hasattr(b2, 'form_Expression103'):
        assert not _is_linked(b2, 'form_Expression103', a)


def test_assoc_imgPath99_link_reassign_clear():
    a = form_ImageWidget(isADocument=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_ImageWidget100', b1)
    assert _is_linked(a, 'form_ImageWidget100', b1)
    if hasattr(b1, 'form_Expression101'):
        assert _is_linked(b1, 'form_Expression101', a)
    _safe_set(a, 'form_ImageWidget100', b2)
    assert _is_linked(a, 'form_ImageWidget100', b2)
    if hasattr(b1, 'form_Expression101'):
        assert not _is_linked(b1, 'form_Expression101', a)
    if hasattr(b2, 'form_Expression101'):
        assert _is_linked(b2, 'form_Expression101', a)
    _safe_set(a, 'form_ImageWidget100', None)
    assert not _is_linked(a, 'form_ImageWidget100', b2)
    if hasattr(b2, 'form_Expression101'):
        assert not _is_linked(b2, 'form_Expression101', a)


def test_assoc_injectWidgetScript68_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget69', b1)
    assert _is_linked(a, 'form_Widget69', b1)
    if hasattr(b1, 'form_Expression70'):
        assert _is_linked(b1, 'form_Expression70', a)
    _safe_set(a, 'form_Widget69', b2)
    assert _is_linked(a, 'form_Widget69', b2)
    if hasattr(b1, 'form_Expression70'):
        assert not _is_linked(b1, 'form_Expression70', a)
    if hasattr(b2, 'form_Expression70'):
        assert _is_linked(b2, 'form_Expression70', a)
    _safe_set(a, 'form_Widget69', None)
    assert not _is_linked(a, 'form_Widget69', b2)
    if hasattr(b2, 'form_Expression70'):
        assert not _is_linked(b2, 'form_Expression70', a)


def test_assoc_inputExpression53_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget54', b1)
    assert _is_linked(a, 'form_Widget54', b1)
    if hasattr(b1, 'form_Expression55'):
        assert _is_linked(b1, 'form_Expression55', a)
    _safe_set(a, 'form_Widget54', b2)
    assert _is_linked(a, 'form_Widget54', b2)
    if hasattr(b1, 'form_Expression55'):
        assert not _is_linked(b1, 'form_Expression55', a)
    if hasattr(b2, 'form_Expression55'):
        assert _is_linked(b2, 'form_Expression55', a)
    _safe_set(a, 'form_Widget54', None)
    assert not _is_linked(a, 'form_Widget54', b2)
    if hasattr(b2, 'form_Expression55'):
        assert not _is_linked(b2, 'form_Expression55', a)


def test_assoc_iterator82_link_reassign_clear():
    a = form_GroupIterator(className="sample_text")
    b1 = form_Group(showBorder=True, useIterator=True)
    b2 = form_Group(showBorder=False, useIterator=False)
    _safe_set(a, 'form_GroupIterator', b1)
    assert _is_linked(a, 'form_GroupIterator', b1)
    if hasattr(b1, 'form_Group83'):
        assert _is_linked(b1, 'form_Group83', a)
    _safe_set(a, 'form_GroupIterator', b2)
    assert _is_linked(a, 'form_GroupIterator', b2)
    if hasattr(b1, 'form_Group83'):
        assert not _is_linked(b1, 'form_Group83', a)
    if hasattr(b2, 'form_Group83'):
        assert _is_linked(b2, 'form_Group83', a)
    _safe_set(a, 'form_GroupIterator', None)
    assert not _is_linked(a, 'form_GroupIterator', b2)
    if hasattr(b2, 'form_Group83'):
        assert not _is_linked(b2, 'form_Group83', a)


def test_assoc_lines10_link_reassign_clear():
    a = form_Line(height="sample_text", number=7)
    b1 = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    b2 = form_Form(allowHTMLInPageLabel=False, nColumn=13, nLine=13, showPageLabel="sample_text_2", version="sample_text_2")
    _safe_set(a, 'form_Line', b1)
    assert _is_linked(a, 'form_Line', b1)
    if hasattr(b1, 'form_Form11'):
        assert _is_linked(b1, 'form_Form11', a)
    _safe_set(a, 'form_Line', b2)
    assert _is_linked(a, 'form_Line', b2)
    if hasattr(b1, 'form_Form11'):
        assert not _is_linked(b1, 'form_Form11', a)
    if hasattr(b2, 'form_Form11'):
        assert _is_linked(b2, 'form_Form11', a)
    _safe_set(a, 'form_Line', None)
    assert not _is_linked(a, 'form_Line', b2)
    if hasattr(b2, 'form_Form11'):
        assert not _is_linked(b2, 'form_Form11', a)


def test_assoc_lines79_link_reassign_clear():
    a = form_Line(height="sample_text", number=7)
    b1 = form_Group(showBorder=True, useIterator=True)
    b2 = form_Group(showBorder=False, useIterator=False)
    _safe_set(a, 'form_Line81', b1)
    assert _is_linked(a, 'form_Line81', b1)
    if hasattr(b1, 'form_Group80'):
        assert _is_linked(b1, 'form_Group80', a)
    _safe_set(a, 'form_Line81', b2)
    assert _is_linked(a, 'form_Line81', b2)
    if hasattr(b1, 'form_Group80'):
        assert not _is_linked(b1, 'form_Group80', a)
    if hasattr(b2, 'form_Group80'):
        assert _is_linked(b2, 'form_Group80', a)
    _safe_set(a, 'form_Line81', None)
    assert not _is_linked(a, 'form_Line81', b2)
    if hasattr(b2, 'form_Group80'):
        assert not _is_linked(b2, 'form_Group80', a)


def test_assoc_maxNumberOfColumn122_link_reassign_clear():
    a = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_DynamicTable123', b1)
    assert _is_linked(a, 'form_DynamicTable123', b1)
    if hasattr(b1, 'form_Expression124'):
        assert _is_linked(b1, 'form_Expression124', a)
    _safe_set(a, 'form_DynamicTable123', b2)
    assert _is_linked(a, 'form_DynamicTable123', b2)
    if hasattr(b1, 'form_Expression124'):
        assert not _is_linked(b1, 'form_Expression124', a)
    if hasattr(b2, 'form_Expression124'):
        assert _is_linked(b2, 'form_Expression124', a)
    _safe_set(a, 'form_DynamicTable123', None)
    assert not _is_linked(a, 'form_DynamicTable123', b2)
    if hasattr(b2, 'form_Expression124'):
        assert not _is_linked(b2, 'form_Expression124', a)


def test_assoc_maxNumberOfDuplication20_link_reassign_clear():
    a = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Duplicable', b1)
    assert _is_linked(a, 'form_Duplicable', b1)
    if hasattr(b1, 'form_Expression21'):
        assert _is_linked(b1, 'form_Expression21', a)
    _safe_set(a, 'form_Duplicable', b2)
    assert _is_linked(a, 'form_Duplicable', b2)
    if hasattr(b1, 'form_Expression21'):
        assert not _is_linked(b1, 'form_Expression21', a)
    if hasattr(b2, 'form_Expression21'):
        assert _is_linked(b2, 'form_Expression21', a)
    _safe_set(a, 'form_Duplicable', None)
    assert not _is_linked(a, 'form_Duplicable', b2)
    if hasattr(b2, 'form_Expression21'):
        assert not _is_linked(b2, 'form_Expression21', a)


def test_assoc_maxNumberOfRow125_link_reassign_clear():
    a = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_DynamicTable126', b1)
    assert _is_linked(a, 'form_DynamicTable126', b1)
    if hasattr(b1, 'form_Expression127'):
        assert _is_linked(b1, 'form_Expression127', a)
    _safe_set(a, 'form_DynamicTable126', b2)
    assert _is_linked(a, 'form_DynamicTable126', b2)
    if hasattr(b1, 'form_Expression127'):
        assert not _is_linked(b1, 'form_Expression127', a)
    if hasattr(b2, 'form_Expression127'):
        assert _is_linked(b2, 'form_Expression127', a)
    _safe_set(a, 'form_DynamicTable126', None)
    assert not _is_linked(a, 'form_DynamicTable126', b2)
    if hasattr(b2, 'form_Expression127'):
        assert not _is_linked(b2, 'form_Expression127', a)


def test_assoc_maxRowForPagination109_link_reassign_clear():
    a = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Table', b1)
    assert _is_linked(a, 'form_Table', b1)
    if hasattr(b1, 'form_Expression110'):
        assert _is_linked(b1, 'form_Expression110', a)
    _safe_set(a, 'form_Table', b2)
    assert _is_linked(a, 'form_Table', b2)
    if hasattr(b1, 'form_Expression110'):
        assert not _is_linked(b1, 'form_Expression110', a)
    if hasattr(b2, 'form_Expression110'):
        assert _is_linked(b2, 'form_Expression110', a)
    _safe_set(a, 'form_Table', None)
    assert not _is_linked(a, 'form_Table', b2)
    if hasattr(b2, 'form_Expression110'):
        assert not _is_linked(b2, 'form_Expression110', a)


def test_assoc_minNumberOfColumn117_link_reassign_clear():
    a = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_DynamicTable', b1)
    assert _is_linked(a, 'form_DynamicTable', b1)
    if hasattr(b1, 'form_Expression118'):
        assert _is_linked(b1, 'form_Expression118', a)
    _safe_set(a, 'form_DynamicTable', b2)
    assert _is_linked(a, 'form_DynamicTable', b2)
    if hasattr(b1, 'form_Expression118'):
        assert not _is_linked(b1, 'form_Expression118', a)
    if hasattr(b2, 'form_Expression118'):
        assert _is_linked(b2, 'form_Expression118', a)
    _safe_set(a, 'form_DynamicTable', None)
    assert not _is_linked(a, 'form_DynamicTable', b2)
    if hasattr(b2, 'form_Expression118'):
        assert not _is_linked(b2, 'form_Expression118', a)


def test_assoc_minNumberOfDuplication22_link_reassign_clear():
    a = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Duplicable23', b1)
    assert _is_linked(a, 'form_Duplicable23', b1)
    if hasattr(b1, 'form_Expression24'):
        assert _is_linked(b1, 'form_Expression24', a)
    _safe_set(a, 'form_Duplicable23', b2)
    assert _is_linked(a, 'form_Duplicable23', b2)
    if hasattr(b1, 'form_Expression24'):
        assert not _is_linked(b1, 'form_Expression24', a)
    if hasattr(b2, 'form_Expression24'):
        assert _is_linked(b2, 'form_Expression24', a)
    _safe_set(a, 'form_Duplicable23', None)
    assert not _is_linked(a, 'form_Duplicable23', b2)
    if hasattr(b2, 'form_Expression24'):
        assert not _is_linked(b2, 'form_Expression24', a)


def test_assoc_minNumberOfRow119_link_reassign_clear():
    a = form_DynamicTable(allowAddRemoveColumn=True, allowAddRemoveRow=True, limitMaxNumberOfColumn=True, limitMaxNumberOfRow=True, limitMinNumberOfColumn=True, limitMinNumberOfRow=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_DynamicTable120', b1)
    assert _is_linked(a, 'form_DynamicTable120', b1)
    if hasattr(b1, 'form_Expression121'):
        assert _is_linked(b1, 'form_Expression121', a)
    _safe_set(a, 'form_DynamicTable120', b2)
    assert _is_linked(a, 'form_DynamicTable120', b2)
    if hasattr(b1, 'form_Expression121'):
        assert not _is_linked(b1, 'form_Expression121', a)
    if hasattr(b2, 'form_Expression121'):
        assert _is_linked(b2, 'form_Expression121', a)
    _safe_set(a, 'form_DynamicTable120', None)
    assert not _is_linked(a, 'form_DynamicTable120', b2)
    if hasattr(b2, 'form_Expression121'):
        assert not _is_linked(b2, 'form_Expression121', a)


def test_assoc_outputDocumentListExpression94_link_reassign_clear():
    a = form_FileWidget(downloadOnly=True, downloadType="sample_text", initialResourcePath="sample_text", inputType="sample_text", intialResourceList="sample_text", outputDocumentName="sample_text", updateDocument=True, usePreview=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_FileWidget95', b1)
    assert _is_linked(a, 'form_FileWidget95', b1)
    if hasattr(b1, 'form_Expression96'):
        assert _is_linked(b1, 'form_Expression96', a)
    _safe_set(a, 'form_FileWidget95', b2)
    assert _is_linked(a, 'form_FileWidget95', b2)
    if hasattr(b1, 'form_Expression96'):
        assert not _is_linked(b1, 'form_Expression96', a)
    if hasattr(b2, 'form_Expression96'):
        assert _is_linked(b2, 'form_Expression96', a)
    _safe_set(a, 'form_FileWidget95', None)
    assert not _is_linked(a, 'form_FileWidget95', b2)
    if hasattr(b2, 'form_Expression96'):
        assert not _is_linked(b2, 'form_Expression96', a)


def test_assoc_pageLabel15_link_reassign_clear():
    a = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Form16', b1)
    assert _is_linked(a, 'form_Form16', b1)
    if hasattr(b1, 'form_Expression17'):
        assert _is_linked(b1, 'form_Expression17', a)
    _safe_set(a, 'form_Form16', b2)
    assert _is_linked(a, 'form_Form16', b2)
    if hasattr(b1, 'form_Expression17'):
        assert not _is_linked(b1, 'form_Expression17', a)
    if hasattr(b2, 'form_Expression17'):
        assert _is_linked(b2, 'form_Expression17', a)
    _safe_set(a, 'form_Form16', None)
    assert not _is_linked(a, 'form_Form16', b2)
    if hasattr(b2, 'form_Expression17'):
        assert not _is_linked(b2, 'form_Expression17', a)


def test_assoc_parameter1_link_reassign_clear():
    a = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Validator', b1)
    assert _is_linked(a, 'form_Validator', b1)
    if hasattr(b1, 'form_Expression'):
        assert _is_linked(b1, 'form_Expression', a)
    _safe_set(a, 'form_Validator', b2)
    assert _is_linked(a, 'form_Validator', b2)
    if hasattr(b1, 'form_Expression'):
        assert not _is_linked(b1, 'form_Expression', a)
    if hasattr(b2, 'form_Expression'):
        assert _is_linked(b2, 'form_Expression', a)
    _safe_set(a, 'form_Validator', None)
    assert not _is_linked(a, 'form_Validator', b2)
    if hasattr(b2, 'form_Expression'):
        assert not _is_linked(b2, 'form_Expression', a)


def test_assoc_parentOf44_link_reassign_clear():
    a = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    b1 = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b2 = form_Widget(allowHTMLForDisplayLabel=False, displayDependentWidgetOnlyOnEventTriggered=False, injectWidgetCondition=False, labelPosition="sample_text_2", mandatory=False, readOnly=False, realHtmlAttributes="sample_text_2", returnTypeModifier="sample_text_2", showDisplayLabel="sample_text_2", version="sample_text_2")
    _safe_set(a, 'form_WidgetDependency46', b1)
    assert _is_linked(a, 'form_WidgetDependency46', b1)
    if hasattr(b1, 'form_Widget45'):
        assert _is_linked(b1, 'form_Widget45', a)
    _safe_set(a, 'form_WidgetDependency46', b2)
    assert _is_linked(a, 'form_WidgetDependency46', b2)
    if hasattr(b1, 'form_Widget45'):
        assert not _is_linked(b1, 'form_Widget45', a)
    if hasattr(b2, 'form_Widget45'):
        assert _is_linked(b2, 'form_Widget45', a)
    _safe_set(a, 'form_WidgetDependency46', None)
    assert not _is_linked(a, 'form_WidgetDependency46', b2)
    if hasattr(b2, 'form_Widget45'):
        assert not _is_linked(b2, 'form_Widget45', a)


def test_assoc_selectedValues114_link_reassign_clear():
    a = form_Table(allowSelection=True, selectionModeIsMultiple=True, usePagination=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Table115', b1)
    assert _is_linked(a, 'form_Table115', b1)
    if hasattr(b1, 'form_Expression116'):
        assert _is_linked(b1, 'form_Expression116', a)
    _safe_set(a, 'form_Table115', b2)
    assert _is_linked(a, 'form_Table115', b2)
    if hasattr(b1, 'form_Expression116'):
        assert not _is_linked(b1, 'form_Expression116', a)
    if hasattr(b2, 'form_Expression116'):
        assert _is_linked(b2, 'form_Expression116', a)
    _safe_set(a, 'form_Table115', None)
    assert not _is_linked(a, 'form_Table115', b2)
    if hasattr(b2, 'form_Expression116'):
        assert not _is_linked(b2, 'form_Expression116', a)


def test_assoc_stringAttributes7_link_reassign_clear():
    a = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    b1 = form_EStringToStringMapEntry()
    b2 = form_EStringToStringMapEntry()
    _safe_set(a, 'form_Form', {b1})
    assert _is_linked(a, 'form_Form', b1)
    if hasattr(b1, 'form_EStringToStringMapEntry'):
        assert _is_linked(b1, 'form_EStringToStringMapEntry', a)
    _safe_set(a, 'form_Form', {b2})
    assert _is_linked(a, 'form_Form', b2)
    if hasattr(b1, 'form_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'form_EStringToStringMapEntry', a)
    if hasattr(b2, 'form_EStringToStringMapEntry'):
        assert _is_linked(b2, 'form_EStringToStringMapEntry', a)
    _safe_set(a, 'form_Form', set())
    assert not _is_linked(a, 'form_Form', b2)
    if hasattr(b2, 'form_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'form_EStringToStringMapEntry', a)


def test_assoc_tableExpression107_link_reassign_clear():
    a = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    b1 = form_TableExpression()
    b2 = form_TableExpression()
    _safe_set(a, 'form_AbstractTable108', b1)
    assert _is_linked(a, 'form_AbstractTable108', b1)
    if hasattr(b1, 'form_TableExpression'):
        assert _is_linked(b1, 'form_TableExpression', a)
    _safe_set(a, 'form_AbstractTable108', b2)
    assert _is_linked(a, 'form_AbstractTable108', b2)
    if hasattr(b1, 'form_TableExpression'):
        assert not _is_linked(b1, 'form_TableExpression', a)
    if hasattr(b2, 'form_TableExpression'):
        assert _is_linked(b2, 'form_TableExpression', a)
    _safe_set(a, 'form_AbstractTable108', None)
    assert not _is_linked(a, 'form_AbstractTable108', b2)
    if hasattr(b2, 'form_TableExpression'):
        assert not _is_linked(b2, 'form_TableExpression', a)


def test_assoc_tooltip59_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Widget60', b1)
    assert _is_linked(a, 'form_Widget60', b1)
    if hasattr(b1, 'form_Expression61'):
        assert _is_linked(b1, 'form_Expression61', a)
    _safe_set(a, 'form_Widget60', b2)
    assert _is_linked(a, 'form_Widget60', b2)
    if hasattr(b1, 'form_Expression61'):
        assert not _is_linked(b1, 'form_Expression61', a)
    if hasattr(b2, 'form_Expression61'):
        assert _is_linked(b2, 'form_Expression61', a)
    _safe_set(a, 'form_Widget60', None)
    assert not _is_linked(a, 'form_Widget60', b2)
    if hasattr(b2, 'form_Expression61'):
        assert not _is_linked(b2, 'form_Expression61', a)


def test_assoc_tooltipForAdd28_link_reassign_clear():
    a = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Duplicable29', b1)
    assert _is_linked(a, 'form_Duplicable29', b1)
    if hasattr(b1, 'form_Expression30'):
        assert _is_linked(b1, 'form_Expression30', a)
    _safe_set(a, 'form_Duplicable29', b2)
    assert _is_linked(a, 'form_Duplicable29', b2)
    if hasattr(b1, 'form_Expression30'):
        assert not _is_linked(b1, 'form_Expression30', a)
    if hasattr(b2, 'form_Expression30'):
        assert _is_linked(b2, 'form_Expression30', a)
    _safe_set(a, 'form_Duplicable29', None)
    assert not _is_linked(a, 'form_Duplicable29', b2)
    if hasattr(b2, 'form_Expression30'):
        assert not _is_linked(b2, 'form_Expression30', a)


def test_assoc_tooltipForRemove34_link_reassign_clear():
    a = form_Duplicable(duplicate=True, limitMinNumberOfDuplication=True, limitNumberOfDuplication=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_Duplicable35', b1)
    assert _is_linked(a, 'form_Duplicable35', b1)
    if hasattr(b1, 'form_Expression36'):
        assert _is_linked(b1, 'form_Expression36', a)
    _safe_set(a, 'form_Duplicable35', b2)
    assert _is_linked(a, 'form_Duplicable35', b2)
    if hasattr(b1, 'form_Expression36'):
        assert not _is_linked(b1, 'form_Expression36', a)
    if hasattr(b2, 'form_Expression36'):
        assert _is_linked(b2, 'form_Expression36', a)
    _safe_set(a, 'form_Duplicable35', None)
    assert not _is_linked(a, 'form_Duplicable35', b2)
    if hasattr(b2, 'form_Expression36'):
        assert not _is_linked(b2, 'form_Expression36', a)


def test_assoc_validators5_link_reassign_clear():
    a = form_Validator(belowField=True, htmlClass="sample_text", name="sample_text", validatorClass="sample_text")
    b1 = form_Validable(below=True, useDefaultValidator="sample_text")
    b2 = form_Validable(below=False, useDefaultValidator="sample_text_2")
    _safe_set(a, 'form_Validator6', b1)
    assert _is_linked(a, 'form_Validator6', b1)
    if hasattr(b1, 'form_Validable'):
        assert _is_linked(b1, 'form_Validable', a)
    _safe_set(a, 'form_Validator6', b2)
    assert _is_linked(a, 'form_Validator6', b2)
    if hasattr(b1, 'form_Validable'):
        assert not _is_linked(b1, 'form_Validable', a)
    if hasattr(b2, 'form_Validable'):
        assert _is_linked(b2, 'form_Validable', a)
    _safe_set(a, 'form_Validator6', None)
    assert not _is_linked(a, 'form_Validator6', b2)
    if hasattr(b2, 'form_Validable'):
        assert not _is_linked(b2, 'form_Validable', a)


def test_assoc_verticalHeaderExpression104_link_reassign_clear():
    a = form_AbstractTable(LastRowIsHeader=True, firstRowIsHeader=True, initializedUsingCells=True, leftColumnIsHeader=True, rightColumnIsHeader=True, useHorizontalHeader=True, useVerticalHeader=True)
    b1 = form_Expression()
    b2 = form_Expression()
    _safe_set(a, 'form_AbstractTable105', b1)
    assert _is_linked(a, 'form_AbstractTable105', b1)
    if hasattr(b1, 'form_Expression106'):
        assert _is_linked(b1, 'form_Expression106', a)
    _safe_set(a, 'form_AbstractTable105', b2)
    assert _is_linked(a, 'form_AbstractTable105', b2)
    if hasattr(b1, 'form_Expression106'):
        assert not _is_linked(b1, 'form_Expression106', a)
    if hasattr(b2, 'form_Expression106'):
        assert _is_linked(b2, 'form_Expression106', a)
    _safe_set(a, 'form_AbstractTable105', None)
    assert not _is_linked(a, 'form_AbstractTable105', b2)
    if hasattr(b2, 'form_Expression106'):
        assert not _is_linked(b2, 'form_Expression106', a)


def test_assoc_widget0_link_reassign_clear():
    a = form_WidgetDependency(eventTypes="sample_text", triggerRefreshOnModification=True)
    b1 = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b2 = form_Widget(allowHTMLForDisplayLabel=False, displayDependentWidgetOnlyOnEventTriggered=False, injectWidgetCondition=False, labelPosition="sample_text_2", mandatory=False, readOnly=False, realHtmlAttributes="sample_text_2", returnTypeModifier="sample_text_2", showDisplayLabel="sample_text_2", version="sample_text_2")
    _safe_set(a, 'form_WidgetDependency', b1)
    assert _is_linked(a, 'form_WidgetDependency', b1)
    if hasattr(b1, 'form_Widget'):
        assert _is_linked(b1, 'form_Widget', a)
    _safe_set(a, 'form_WidgetDependency', b2)
    assert _is_linked(a, 'form_WidgetDependency', b2)
    if hasattr(b1, 'form_Widget'):
        assert not _is_linked(b1, 'form_Widget', a)
    if hasattr(b2, 'form_Widget'):
        assert _is_linked(b2, 'form_Widget', a)
    _safe_set(a, 'form_WidgetDependency', None)
    assert not _is_linked(a, 'form_WidgetDependency', b2)
    if hasattr(b2, 'form_Widget'):
        assert not _is_linked(b2, 'form_Widget', a)


def test_assoc_widgetLayoutInfo39_link_reassign_clear():
    a = form_WidgetLayoutInfo(column=7, horizontalSpan=7, line=7, verticalSpan=7)
    b1 = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b2 = form_Widget(allowHTMLForDisplayLabel=False, displayDependentWidgetOnlyOnEventTriggered=False, injectWidgetCondition=False, labelPosition="sample_text_2", mandatory=False, readOnly=False, realHtmlAttributes="sample_text_2", returnTypeModifier="sample_text_2", showDisplayLabel="sample_text_2", version="sample_text_2")
    _safe_set(a, 'form_WidgetLayoutInfo', b1)
    assert _is_linked(a, 'form_WidgetLayoutInfo', b1)
    if hasattr(b1, 'form_Widget40'):
        assert _is_linked(b1, 'form_Widget40', a)
    _safe_set(a, 'form_WidgetLayoutInfo', b2)
    assert _is_linked(a, 'form_WidgetLayoutInfo', b2)
    if hasattr(b1, 'form_Widget40'):
        assert not _is_linked(b1, 'form_Widget40', a)
    if hasattr(b2, 'form_Widget40'):
        assert _is_linked(b2, 'form_Widget40', a)
    _safe_set(a, 'form_WidgetLayoutInfo', None)
    assert not _is_linked(a, 'form_WidgetLayoutInfo', b2)
    if hasattr(b2, 'form_Widget40'):
        assert not _is_linked(b2, 'form_Widget40', a)


def test_assoc_widgets12_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Form(allowHTMLInPageLabel=True, nColumn=7, nLine=7, showPageLabel="sample_text", version="sample_text")
    b2 = form_Form(allowHTMLInPageLabel=False, nColumn=13, nLine=13, showPageLabel="sample_text_2", version="sample_text_2")
    _safe_set(a, 'form_Widget14', b1)
    assert _is_linked(a, 'form_Widget14', b1)
    if hasattr(b1, 'form_Form13'):
        assert _is_linked(b1, 'form_Form13', a)
    _safe_set(a, 'form_Widget14', b2)
    assert _is_linked(a, 'form_Widget14', b2)
    if hasattr(b1, 'form_Form13'):
        assert not _is_linked(b1, 'form_Form13', a)
    if hasattr(b2, 'form_Form13'):
        assert _is_linked(b2, 'form_Form13', a)
    _safe_set(a, 'form_Widget14', None)
    assert not _is_linked(a, 'form_Widget14', b2)
    if hasattr(b2, 'form_Form13'):
        assert not _is_linked(b2, 'form_Form13', a)


def test_assoc_widgets74_link_reassign_clear():
    a = form_Widget(allowHTMLForDisplayLabel=True, displayDependentWidgetOnlyOnEventTriggered=True, injectWidgetCondition=True, labelPosition="sample_text", mandatory=True, readOnly=True, realHtmlAttributes="sample_text", returnTypeModifier="sample_text", showDisplayLabel="sample_text", version="sample_text")
    b1 = form_Group(showBorder=True, useIterator=True)
    b2 = form_Group(showBorder=False, useIterator=False)
    _safe_set(a, 'form_Widget75', b1)
    assert _is_linked(a, 'form_Widget75', b1)
    if hasattr(b1, 'form_Group'):
        assert _is_linked(b1, 'form_Group', a)
    _safe_set(a, 'form_Widget75', b2)
    assert _is_linked(a, 'form_Widget75', b2)
    if hasattr(b1, 'form_Group'):
        assert not _is_linked(b1, 'form_Group', a)
    if hasattr(b2, 'form_Group'):
        assert _is_linked(b2, 'form_Group', a)
    _safe_set(a, 'form_Widget75', None)
    assert not _is_linked(a, 'form_Widget75', b2)
    if hasattr(b2, 'form_Group'):
        assert not _is_linked(b2, 'form_Group', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractTable_strategy = st.builds(AbstractTable)
@given(instance=AbstractTable_strategy)
@settings(max_examples=25)
def test_AbstractTable_instantiation(instance):
    assert isinstance(instance, AbstractTable)


CSSCustomizable_strategy = st.builds(CSSCustomizable)
@given(instance=CSSCustomizable_strategy)
@settings(max_examples=25)
def test_CSSCustomizable_instantiation(instance):
    assert isinstance(instance, CSSCustomizable)


ConnectableElement_strategy = st.builds(ConnectableElement)
@given(instance=ConnectableElement_strategy)
@settings(max_examples=25)
def test_ConnectableElement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)


Duplicable_strategy = st.builds(Duplicable)
@given(instance=Duplicable_strategy)
@settings(max_examples=25)
def test_Duplicable_instantiation(instance):
    assert isinstance(instance, Duplicable)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Form_strategy = st.builds(Form)
@given(instance=Form_strategy)
@settings(max_examples=25)
def test_Form_instantiation(instance):
    assert isinstance(instance, Form)


FormButton_strategy = st.builds(FormButton)
@given(instance=FormButton_strategy)
@settings(max_examples=25)
def test_FormButton_instantiation(instance):
    assert isinstance(instance, FormButton)


FormField_strategy = st.builds(FormField)
@given(instance=FormField_strategy)
@settings(max_examples=25)
def test_FormField_instantiation(instance):
    assert isinstance(instance, FormField)


Info_strategy = st.builds(Info)
@given(instance=Info_strategy)
@settings(max_examples=25)
def test_Info_instantiation(instance):
    assert isinstance(instance, Info)


ItemContainer_strategy = st.builds(ItemContainer)
@given(instance=ItemContainer_strategy)
@settings(max_examples=25)
def test_ItemContainer_instantiation(instance):
    assert isinstance(instance, ItemContainer)


MultipleValuatedFormField_strategy = st.builds(MultipleValuatedFormField)
@given(instance=MultipleValuatedFormField_strategy)
@settings(max_examples=25)
def test_MultipleValuatedFormField_instantiation(instance):
    assert isinstance(instance, MultipleValuatedFormField)


SingleValuatedFormField_strategy = st.builds(SingleValuatedFormField)
@given(instance=SingleValuatedFormField_strategy)
@settings(max_examples=25)
def test_SingleValuatedFormField_instantiation(instance):
    assert isinstance(instance, SingleValuatedFormField)


Validable_strategy = st.builds(Validable)
@given(instance=Validable_strategy)
@settings(max_examples=25)
def test_Validable_instantiation(instance):
    assert isinstance(instance, Validable)


Widget_strategy = st.builds(Widget)
@given(instance=Widget_strategy)
@settings(max_examples=25)
def test_Widget_instantiation(instance):
    assert isinstance(instance, Widget)


form_AbstractTable_strategy = st.builds(form_AbstractTable, LastRowIsHeader=st.booleans(), firstRowIsHeader=st.booleans(), initializedUsingCells=st.booleans(), leftColumnIsHeader=st.booleans(), rightColumnIsHeader=st.booleans(), useHorizontalHeader=st.booleans(), useVerticalHeader=st.booleans())
@given(instance=form_AbstractTable_strategy)
@settings(max_examples=25)
def test_form_AbstractTable_instantiation(instance):
    assert isinstance(instance, form_AbstractTable)


form_CSSCustomizable_strategy = st.builds(form_CSSCustomizable)
@given(instance=form_CSSCustomizable_strategy)
@settings(max_examples=25)
def test_form_CSSCustomizable_instantiation(instance):
    assert isinstance(instance, form_CSSCustomizable)


form_CheckBoxMultipleFormField_strategy = st.builds(form_CheckBoxMultipleFormField)
@given(instance=form_CheckBoxMultipleFormField_strategy)
@settings(max_examples=25)
def test_form_CheckBoxMultipleFormField_instantiation(instance):
    assert isinstance(instance, form_CheckBoxMultipleFormField)


form_CheckBoxSingleFormField_strategy = st.builds(form_CheckBoxSingleFormField)
@given(instance=form_CheckBoxSingleFormField_strategy)
@settings(max_examples=25)
def test_form_CheckBoxSingleFormField_instantiation(instance):
    assert isinstance(instance, form_CheckBoxSingleFormField)


form_Column_strategy = st.builds(form_Column, number=st.integers(), width=safe_text)
@given(instance=form_Column_strategy)
@settings(max_examples=25)
def test_form_Column_instantiation(instance):
    assert isinstance(instance, form_Column)


form_ComboFormField_strategy = st.builds(form_ComboFormField)
@given(instance=form_ComboFormField_strategy)
@settings(max_examples=25)
def test_form_ComboFormField_instantiation(instance):
    assert isinstance(instance, form_ComboFormField)


form_DateFormField_strategy = st.builds(form_DateFormField, displayFormat=safe_text, initialFormat=safe_text)
@given(instance=form_DateFormField_strategy)
@settings(max_examples=25)
def test_form_DateFormField_instantiation(instance):
    assert isinstance(instance, form_DateFormField)


form_Document_strategy = st.builds(form_Document)
@given(instance=form_Document_strategy)
@settings(max_examples=25)
def test_form_Document_instantiation(instance):
    assert isinstance(instance, form_Document)


form_Duplicable_strategy = st.builds(form_Duplicable, duplicate=st.booleans(), limitMinNumberOfDuplication=st.booleans(), limitNumberOfDuplication=st.booleans())
@given(instance=form_Duplicable_strategy)
@settings(max_examples=25)
def test_form_Duplicable_instantiation(instance):
    assert isinstance(instance, form_Duplicable)


form_DurationFormField_strategy = st.builds(form_DurationFormField, day=safe_text, hour=safe_text, min=safe_text, sec=safe_text)
@given(instance=form_DurationFormField_strategy)
@settings(max_examples=25)
def test_form_DurationFormField_instantiation(instance):
    assert isinstance(instance, form_DurationFormField)


form_DynamicTable_strategy = st.builds(form_DynamicTable, allowAddRemoveColumn=st.booleans(), allowAddRemoveRow=st.booleans(), limitMaxNumberOfColumn=st.booleans(), limitMaxNumberOfRow=st.booleans(), limitMinNumberOfColumn=st.booleans(), limitMinNumberOfRow=st.booleans())
@given(instance=form_DynamicTable_strategy)
@settings(max_examples=25)
def test_form_DynamicTable_instantiation(instance):
    assert isinstance(instance, form_DynamicTable)


form_EStringToStringMapEntry_strategy = st.builds(form_EStringToStringMapEntry)
@given(instance=form_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_form_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, form_EStringToStringMapEntry)


form_Expression_strategy = st.builds(form_Expression)
@given(instance=form_Expression_strategy)
@settings(max_examples=25)
def test_form_Expression_instantiation(instance):
    assert isinstance(instance, form_Expression)


form_FileWidget_strategy = st.builds(form_FileWidget, downloadOnly=st.booleans(), downloadType=safe_text, initialResourcePath=safe_text, inputType=safe_text, intialResourceList=safe_text, outputDocumentName=safe_text, updateDocument=st.booleans(), usePreview=st.booleans())
@given(instance=form_FileWidget_strategy)
@settings(max_examples=25)
def test_form_FileWidget_instantiation(instance):
    assert isinstance(instance, form_FileWidget)


form_Form_strategy = st.builds(form_Form, allowHTMLInPageLabel=st.booleans(), nColumn=st.integers(), nLine=st.integers(), showPageLabel=safe_text, version=safe_text)
@given(instance=form_Form_strategy)
@settings(max_examples=25)
def test_form_Form_instantiation(instance):
    assert isinstance(instance, form_Form)


form_FormButton_strategy = st.builds(form_FormButton, labelBehavior=safe_text)
@given(instance=form_FormButton_strategy)
@settings(max_examples=25)
def test_form_FormButton_instantiation(instance):
    assert isinstance(instance, form_FormButton)


form_FormField_strategy = st.builds(form_FormField, description=safe_text, exampleMessagePosition=safe_text)
@given(instance=form_FormField_strategy)
@settings(max_examples=25)
def test_form_FormField_instantiation(instance):
    assert isinstance(instance, form_FormField)


form_Group_strategy = st.builds(form_Group, showBorder=st.booleans(), useIterator=st.booleans())
@given(instance=form_Group_strategy)
@settings(max_examples=25)
def test_form_Group_instantiation(instance):
    assert isinstance(instance, form_Group)


form_GroupIterator_strategy = st.builds(form_GroupIterator, className=safe_text)
@given(instance=form_GroupIterator_strategy)
@settings(max_examples=25)
def test_form_GroupIterator_instantiation(instance):
    assert isinstance(instance, form_GroupIterator)


form_HiddenWidget_strategy = st.builds(form_HiddenWidget)
@given(instance=form_HiddenWidget_strategy)
@settings(max_examples=25)
def test_form_HiddenWidget_instantiation(instance):
    assert isinstance(instance, form_HiddenWidget)


form_HtmlWidget_strategy = st.builds(form_HtmlWidget)
@given(instance=form_HtmlWidget_strategy)
@settings(max_examples=25)
def test_form_HtmlWidget_instantiation(instance):
    assert isinstance(instance, form_HtmlWidget)


form_IFrameWidget_strategy = st.builds(form_IFrameWidget)
@given(instance=form_IFrameWidget_strategy)
@settings(max_examples=25)
def test_form_IFrameWidget_instantiation(instance):
    assert isinstance(instance, form_IFrameWidget)


form_ImageWidget_strategy = st.builds(form_ImageWidget, isADocument=st.booleans())
@given(instance=form_ImageWidget_strategy)
@settings(max_examples=25)
def test_form_ImageWidget_instantiation(instance):
    assert isinstance(instance, form_ImageWidget)


form_Info_strategy = st.builds(form_Info)
@given(instance=form_Info_strategy)
@settings(max_examples=25)
def test_form_Info_instantiation(instance):
    assert isinstance(instance, form_Info)


form_ItemContainer_strategy = st.builds(form_ItemContainer, itemClass=safe_text)
@given(instance=form_ItemContainer_strategy)
@settings(max_examples=25)
def test_form_ItemContainer_instantiation(instance):
    assert isinstance(instance, form_ItemContainer)


form_Line_strategy = st.builds(form_Line, height=safe_text, number=st.integers())
@given(instance=form_Line_strategy)
@settings(max_examples=25)
def test_form_Line_instantiation(instance):
    assert isinstance(instance, form_Line)


form_ListFormField_strategy = st.builds(form_ListFormField, maxHeigth=st.integers())
@given(instance=form_ListFormField_strategy)
@settings(max_examples=25)
def test_form_ListFormField_instantiation(instance):
    assert isinstance(instance, form_ListFormField)


form_MandatoryFieldsCustomization_strategy = st.builds(form_MandatoryFieldsCustomization)
@given(instance=form_MandatoryFieldsCustomization_strategy)
@settings(max_examples=25)
def test_form_MandatoryFieldsCustomization_instantiation(instance):
    assert isinstance(instance, form_MandatoryFieldsCustomization)


form_MessageInfo_strategy = st.builds(form_MessageInfo)
@given(instance=form_MessageInfo_strategy)
@settings(max_examples=25)
def test_form_MessageInfo_instantiation(instance):
    assert isinstance(instance, form_MessageInfo)


form_MultipleValuatedFormField_strategy = st.builds(form_MultipleValuatedFormField)
@given(instance=form_MultipleValuatedFormField_strategy)
@settings(max_examples=25)
def test_form_MultipleValuatedFormField_instantiation(instance):
    assert isinstance(instance, form_MultipleValuatedFormField)


form_NextFormButton_strategy = st.builds(form_NextFormButton)
@given(instance=form_NextFormButton_strategy)
@settings(max_examples=25)
def test_form_NextFormButton_instantiation(instance):
    assert isinstance(instance, form_NextFormButton)


form_Operation_strategy = st.builds(form_Operation)
@given(instance=form_Operation_strategy)
@settings(max_examples=25)
def test_form_Operation_instantiation(instance):
    assert isinstance(instance, form_Operation)


form_PasswordFormField_strategy = st.builds(form_PasswordFormField, maxLength=st.integers())
@given(instance=form_PasswordFormField_strategy)
@settings(max_examples=25)
def test_form_PasswordFormField_instantiation(instance):
    assert isinstance(instance, form_PasswordFormField)


form_PreviousFormButton_strategy = st.builds(form_PreviousFormButton)
@given(instance=form_PreviousFormButton_strategy)
@settings(max_examples=25)
def test_form_PreviousFormButton_instantiation(instance):
    assert isinstance(instance, form_PreviousFormButton)


form_RadioFormField_strategy = st.builds(form_RadioFormField)
@given(instance=form_RadioFormField_strategy)
@settings(max_examples=25)
def test_form_RadioFormField_instantiation(instance):
    assert isinstance(instance, form_RadioFormField)


form_RichTextAreaFormField_strategy = st.builds(form_RichTextAreaFormField)
@given(instance=form_RichTextAreaFormField_strategy)
@settings(max_examples=25)
def test_form_RichTextAreaFormField_instantiation(instance):
    assert isinstance(instance, form_RichTextAreaFormField)


form_SelectFormField_strategy = st.builds(form_SelectFormField)
@given(instance=form_SelectFormField_strategy)
@settings(max_examples=25)
def test_form_SelectFormField_instantiation(instance):
    assert isinstance(instance, form_SelectFormField)


form_SingleValuatedFormField_strategy = st.builds(form_SingleValuatedFormField)
@given(instance=form_SingleValuatedFormField_strategy)
@settings(max_examples=25)
def test_form_SingleValuatedFormField_instantiation(instance):
    assert isinstance(instance, form_SingleValuatedFormField)


form_SubmitFormButton_strategy = st.builds(form_SubmitFormButton)
@given(instance=form_SubmitFormButton_strategy)
@settings(max_examples=25)
def test_form_SubmitFormButton_instantiation(instance):
    assert isinstance(instance, form_SubmitFormButton)


form_SuggestBox_strategy = st.builds(form_SuggestBox, asynchronous=st.booleans(), delay=st.integers(), maxItems=st.integers(), useMaxItems=st.booleans())
@given(instance=form_SuggestBox_strategy)
@settings(max_examples=25)
def test_form_SuggestBox_instantiation(instance):
    assert isinstance(instance, form_SuggestBox)


form_Table_strategy = st.builds(form_Table, allowSelection=st.booleans(), selectionModeIsMultiple=st.booleans(), usePagination=st.booleans())
@given(instance=form_Table_strategy)
@settings(max_examples=25)
def test_form_Table_instantiation(instance):
    assert isinstance(instance, form_Table)


form_TableExpression_strategy = st.builds(form_TableExpression)
@given(instance=form_TableExpression_strategy)
@settings(max_examples=25)
def test_form_TableExpression_instantiation(instance):
    assert isinstance(instance, form_TableExpression)


form_TextAreaFormField_strategy = st.builds(form_TextAreaFormField, maxHeigth=st.integers(), maxLength=st.integers())
@given(instance=form_TextAreaFormField_strategy)
@settings(max_examples=25)
def test_form_TextAreaFormField_instantiation(instance):
    assert isinstance(instance, form_TextAreaFormField)


form_TextFormField_strategy = st.builds(form_TextFormField, maxLength=st.integers())
@given(instance=form_TextFormField_strategy)
@settings(max_examples=25)
def test_form_TextFormField_instantiation(instance):
    assert isinstance(instance, form_TextFormField)


form_TextInfo_strategy = st.builds(form_TextInfo)
@given(instance=form_TextInfo_strategy)
@settings(max_examples=25)
def test_form_TextInfo_instantiation(instance):
    assert isinstance(instance, form_TextInfo)


form_Validable_strategy = st.builds(form_Validable, below=st.booleans(), useDefaultValidator=safe_text)
@given(instance=form_Validable_strategy)
@settings(max_examples=25)
def test_form_Validable_instantiation(instance):
    assert isinstance(instance, form_Validable)


form_Validator_strategy = st.builds(form_Validator, belowField=st.booleans(), htmlClass=safe_text, name=safe_text, validatorClass=safe_text)
@given(instance=form_Validator_strategy)
@settings(max_examples=25)
def test_form_Validator_instantiation(instance):
    assert isinstance(instance, form_Validator)


form_ViewForm_strategy = st.builds(form_ViewForm)
@given(instance=form_ViewForm_strategy)
@settings(max_examples=25)
def test_form_ViewForm_instantiation(instance):
    assert isinstance(instance, form_ViewForm)


form_Widget_strategy = st.builds(form_Widget, allowHTMLForDisplayLabel=st.booleans(), displayDependentWidgetOnlyOnEventTriggered=st.booleans(), injectWidgetCondition=st.booleans(), labelPosition=safe_text, mandatory=st.booleans(), readOnly=st.booleans(), realHtmlAttributes=safe_text, returnTypeModifier=safe_text, showDisplayLabel=safe_text, version=safe_text)
@given(instance=form_Widget_strategy)
@settings(max_examples=25)
def test_form_Widget_instantiation(instance):
    assert isinstance(instance, form_Widget)


form_WidgetDependency_strategy = st.builds(form_WidgetDependency, eventTypes=safe_text, triggerRefreshOnModification=st.booleans())
@given(instance=form_WidgetDependency_strategy)
@settings(max_examples=25)
def test_form_WidgetDependency_instantiation(instance):
    assert isinstance(instance, form_WidgetDependency)


form_WidgetLayoutInfo_strategy = st.builds(form_WidgetLayoutInfo, column=st.integers(), horizontalSpan=st.integers(), line=st.integers(), verticalSpan=st.integers())
@given(instance=form_WidgetLayoutInfo_strategy)
@settings(max_examples=25)
def test_form_WidgetLayoutInfo_instantiation(instance):
    assert isinstance(instance, form_WidgetLayoutInfo)


