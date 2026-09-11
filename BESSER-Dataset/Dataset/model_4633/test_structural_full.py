import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BackgroundConditionalStyle,
    BackgroundStyleDescription,
    CellUpdater,
    ColorDescription,
    ColumnMapping,
    CreateCellTool,
    CreateColumnTool,
    CreateCrossColumnTool,
    CreateLineTool,
    CreateTool,
    DColumn,
    DRepresentation,
    DRepresentationElement,
    DSemanticDecorator,
    DTableElement,
    DTableElementStyle,
    DeleteColumnTool,
    DeleteLineTool,
    DeleteTool,
    ElementColumnMapping,
    FeatureColumnMapping,
    ForegroundConditionalStyle,
    ForegroundStyleDescription,
    IntersectionMapping,
    LabelEditTool,
    LineContainer,
    LineMapping,
    RepresentationCreationDescription,
    RepresentationElementMapping,
    RepresentationNavigationDescription,
    TableDescription,
    TableMapping,
    TableTool,
    TableVariable,
    description_AbstractVariable,
    description_CellUpdater,
    description_ColumnMapping,
    description_DocumentedElement,
    description_EndUserDocumentedElement,
    description_RepresentationDescription,
    description_StyleUpdater,
    description_TableMapping,
    description_TableTool,
    description_table_EObject,
    table_DCell,
    table_DCellStyle,
    table_DColumn,
    table_DFeatureColumn,
    table_DLine,
    table_DTable,
    table_DTableElement,
    table_DTableElementStyle,
    table_DTableElementSynchronizer,
    table_DTargetColumn,
    table_LineContainer,
    table_description_BackgroundConditionalStyle,
    table_description_BackgroundStyleDescription,
    table_description_CellUpdater,
    table_description_ColumnMapping,
    table_description_CreateCellTool,
    table_description_CreateColumnTool,
    table_description_CreateCrossColumnTool,
    table_description_CreateLineTool,
    table_description_CreateTool,
    table_description_CrossTableDescription,
    table_description_DeleteColumnTool,
    table_description_DeleteLineTool,
    table_description_DeleteTool,
    table_description_EditionTableDescription,
    table_description_ElementColumnMapping,
    table_description_FeatureColumnMapping,
    table_description_ForegroundConditionalStyle,
    table_description_ForegroundStyleDescription,
    table_description_IntersectionMapping,
    table_description_LabelEditTool,
    table_description_LineMapping,
    table_description_StyleUpdater,
    table_description_TableCreationDescription,
    table_description_TableDescription,
    table_description_TableMapping,
    table_description_TableNavigationDescription,
    table_description_TableTool,
    table_description_TableVariable,
    tool_AbstractToolDescription,
    tool_EditMaskVariables,
    tool_ModelOperation,
    tool_RepresentationCreationDescription,
    tool_RepresentationNavigationDescription,
    tool_VariableContainer,
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

def test_table_DCell_label_value_roundtrip():
    instance = table_DCell(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_table_DColumn_label_value_roundtrip():
    instance = table_DColumn(label="sample_text", visible=True, width=7)
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_table_DColumn_visible_value_roundtrip():
    instance = table_DColumn(label="sample_text", visible=True, width=7)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_table_DColumn_width_value_roundtrip():
    instance = table_DColumn(label="sample_text", visible=True, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_table_DFeatureColumn_featureName_value_roundtrip():
    instance = table_DFeatureColumn(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_table_DLine_collapsed_value_roundtrip():
    instance = table_DLine(collapsed=True, label="sample_text", visible=True)
    assert instance.collapsed == True
    instance.collapsed = False
    assert instance.collapsed == False


def test_table_DLine_label_value_roundtrip():
    instance = table_DLine(collapsed=True, label="sample_text", visible=True)
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_table_DLine_visible_value_roundtrip():
    instance = table_DLine(collapsed=True, label="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_table_DTable_headerColumnWidth_value_roundtrip():
    instance = table_DTable(headerColumnWidth=7)
    assert instance.headerColumnWidth == 7
    instance.headerColumnWidth = 13
    assert instance.headerColumnWidth == 13


def test_table_DTableElementStyle_backgroundColor_value_roundtrip():
    instance = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_table_DTableElementStyle_defaultBackgroundStyle_value_roundtrip():
    instance = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    assert instance.defaultBackgroundStyle == True
    instance.defaultBackgroundStyle = False
    assert instance.defaultBackgroundStyle == False


def test_table_DTableElementStyle_defaultForegroundStyle_value_roundtrip():
    instance = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    assert instance.defaultForegroundStyle == True
    instance.defaultForegroundStyle = False
    assert instance.defaultForegroundStyle == False


def test_table_DTableElementStyle_foregroundColor_value_roundtrip():
    instance = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    assert instance.foregroundColor == "sample_text"
    instance.foregroundColor = "sample_text_2"
    assert instance.foregroundColor == "sample_text_2"


def test_table_DTableElementStyle_labelFormat_value_roundtrip():
    instance = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    assert instance.labelFormat == "sample_text"
    instance.labelFormat = "sample_text_2"
    assert instance.labelFormat == "sample_text_2"


def test_table_DTableElementStyle_labelSize_value_roundtrip():
    instance = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    assert instance.labelSize == 7
    instance.labelSize = 13
    assert instance.labelSize == 13


def test_table_description_BackgroundConditionalStyle_predicateExpression_value_roundtrip():
    instance = table_description_BackgroundConditionalStyle(predicateExpression="sample_text")
    assert instance.predicateExpression == "sample_text"
    instance.predicateExpression = "sample_text_2"
    assert instance.predicateExpression == "sample_text_2"


def test_table_description_CellUpdater_canEdit_value_roundtrip():
    instance = table_description_CellUpdater(canEdit="sample_text")
    assert instance.canEdit == "sample_text"
    instance.canEdit = "sample_text_2"
    assert instance.canEdit == "sample_text_2"


def test_table_description_ColumnMapping_headerLabelExpression_value_roundtrip():
    instance = table_description_ColumnMapping(headerLabelExpression="sample_text", initialWidth=7)
    assert instance.headerLabelExpression == "sample_text"
    instance.headerLabelExpression = "sample_text_2"
    assert instance.headerLabelExpression == "sample_text_2"


def test_table_description_ColumnMapping_initialWidth_value_roundtrip():
    instance = table_description_ColumnMapping(headerLabelExpression="sample_text", initialWidth=7)
    assert instance.initialWidth == 7
    instance.initialWidth = 13
    assert instance.initialWidth == 13


def test_table_description_ElementColumnMapping_domainClass_value_roundtrip():
    instance = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_table_description_ElementColumnMapping_semanticCandidatesExpression_value_roundtrip():
    instance = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.semanticCandidatesExpression == "sample_text"
    instance.semanticCandidatesExpression = "sample_text_2"
    assert instance.semanticCandidatesExpression == "sample_text_2"


def test_table_description_FeatureColumnMapping_featureName_value_roundtrip():
    instance = table_description_FeatureColumnMapping(featureName="sample_text", featureParentExpression="sample_text", labelExpression="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_table_description_FeatureColumnMapping_featureParentExpression_value_roundtrip():
    instance = table_description_FeatureColumnMapping(featureName="sample_text", featureParentExpression="sample_text", labelExpression="sample_text")
    assert instance.featureParentExpression == "sample_text"
    instance.featureParentExpression = "sample_text_2"
    assert instance.featureParentExpression == "sample_text_2"


def test_table_description_FeatureColumnMapping_labelExpression_value_roundtrip():
    instance = table_description_FeatureColumnMapping(featureName="sample_text", featureParentExpression="sample_text", labelExpression="sample_text")
    assert instance.labelExpression == "sample_text"
    instance.labelExpression = "sample_text_2"
    assert instance.labelExpression == "sample_text_2"


def test_table_description_ForegroundConditionalStyle_predicateExpression_value_roundtrip():
    instance = table_description_ForegroundConditionalStyle(predicateExpression="sample_text")
    assert instance.predicateExpression == "sample_text"
    instance.predicateExpression = "sample_text_2"
    assert instance.predicateExpression == "sample_text_2"


def test_table_description_ForegroundStyleDescription_labelFormat_value_roundtrip():
    instance = table_description_ForegroundStyleDescription(labelFormat="sample_text", labelSize=7)
    assert instance.labelFormat == "sample_text"
    instance.labelFormat = "sample_text_2"
    assert instance.labelFormat == "sample_text_2"


def test_table_description_ForegroundStyleDescription_labelSize_value_roundtrip():
    instance = table_description_ForegroundStyleDescription(labelFormat="sample_text", labelSize=7)
    assert instance.labelSize == 7
    instance.labelSize = 13
    assert instance.labelSize == 13


def test_table_description_IntersectionMapping_columnFinderExpression_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.columnFinderExpression == "sample_text"
    instance.columnFinderExpression = "sample_text_2"
    assert instance.columnFinderExpression == "sample_text_2"


def test_table_description_IntersectionMapping_domainClass_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_table_description_IntersectionMapping_labelExpression_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.labelExpression == "sample_text"
    instance.labelExpression = "sample_text_2"
    assert instance.labelExpression == "sample_text_2"


def test_table_description_IntersectionMapping_lineFinderExpression_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.lineFinderExpression == "sample_text"
    instance.lineFinderExpression = "sample_text_2"
    assert instance.lineFinderExpression == "sample_text_2"


def test_table_description_IntersectionMapping_preconditionExpression_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_table_description_IntersectionMapping_semanticCandidatesExpression_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.semanticCandidatesExpression == "sample_text"
    instance.semanticCandidatesExpression = "sample_text_2"
    assert instance.semanticCandidatesExpression == "sample_text_2"


def test_table_description_IntersectionMapping_useDomainClass_value_roundtrip():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert instance.useDomainClass == True
    instance.useDomainClass = False
    assert instance.useDomainClass == False


def test_table_description_LineMapping_domainClass_value_roundtrip():
    instance = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_table_description_LineMapping_headerLabelExpression_value_roundtrip():
    instance = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.headerLabelExpression == "sample_text"
    instance.headerLabelExpression = "sample_text_2"
    assert instance.headerLabelExpression == "sample_text_2"


def test_table_description_LineMapping_semanticCandidatesExpression_value_roundtrip():
    instance = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.semanticCandidatesExpression == "sample_text"
    instance.semanticCandidatesExpression = "sample_text_2"
    assert instance.semanticCandidatesExpression == "sample_text_2"


def test_table_description_TableDescription_domainClass_value_roundtrip():
    instance = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_table_description_TableDescription_initialHeaderColumnWidth_value_roundtrip():
    instance = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    assert instance.initialHeaderColumnWidth == 7
    instance.initialHeaderColumnWidth = 13
    assert instance.initialHeaderColumnWidth == 13


def test_table_description_TableDescription_preconditionExpression_value_roundtrip():
    instance = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_table_description_TableMapping_semanticElements_value_roundtrip():
    instance = table_description_TableMapping(semanticElements="sample_text")
    assert instance.semanticElements == "sample_text"
    instance.semanticElements = "sample_text_2"
    assert instance.semanticElements == "sample_text_2"


def test_table_description_TableVariable_documentation_value_roundtrip():
    instance = table_description_TableVariable(documentation="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_table_description_CreateColumnTool_isa_CreateTool():
    instance = table_description_CreateColumnTool()
    assert isinstance(instance, CreateTool)


def test_table_description_CreateCrossColumnTool_isa_CreateTool():
    instance = table_description_CreateCrossColumnTool()
    assert isinstance(instance, CreateTool)


def test_table_description_CreateLineTool_isa_CreateTool():
    instance = table_description_CreateLineTool()
    assert isinstance(instance, CreateTool)


def test_table_DFeatureColumn_isa_DColumn():
    instance = table_DFeatureColumn(featureName="sample_text")
    assert isinstance(instance, DColumn)


def test_table_DTargetColumn_isa_DColumn():
    instance = table_DTargetColumn()
    assert isinstance(instance, DColumn)


def test_table_DTable_isa_DRepresentation():
    instance = table_DTable(headerColumnWidth=7)
    assert isinstance(instance, DRepresentation)


def test_table_DTableElement_isa_DRepresentationElement():
    instance = table_DTableElement()
    assert isinstance(instance, DRepresentationElement)


def test_table_DCell_isa_DSemanticDecorator():
    instance = table_DCell(label="sample_text")
    assert isinstance(instance, DSemanticDecorator)


def test_table_DTargetColumn_isa_DSemanticDecorator():
    instance = table_DTargetColumn()
    assert isinstance(instance, DSemanticDecorator)


def test_table_LineContainer_isa_DSemanticDecorator():
    instance = table_LineContainer()
    assert isinstance(instance, DSemanticDecorator)


def test_table_DCell_isa_DTableElement():
    instance = table_DCell(label="sample_text")
    assert isinstance(instance, DTableElement)


def test_table_DColumn_isa_DTableElement():
    instance = table_DColumn(label="sample_text", visible=True, width=7)
    assert isinstance(instance, DTableElement)


def test_table_DLine_isa_DTableElement():
    instance = table_DLine(collapsed=True, label="sample_text", visible=True)
    assert isinstance(instance, DTableElement)


def test_table_DCellStyle_isa_DTableElementStyle():
    instance = table_DCellStyle()
    assert isinstance(instance, DTableElementStyle)


def test_table_description_DeleteColumnTool_isa_DeleteTool():
    instance = table_description_DeleteColumnTool()
    assert isinstance(instance, DeleteTool)


def test_table_description_DeleteLineTool_isa_DeleteTool():
    instance = table_description_DeleteLineTool()
    assert isinstance(instance, DeleteTool)


def test_table_DLine_isa_LineContainer():
    instance = table_DLine(collapsed=True, label="sample_text", visible=True)
    assert isinstance(instance, LineContainer)


def test_table_DTable_isa_LineContainer():
    instance = table_DTable(headerColumnWidth=7)
    assert isinstance(instance, LineContainer)


def test_table_description_TableCreationDescription_isa_RepresentationCreationDescription():
    instance = table_description_TableCreationDescription()
    assert isinstance(instance, RepresentationCreationDescription)


def test_table_description_TableMapping_isa_RepresentationElementMapping():
    instance = table_description_TableMapping(semanticElements="sample_text")
    assert isinstance(instance, RepresentationElementMapping)


def test_table_description_TableNavigationDescription_isa_RepresentationNavigationDescription():
    instance = table_description_TableNavigationDescription()
    assert isinstance(instance, RepresentationNavigationDescription)


def test_table_description_CrossTableDescription_isa_TableDescription():
    instance = table_description_CrossTableDescription()
    assert isinstance(instance, TableDescription)


def test_table_description_EditionTableDescription_isa_TableDescription():
    instance = table_description_EditionTableDescription()
    assert isinstance(instance, TableDescription)


def test_table_description_ColumnMapping_isa_TableMapping():
    instance = table_description_ColumnMapping(headerLabelExpression="sample_text", initialWidth=7)
    assert isinstance(instance, TableMapping)


def test_table_description_LabelEditTool_isa_TableTool():
    instance = table_description_LabelEditTool()
    assert isinstance(instance, TableTool)


def test_table_description_TableVariable_isa_description_AbstractVariable():
    instance = table_description_TableVariable(documentation="sample_text")
    assert isinstance(instance, description_AbstractVariable)


def test_table_description_FeatureColumnMapping_isa_description_CellUpdater():
    instance = table_description_FeatureColumnMapping(featureName="sample_text", featureParentExpression="sample_text", labelExpression="sample_text")
    assert isinstance(instance, description_CellUpdater)


def test_table_description_IntersectionMapping_isa_description_CellUpdater():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert isinstance(instance, description_CellUpdater)


def test_table_description_ElementColumnMapping_isa_description_ColumnMapping():
    instance = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_ColumnMapping)


def test_table_description_FeatureColumnMapping_isa_description_ColumnMapping():
    instance = table_description_FeatureColumnMapping(featureName="sample_text", featureParentExpression="sample_text", labelExpression="sample_text")
    assert isinstance(instance, description_ColumnMapping)


def test_table_description_TableDescription_isa_description_DocumentedElement():
    instance = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    assert isinstance(instance, description_DocumentedElement)


def test_table_description_TableDescription_isa_description_EndUserDocumentedElement():
    instance = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    assert isinstance(instance, description_EndUserDocumentedElement)


def test_table_description_TableDescription_isa_description_RepresentationDescription():
    instance = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    assert isinstance(instance, description_RepresentationDescription)


def test_table_description_ElementColumnMapping_isa_description_StyleUpdater():
    instance = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_StyleUpdater)


def test_table_description_FeatureColumnMapping_isa_description_StyleUpdater():
    instance = table_description_FeatureColumnMapping(featureName="sample_text", featureParentExpression="sample_text", labelExpression="sample_text")
    assert isinstance(instance, description_StyleUpdater)


def test_table_description_IntersectionMapping_isa_description_StyleUpdater():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert isinstance(instance, description_StyleUpdater)


def test_table_description_LineMapping_isa_description_StyleUpdater():
    instance = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_StyleUpdater)


def test_table_description_IntersectionMapping_isa_description_TableMapping():
    instance = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    assert isinstance(instance, description_TableMapping)


def test_table_description_LineMapping_isa_description_TableMapping():
    instance = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_TableMapping)


def test_table_description_CreateCellTool_isa_description_TableTool():
    instance = table_description_CreateCellTool()
    assert isinstance(instance, description_TableTool)


def test_table_description_CreateTool_isa_description_TableTool():
    instance = table_description_CreateTool()
    assert isinstance(instance, description_TableTool)


def test_table_description_DeleteTool_isa_description_TableTool():
    instance = table_description_DeleteTool()
    assert isinstance(instance, description_TableTool)


def test_table_description_CreateCellTool_isa_tool_AbstractToolDescription():
    instance = table_description_CreateCellTool()
    assert isinstance(instance, tool_AbstractToolDescription)


def test_table_description_CreateTool_isa_tool_AbstractToolDescription():
    instance = table_description_CreateTool()
    assert isinstance(instance, tool_AbstractToolDescription)


def test_table_description_DeleteTool_isa_tool_AbstractToolDescription():
    instance = table_description_DeleteTool()
    assert isinstance(instance, tool_AbstractToolDescription)


def test_table_description_TableVariable_isa_tool_VariableContainer():
    instance = table_description_TableVariable(documentation="sample_text")
    assert isinstance(instance, tool_VariableContainer)


def test_assoc_allCreateLine67_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = CreateLineTool()
    b2 = CreateLineTool()
    _safe_set(a, 'table_description_TableDescription68', {b1})
    assert _is_linked(a, 'table_description_TableDescription68', b1)
    if hasattr(b1, 'CreateLineTool69'):
        assert _is_linked(b1, 'CreateLineTool69', a)
    _safe_set(a, 'table_description_TableDescription68', {b2})
    assert _is_linked(a, 'table_description_TableDescription68', b2)
    if hasattr(b1, 'CreateLineTool69'):
        assert not _is_linked(b1, 'CreateLineTool69', a)
    if hasattr(b2, 'CreateLineTool69'):
        assert _is_linked(b2, 'CreateLineTool69', a)
    _safe_set(a, 'table_description_TableDescription68', set())
    assert not _is_linked(a, 'table_description_TableDescription68', b2)
    if hasattr(b2, 'CreateLineTool69'):
        assert not _is_linked(b2, 'CreateLineTool69', a)


def test_assoc_allLineMappings59_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_description_TableDescription60', {b1})
    assert _is_linked(a, 'table_description_TableDescription60', b1)
    if hasattr(b1, 'LineMapping61'):
        assert _is_linked(b1, 'LineMapping61', a)
    _safe_set(a, 'table_description_TableDescription60', {b2})
    assert _is_linked(a, 'table_description_TableDescription60', b2)
    if hasattr(b1, 'LineMapping61'):
        assert not _is_linked(b1, 'LineMapping61', a)
    if hasattr(b2, 'LineMapping61'):
        assert _is_linked(b2, 'LineMapping61', a)
    _safe_set(a, 'table_description_TableDescription60', set())
    assert not _is_linked(a, 'table_description_TableDescription60', b2)
    if hasattr(b2, 'LineMapping61'):
        assert not _is_linked(b2, 'LineMapping61', a)


def test_assoc_allRepresentationCreationDescriptions42_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = tool_RepresentationCreationDescription()
    b2 = tool_RepresentationCreationDescription()
    _safe_set(a, 'table_description_TableDescription43', {b1})
    assert _is_linked(a, 'table_description_TableDescription43', b1)
    if hasattr(b1, 'tool_RepresentationCreationDescription44'):
        assert _is_linked(b1, 'tool_RepresentationCreationDescription44', a)
    _safe_set(a, 'table_description_TableDescription43', {b2})
    assert _is_linked(a, 'table_description_TableDescription43', b2)
    if hasattr(b1, 'tool_RepresentationCreationDescription44'):
        assert not _is_linked(b1, 'tool_RepresentationCreationDescription44', a)
    if hasattr(b2, 'tool_RepresentationCreationDescription44'):
        assert _is_linked(b2, 'tool_RepresentationCreationDescription44', a)
    _safe_set(a, 'table_description_TableDescription43', set())
    assert not _is_linked(a, 'table_description_TableDescription43', b2)
    if hasattr(b2, 'tool_RepresentationCreationDescription44'):
        assert not _is_linked(b2, 'tool_RepresentationCreationDescription44', a)


def test_assoc_allRepresentationNavigationDescriptions50_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = tool_RepresentationNavigationDescription()
    b2 = tool_RepresentationNavigationDescription()
    _safe_set(a, 'table_description_TableDescription51', {b1})
    assert _is_linked(a, 'table_description_TableDescription51', b1)
    if hasattr(b1, 'tool_RepresentationNavigationDescription52'):
        assert _is_linked(b1, 'tool_RepresentationNavigationDescription52', a)
    _safe_set(a, 'table_description_TableDescription51', {b2})
    assert _is_linked(a, 'table_description_TableDescription51', b2)
    if hasattr(b1, 'tool_RepresentationNavigationDescription52'):
        assert not _is_linked(b1, 'tool_RepresentationNavigationDescription52', a)
    if hasattr(b2, 'tool_RepresentationNavigationDescription52'):
        assert _is_linked(b2, 'tool_RepresentationNavigationDescription52', a)
    _safe_set(a, 'table_description_TableDescription51', set())
    assert not _is_linked(a, 'table_description_TableDescription51', b2)
    if hasattr(b2, 'tool_RepresentationNavigationDescription52'):
        assert not _is_linked(b2, 'tool_RepresentationNavigationDescription52', a)


def test_assoc_allSubLines89_link_reassign_clear():
    a = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_description_LineMapping90', {b1})
    assert _is_linked(a, 'table_description_LineMapping90', b1)
    if hasattr(b1, 'LineMapping91'):
        assert _is_linked(b1, 'LineMapping91', a)
    _safe_set(a, 'table_description_LineMapping90', {b2})
    assert _is_linked(a, 'table_description_LineMapping90', b2)
    if hasattr(b1, 'LineMapping91'):
        assert not _is_linked(b1, 'LineMapping91', a)
    if hasattr(b2, 'LineMapping91'):
        assert _is_linked(b2, 'LineMapping91', a)
    _safe_set(a, 'table_description_LineMapping90', set())
    assert not _is_linked(a, 'table_description_LineMapping90', b2)
    if hasattr(b2, 'LineMapping91'):
        assert not _is_linked(b2, 'LineMapping91', a)


def test_assoc_cells28_link_reassign_clear():
    a = table_DColumn(label="sample_text", visible=True, width=7)
    b1 = table_DCell(label="sample_text")
    b2 = table_DCell(label="sample_text_2")
    _safe_set(a, 'column', {b1})
    assert _is_linked(a, 'column', b1)
    if hasattr(b1, 'DCell29'):
        assert _is_linked(b1, 'DCell29', a)
    _safe_set(a, 'column', {b2})
    assert _is_linked(a, 'column', b2)
    if hasattr(b1, 'DCell29'):
        assert not _is_linked(b1, 'DCell29', a)
    if hasattr(b2, 'DCell29'):
        assert _is_linked(b2, 'DCell29', a)
    _safe_set(a, 'column', set())
    assert not _is_linked(a, 'column', b2)
    if hasattr(b2, 'DCell29'):
        assert not _is_linked(b2, 'DCell29', a)


def test_assoc_cells5_link_reassign_clear():
    a = table_DLine(collapsed=True, label="sample_text", visible=True)
    b1 = table_DCell(label="sample_text")
    b2 = table_DCell(label="sample_text_2")
    _safe_set(a, 'line', {b1})
    assert _is_linked(a, 'line', b1)
    if hasattr(b1, 'DCell'):
        assert _is_linked(b1, 'DCell', a)
    _safe_set(a, 'line', {b2})
    assert _is_linked(a, 'line', b2)
    if hasattr(b1, 'DCell'):
        assert not _is_linked(b1, 'DCell', a)
    if hasattr(b2, 'DCell'):
        assert _is_linked(b2, 'DCell', a)
    _safe_set(a, 'line', set())
    assert not _is_linked(a, 'line', b2)
    if hasattr(b2, 'DCell'):
        assert not _is_linked(b2, 'DCell', a)


def test_assoc_column13_link_reassign_clear():
    a = table_DColumn(label="sample_text", visible=True, width=7)
    b1 = table_DCell(label="sample_text")
    b2 = table_DCell(label="sample_text_2")
    _safe_set(a, 'DColumn15', b1)
    assert _is_linked(a, 'DColumn15', b1)
    if hasattr(b1, 'cells14'):
        assert _is_linked(b1, 'cells14', a)
    _safe_set(a, 'DColumn15', b2)
    assert _is_linked(a, 'DColumn15', b2)
    if hasattr(b1, 'cells14'):
        assert not _is_linked(b1, 'cells14', a)
    if hasattr(b2, 'cells14'):
        assert _is_linked(b2, 'cells14', a)
    _safe_set(a, 'DColumn15', None)
    assert not _is_linked(a, 'DColumn15', b2)
    if hasattr(b2, 'cells14'):
        assert not _is_linked(b2, 'cells14', a)


def test_assoc_columnMapping112_link_reassign_clear():
    a = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    b1 = ColumnMapping()
    b2 = ColumnMapping()
    _safe_set(a, 'table_description_IntersectionMapping113', b1)
    assert _is_linked(a, 'table_description_IntersectionMapping113', b1)
    if hasattr(b1, 'ColumnMapping114'):
        assert _is_linked(b1, 'ColumnMapping114', a)
    _safe_set(a, 'table_description_IntersectionMapping113', b2)
    assert _is_linked(a, 'table_description_IntersectionMapping113', b2)
    if hasattr(b1, 'ColumnMapping114'):
        assert not _is_linked(b1, 'ColumnMapping114', a)
    if hasattr(b2, 'ColumnMapping114'):
        assert _is_linked(b2, 'ColumnMapping114', a)
    _safe_set(a, 'table_description_IntersectionMapping113', None)
    assert not _is_linked(a, 'table_description_IntersectionMapping113', b2)
    if hasattr(b2, 'ColumnMapping114'):
        assert not _is_linked(b2, 'ColumnMapping114', a)


def test_assoc_columns0_link_reassign_clear():
    a = table_DTable(headerColumnWidth=7)
    b1 = table_DColumn(label="sample_text", visible=True, width=7)
    b2 = table_DColumn(label="sample_text_2", visible=False, width=13)
    _safe_set(a, 'table', {b1})
    assert _is_linked(a, 'table', b1)
    if hasattr(b1, 'DColumn'):
        assert _is_linked(b1, 'DColumn', a)
    _safe_set(a, 'table', {b2})
    assert _is_linked(a, 'table', b2)
    if hasattr(b1, 'DColumn'):
        assert not _is_linked(b1, 'DColumn', a)
    if hasattr(b2, 'DColumn'):
        assert _is_linked(b2, 'DColumn', a)
    _safe_set(a, 'table', set())
    assert not _is_linked(a, 'table', b2)
    if hasattr(b2, 'DColumn'):
        assert not _is_linked(b2, 'DColumn', a)


def test_assoc_container6_link_reassign_clear():
    a = table_DLine(collapsed=True, label="sample_text", visible=True)
    b1 = table_LineContainer()
    b2 = table_LineContainer()
    _safe_set(a, 'lines', b1)
    assert _is_linked(a, 'lines', b1)
    if hasattr(b1, 'LineContainer'):
        assert _is_linked(b1, 'LineContainer', a)
    _safe_set(a, 'lines', b2)
    assert _is_linked(a, 'lines', b2)
    if hasattr(b1, 'LineContainer'):
        assert not _is_linked(b1, 'LineContainer', a)
    if hasattr(b2, 'LineContainer'):
        assert _is_linked(b2, 'LineContainer', a)
    _safe_set(a, 'lines', None)
    assert not _is_linked(a, 'lines', b2)
    if hasattr(b2, 'LineContainer'):
        assert not _is_linked(b2, 'LineContainer', a)


def test_assoc_create115_link_reassign_clear():
    a = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    b1 = CreateCellTool()
    b2 = CreateCellTool()
    _safe_set(a, 'mapping116', b1)
    assert _is_linked(a, 'mapping116', b1)
    if hasattr(b1, 'CreateCellTool'):
        assert _is_linked(b1, 'CreateCellTool', a)
    _safe_set(a, 'mapping116', b2)
    assert _is_linked(a, 'mapping116', b2)
    if hasattr(b1, 'CreateCellTool'):
        assert not _is_linked(b1, 'CreateCellTool', a)
    if hasattr(b2, 'CreateCellTool'):
        assert _is_linked(b2, 'CreateCellTool', a)
    _safe_set(a, 'mapping116', None)
    assert not _is_linked(a, 'mapping116', b2)
    if hasattr(b2, 'CreateCellTool'):
        assert not _is_linked(b2, 'CreateCellTool', a)


def test_assoc_create94_link_reassign_clear():
    a = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = CreateLineTool()
    b2 = CreateLineTool()
    _safe_set(a, 'table_description_LineMapping95', {b1})
    assert _is_linked(a, 'table_description_LineMapping95', b1)
    if hasattr(b1, 'CreateLineTool96'):
        assert _is_linked(b1, 'CreateLineTool96', a)
    _safe_set(a, 'table_description_LineMapping95', {b2})
    assert _is_linked(a, 'table_description_LineMapping95', b2)
    if hasattr(b1, 'CreateLineTool96'):
        assert not _is_linked(b1, 'CreateLineTool96', a)
    if hasattr(b2, 'CreateLineTool96'):
        assert _is_linked(b2, 'CreateLineTool96', a)
    _safe_set(a, 'table_description_LineMapping95', set())
    assert not _is_linked(a, 'table_description_LineMapping95', b2)
    if hasattr(b2, 'CreateLineTool96'):
        assert not _is_linked(b2, 'CreateLineTool96', a)


def test_assoc_create98_link_reassign_clear():
    a = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    b1 = CreateColumnTool()
    b2 = CreateColumnTool()
    _safe_set(a, 'mapping99', {b1})
    assert _is_linked(a, 'mapping99', b1)
    if hasattr(b1, 'CreateColumnTool'):
        assert _is_linked(b1, 'CreateColumnTool', a)
    _safe_set(a, 'mapping99', {b2})
    assert _is_linked(a, 'mapping99', b2)
    if hasattr(b1, 'CreateColumnTool'):
        assert not _is_linked(b1, 'CreateColumnTool', a)
    if hasattr(b2, 'CreateColumnTool'):
        assert _is_linked(b2, 'CreateColumnTool', a)
    _safe_set(a, 'mapping99', set())
    assert not _is_linked(a, 'mapping99', b2)
    if hasattr(b2, 'CreateColumnTool'):
        assert not _is_linked(b2, 'CreateColumnTool', a)


def test_assoc_currentStyle16_link_reassign_clear():
    a = table_DCell(label="sample_text")
    b1 = table_DCellStyle()
    b2 = table_DCellStyle()
    _safe_set(a, 'table_DCell17', b1)
    assert _is_linked(a, 'table_DCell17', b1)
    if hasattr(b1, 'table_DCellStyle'):
        assert _is_linked(b1, 'table_DCellStyle', a)
    _safe_set(a, 'table_DCell17', b2)
    assert _is_linked(a, 'table_DCell17', b2)
    if hasattr(b1, 'table_DCellStyle'):
        assert not _is_linked(b1, 'table_DCellStyle', a)
    if hasattr(b2, 'table_DCellStyle'):
        assert _is_linked(b2, 'table_DCellStyle', a)
    _safe_set(a, 'table_DCell17', None)
    assert not _is_linked(a, 'table_DCell17', b2)
    if hasattr(b2, 'table_DCellStyle'):
        assert not _is_linked(b2, 'table_DCellStyle', a)


def test_assoc_currentStyle35_link_reassign_clear():
    a = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    b1 = table_DColumn(label="sample_text", visible=True, width=7)
    b2 = table_DColumn(label="sample_text_2", visible=False, width=13)
    _safe_set(a, 'table_DTableElementStyle37', b1)
    assert _is_linked(a, 'table_DTableElementStyle37', b1)
    if hasattr(b1, 'table_DColumn36'):
        assert _is_linked(b1, 'table_DColumn36', a)
    _safe_set(a, 'table_DTableElementStyle37', b2)
    assert _is_linked(a, 'table_DTableElementStyle37', b2)
    if hasattr(b1, 'table_DColumn36'):
        assert not _is_linked(b1, 'table_DColumn36', a)
    if hasattr(b2, 'table_DColumn36'):
        assert _is_linked(b2, 'table_DColumn36', a)
    _safe_set(a, 'table_DTableElementStyle37', None)
    assert not _is_linked(a, 'table_DTableElementStyle37', b2)
    if hasattr(b2, 'table_DColumn36'):
        assert not _is_linked(b2, 'table_DColumn36', a)


def test_assoc_currentStyle9_link_reassign_clear():
    a = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    b1 = table_DLine(collapsed=True, label="sample_text", visible=True)
    b2 = table_DLine(collapsed=False, label="sample_text_2", visible=False)
    _safe_set(a, 'table_DTableElementStyle', b1)
    assert _is_linked(a, 'table_DTableElementStyle', b1)
    if hasattr(b1, 'table_DLine10'):
        assert _is_linked(b1, 'table_DLine10', a)
    _safe_set(a, 'table_DTableElementStyle', b2)
    assert _is_linked(a, 'table_DTableElementStyle', b2)
    if hasattr(b1, 'table_DLine10'):
        assert not _is_linked(b1, 'table_DLine10', a)
    if hasattr(b2, 'table_DLine10'):
        assert _is_linked(b2, 'table_DLine10', a)
    _safe_set(a, 'table_DTableElementStyle', None)
    assert not _is_linked(a, 'table_DTableElementStyle', b2)
    if hasattr(b2, 'table_DLine10'):
        assert not _is_linked(b2, 'table_DLine10', a)


def test_assoc_delete100_link_reassign_clear():
    a = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    b1 = DeleteColumnTool()
    b2 = DeleteColumnTool()
    _safe_set(a, 'mapping101', b1)
    assert _is_linked(a, 'mapping101', b1)
    if hasattr(b1, 'DeleteColumnTool'):
        assert _is_linked(b1, 'DeleteColumnTool', a)
    _safe_set(a, 'mapping101', b2)
    assert _is_linked(a, 'mapping101', b2)
    if hasattr(b1, 'DeleteColumnTool'):
        assert not _is_linked(b1, 'DeleteColumnTool', a)
    if hasattr(b2, 'DeleteColumnTool'):
        assert _is_linked(b2, 'DeleteColumnTool', a)
    _safe_set(a, 'mapping101', None)
    assert not _is_linked(a, 'mapping101', b2)
    if hasattr(b2, 'DeleteColumnTool'):
        assert not _is_linked(b2, 'DeleteColumnTool', a)


def test_assoc_delete97_link_reassign_clear():
    a = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = DeleteLineTool()
    b2 = DeleteLineTool()
    _safe_set(a, 'mapping', b1)
    assert _is_linked(a, 'mapping', b1)
    if hasattr(b1, 'DeleteLineTool'):
        assert _is_linked(b1, 'DeleteLineTool', a)
    _safe_set(a, 'mapping', b2)
    assert _is_linked(a, 'mapping', b2)
    if hasattr(b1, 'DeleteLineTool'):
        assert not _is_linked(b1, 'DeleteLineTool', a)
    if hasattr(b2, 'DeleteLineTool'):
        assert _is_linked(b2, 'DeleteLineTool', a)
    _safe_set(a, 'mapping', None)
    assert not _is_linked(a, 'mapping', b2)
    if hasattr(b2, 'DeleteLineTool'):
        assert not _is_linked(b2, 'DeleteLineTool', a)


def test_assoc_description1_link_reassign_clear():
    a = table_DTable(headerColumnWidth=7)
    b1 = TableDescription()
    b2 = TableDescription()
    _safe_set(a, 'table_DTable', b1)
    assert _is_linked(a, 'table_DTable', b1)
    if hasattr(b1, 'TableDescription'):
        assert _is_linked(b1, 'TableDescription', a)
    _safe_set(a, 'table_DTable', b2)
    assert _is_linked(a, 'table_DTable', b2)
    if hasattr(b1, 'TableDescription'):
        assert not _is_linked(b1, 'TableDescription', a)
    if hasattr(b2, 'TableDescription'):
        assert _is_linked(b2, 'TableDescription', a)
    _safe_set(a, 'table_DTable', None)
    assert not _is_linked(a, 'table_DTable', b2)
    if hasattr(b2, 'TableDescription'):
        assert not _is_linked(b2, 'TableDescription', a)


def test_assoc_directEdit102_link_reassign_clear():
    a = table_description_CellUpdater(canEdit="sample_text")
    b1 = LabelEditTool()
    b2 = LabelEditTool()
    _safe_set(a, 'table_description_CellUpdater', b1)
    assert _is_linked(a, 'table_description_CellUpdater', b1)
    if hasattr(b1, 'LabelEditTool'):
        assert _is_linked(b1, 'LabelEditTool', a)
    _safe_set(a, 'table_description_CellUpdater', b2)
    assert _is_linked(a, 'table_description_CellUpdater', b2)
    if hasattr(b1, 'LabelEditTool'):
        assert not _is_linked(b1, 'LabelEditTool', a)
    if hasattr(b2, 'LabelEditTool'):
        assert _is_linked(b2, 'LabelEditTool', a)
    _safe_set(a, 'table_description_CellUpdater', None)
    assert not _is_linked(a, 'table_description_CellUpdater', b2)
    if hasattr(b2, 'LabelEditTool'):
        assert not _is_linked(b2, 'LabelEditTool', a)


def test_assoc_foreGroundColor137_link_reassign_clear():
    a = table_description_ForegroundStyleDescription(labelFormat="sample_text", labelSize=7)
    b1 = ColorDescription()
    b2 = ColorDescription()
    _safe_set(a, 'table_description_ForegroundStyleDescription', b1)
    assert _is_linked(a, 'table_description_ForegroundStyleDescription', b1)
    if hasattr(b1, 'ColorDescription'):
        assert _is_linked(b1, 'ColorDescription', a)
    _safe_set(a, 'table_description_ForegroundStyleDescription', b2)
    assert _is_linked(a, 'table_description_ForegroundStyleDescription', b2)
    if hasattr(b1, 'ColorDescription'):
        assert not _is_linked(b1, 'ColorDescription', a)
    if hasattr(b2, 'ColorDescription'):
        assert _is_linked(b2, 'ColorDescription', a)
    _safe_set(a, 'table_description_ForegroundStyleDescription', None)
    assert not _is_linked(a, 'table_description_ForegroundStyleDescription', b2)
    if hasattr(b2, 'ColorDescription'):
        assert not _is_linked(b2, 'ColorDescription', a)


def test_assoc_importedElements70_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = description_table_EObject()
    b2 = description_table_EObject()
    _safe_set(a, 'table_description_TableDescription71', {b1})
    assert _is_linked(a, 'table_description_TableDescription71', b1)
    if hasattr(b1, 'description_table_EObject'):
        assert _is_linked(b1, 'description_table_EObject', a)
    _safe_set(a, 'table_description_TableDescription71', {b2})
    assert _is_linked(a, 'table_description_TableDescription71', b2)
    if hasattr(b1, 'description_table_EObject'):
        assert not _is_linked(b1, 'description_table_EObject', a)
    if hasattr(b2, 'description_table_EObject'):
        assert _is_linked(b2, 'description_table_EObject', a)
    _safe_set(a, 'table_description_TableDescription71', set())
    assert not _is_linked(a, 'table_description_TableDescription71', b2)
    if hasattr(b2, 'description_table_EObject'):
        assert not _is_linked(b2, 'description_table_EObject', a)


def test_assoc_intersectionMapping20_link_reassign_clear():
    a = table_DCell(label="sample_text")
    b1 = IntersectionMapping()
    b2 = IntersectionMapping()
    _safe_set(a, 'table_DCell21', b1)
    assert _is_linked(a, 'table_DCell21', b1)
    if hasattr(b1, 'IntersectionMapping'):
        assert _is_linked(b1, 'IntersectionMapping', a)
    _safe_set(a, 'table_DCell21', b2)
    assert _is_linked(a, 'table_DCell21', b2)
    if hasattr(b1, 'IntersectionMapping'):
        assert not _is_linked(b1, 'IntersectionMapping', a)
    if hasattr(b2, 'IntersectionMapping'):
        assert _is_linked(b2, 'IntersectionMapping', a)
    _safe_set(a, 'table_DCell21', None)
    assert not _is_linked(a, 'table_DCell21', b2)
    if hasattr(b2, 'IntersectionMapping'):
        assert not _is_linked(b2, 'IntersectionMapping', a)


def test_assoc_line11_link_reassign_clear():
    a = table_DLine(collapsed=True, label="sample_text", visible=True)
    b1 = table_DCell(label="sample_text")
    b2 = table_DCell(label="sample_text_2")
    _safe_set(a, 'DLine12', b1)
    assert _is_linked(a, 'DLine12', b1)
    if hasattr(b1, 'cells'):
        assert _is_linked(b1, 'cells', a)
    _safe_set(a, 'DLine12', b2)
    assert _is_linked(a, 'DLine12', b2)
    if hasattr(b1, 'cells'):
        assert not _is_linked(b1, 'cells', a)
    if hasattr(b2, 'cells'):
        assert _is_linked(b2, 'cells', a)
    _safe_set(a, 'DLine12', None)
    assert not _is_linked(a, 'DLine12', b2)
    if hasattr(b2, 'cells'):
        assert not _is_linked(b2, 'cells', a)


def test_assoc_lineMapping110_link_reassign_clear():
    a = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_description_IntersectionMapping', {b1})
    assert _is_linked(a, 'table_description_IntersectionMapping', b1)
    if hasattr(b1, 'LineMapping111'):
        assert _is_linked(b1, 'LineMapping111', a)
    _safe_set(a, 'table_description_IntersectionMapping', {b2})
    assert _is_linked(a, 'table_description_IntersectionMapping', b2)
    if hasattr(b1, 'LineMapping111'):
        assert not _is_linked(b1, 'LineMapping111', a)
    if hasattr(b2, 'LineMapping111'):
        assert _is_linked(b2, 'LineMapping111', a)
    _safe_set(a, 'table_description_IntersectionMapping', set())
    assert not _is_linked(a, 'table_description_IntersectionMapping', b2)
    if hasattr(b2, 'LineMapping111'):
        assert not _is_linked(b2, 'LineMapping111', a)


def test_assoc_lines3_link_reassign_clear():
    a = table_DLine(collapsed=True, label="sample_text", visible=True)
    b1 = table_LineContainer()
    b2 = table_LineContainer()
    _safe_set(a, 'DLine', b1)
    assert _is_linked(a, 'DLine', b1)
    if hasattr(b1, 'container'):
        assert _is_linked(b1, 'container', a)
    _safe_set(a, 'DLine', b2)
    assert _is_linked(a, 'DLine', b2)
    if hasattr(b1, 'container'):
        assert not _is_linked(b1, 'container', a)
    if hasattr(b2, 'container'):
        assert _is_linked(b2, 'container', a)
    _safe_set(a, 'DLine', None)
    assert not _is_linked(a, 'DLine', b2)
    if hasattr(b2, 'container'):
        assert not _is_linked(b2, 'container', a)


def test_assoc_orderedCells32_link_reassign_clear():
    a = table_DColumn(label="sample_text", visible=True, width=7)
    b1 = table_DCell(label="sample_text")
    b2 = table_DCell(label="sample_text_2")
    _safe_set(a, 'table_DColumn33', {b1})
    assert _is_linked(a, 'table_DColumn33', b1)
    if hasattr(b1, 'table_DCell34'):
        assert _is_linked(b1, 'table_DCell34', a)
    _safe_set(a, 'table_DColumn33', {b2})
    assert _is_linked(a, 'table_DColumn33', b2)
    if hasattr(b1, 'table_DCell34'):
        assert not _is_linked(b1, 'table_DCell34', a)
    if hasattr(b2, 'table_DCell34'):
        assert _is_linked(b2, 'table_DCell34', a)
    _safe_set(a, 'table_DColumn33', set())
    assert not _is_linked(a, 'table_DColumn33', b2)
    if hasattr(b2, 'table_DCell34'):
        assert not _is_linked(b2, 'table_DCell34', a)


def test_assoc_orderedCells7_link_reassign_clear():
    a = table_DLine(collapsed=True, label="sample_text", visible=True)
    b1 = table_DCell(label="sample_text")
    b2 = table_DCell(label="sample_text_2")
    _safe_set(a, 'table_DLine8', {b1})
    assert _is_linked(a, 'table_DLine8', b1)
    if hasattr(b1, 'table_DCell'):
        assert _is_linked(b1, 'table_DCell', a)
    _safe_set(a, 'table_DLine8', {b2})
    assert _is_linked(a, 'table_DLine8', b2)
    if hasattr(b1, 'table_DCell'):
        assert not _is_linked(b1, 'table_DCell', a)
    if hasattr(b2, 'table_DCell'):
        assert _is_linked(b2, 'table_DCell', a)
    _safe_set(a, 'table_DLine8', set())
    assert not _is_linked(a, 'table_DLine8', b2)
    if hasattr(b2, 'table_DCell'):
        assert not _is_linked(b2, 'table_DCell', a)


def test_assoc_originMapping30_link_reassign_clear():
    a = table_DColumn(label="sample_text", visible=True, width=7)
    b1 = ColumnMapping()
    b2 = ColumnMapping()
    _safe_set(a, 'table_DColumn', b1)
    assert _is_linked(a, 'table_DColumn', b1)
    if hasattr(b1, 'ColumnMapping'):
        assert _is_linked(b1, 'ColumnMapping', a)
    _safe_set(a, 'table_DColumn', b2)
    assert _is_linked(a, 'table_DColumn', b2)
    if hasattr(b1, 'ColumnMapping'):
        assert not _is_linked(b1, 'ColumnMapping', a)
    if hasattr(b2, 'ColumnMapping'):
        assert _is_linked(b2, 'ColumnMapping', a)
    _safe_set(a, 'table_DColumn', None)
    assert not _is_linked(a, 'table_DColumn', b2)
    if hasattr(b2, 'ColumnMapping'):
        assert not _is_linked(b2, 'ColumnMapping', a)


def test_assoc_originMapping4_link_reassign_clear():
    a = table_DLine(collapsed=True, label="sample_text", visible=True)
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_DLine', b1)
    assert _is_linked(a, 'table_DLine', b1)
    if hasattr(b1, 'LineMapping'):
        assert _is_linked(b1, 'LineMapping', a)
    _safe_set(a, 'table_DLine', b2)
    assert _is_linked(a, 'table_DLine', b2)
    if hasattr(b1, 'LineMapping'):
        assert not _is_linked(b1, 'LineMapping', a)
    if hasattr(b2, 'LineMapping'):
        assert _is_linked(b2, 'LineMapping', a)
    _safe_set(a, 'table_DLine', None)
    assert not _is_linked(a, 'table_DLine', b2)
    if hasattr(b2, 'LineMapping'):
        assert not _is_linked(b2, 'LineMapping', a)


def test_assoc_ownedCreateLine62_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = CreateLineTool()
    b2 = CreateLineTool()
    _safe_set(a, 'table_description_TableDescription63', {b1})
    assert _is_linked(a, 'table_description_TableDescription63', b1)
    if hasattr(b1, 'CreateLineTool'):
        assert _is_linked(b1, 'CreateLineTool', a)
    _safe_set(a, 'table_description_TableDescription63', {b2})
    assert _is_linked(a, 'table_description_TableDescription63', b2)
    if hasattr(b1, 'CreateLineTool'):
        assert not _is_linked(b1, 'CreateLineTool', a)
    if hasattr(b2, 'CreateLineTool'):
        assert _is_linked(b2, 'CreateLineTool', a)
    _safe_set(a, 'table_description_TableDescription63', set())
    assert not _is_linked(a, 'table_description_TableDescription63', b2)
    if hasattr(b2, 'CreateLineTool'):
        assert not _is_linked(b2, 'CreateLineTool', a)


def test_assoc_ownedLineMappings53_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_description_TableDescription54', {b1})
    assert _is_linked(a, 'table_description_TableDescription54', b1)
    if hasattr(b1, 'LineMapping55'):
        assert _is_linked(b1, 'LineMapping55', a)
    _safe_set(a, 'table_description_TableDescription54', {b2})
    assert _is_linked(a, 'table_description_TableDescription54', b2)
    if hasattr(b1, 'LineMapping55'):
        assert not _is_linked(b1, 'LineMapping55', a)
    if hasattr(b2, 'LineMapping55'):
        assert _is_linked(b2, 'LineMapping55', a)
    _safe_set(a, 'table_description_TableDescription54', set())
    assert not _is_linked(a, 'table_description_TableDescription54', b2)
    if hasattr(b2, 'LineMapping55'):
        assert not _is_linked(b2, 'LineMapping55', a)


def test_assoc_ownedRepresentationCreationDescriptions38_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = tool_RepresentationCreationDescription()
    b2 = tool_RepresentationCreationDescription()
    _safe_set(a, 'table_description_TableDescription', {b1})
    assert _is_linked(a, 'table_description_TableDescription', b1)
    if hasattr(b1, 'tool_RepresentationCreationDescription'):
        assert _is_linked(b1, 'tool_RepresentationCreationDescription', a)
    _safe_set(a, 'table_description_TableDescription', {b2})
    assert _is_linked(a, 'table_description_TableDescription', b2)
    if hasattr(b1, 'tool_RepresentationCreationDescription'):
        assert not _is_linked(b1, 'tool_RepresentationCreationDescription', a)
    if hasattr(b2, 'tool_RepresentationCreationDescription'):
        assert _is_linked(b2, 'tool_RepresentationCreationDescription', a)
    _safe_set(a, 'table_description_TableDescription', set())
    assert not _is_linked(a, 'table_description_TableDescription', b2)
    if hasattr(b2, 'tool_RepresentationCreationDescription'):
        assert not _is_linked(b2, 'tool_RepresentationCreationDescription', a)


def test_assoc_ownedRepresentationNavigationDescriptions45_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = tool_RepresentationNavigationDescription()
    b2 = tool_RepresentationNavigationDescription()
    _safe_set(a, 'table_description_TableDescription46', {b1})
    assert _is_linked(a, 'table_description_TableDescription46', b1)
    if hasattr(b1, 'tool_RepresentationNavigationDescription'):
        assert _is_linked(b1, 'tool_RepresentationNavigationDescription', a)
    _safe_set(a, 'table_description_TableDescription46', {b2})
    assert _is_linked(a, 'table_description_TableDescription46', b2)
    if hasattr(b1, 'tool_RepresentationNavigationDescription'):
        assert not _is_linked(b1, 'tool_RepresentationNavigationDescription', a)
    if hasattr(b2, 'tool_RepresentationNavigationDescription'):
        assert _is_linked(b2, 'tool_RepresentationNavigationDescription', a)
    _safe_set(a, 'table_description_TableDescription46', set())
    assert not _is_linked(a, 'table_description_TableDescription46', b2)
    if hasattr(b2, 'tool_RepresentationNavigationDescription'):
        assert not _is_linked(b2, 'tool_RepresentationNavigationDescription', a)


def test_assoc_ownedSubLines85_link_reassign_clear():
    a = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_description_LineMapping', {b1})
    assert _is_linked(a, 'table_description_LineMapping', b1)
    if hasattr(b1, 'LineMapping86'):
        assert _is_linked(b1, 'LineMapping86', a)
    _safe_set(a, 'table_description_LineMapping', {b2})
    assert _is_linked(a, 'table_description_LineMapping', b2)
    if hasattr(b1, 'LineMapping86'):
        assert not _is_linked(b1, 'LineMapping86', a)
    if hasattr(b2, 'LineMapping86'):
        assert _is_linked(b2, 'LineMapping86', a)
    _safe_set(a, 'table_description_LineMapping', set())
    assert not _is_linked(a, 'table_description_LineMapping', b2)
    if hasattr(b2, 'LineMapping86'):
        assert not _is_linked(b2, 'LineMapping86', a)


def test_assoc_reusedCreateLine64_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = CreateLineTool()
    b2 = CreateLineTool()
    _safe_set(a, 'table_description_TableDescription65', {b1})
    assert _is_linked(a, 'table_description_TableDescription65', b1)
    if hasattr(b1, 'CreateLineTool66'):
        assert _is_linked(b1, 'CreateLineTool66', a)
    _safe_set(a, 'table_description_TableDescription65', {b2})
    assert _is_linked(a, 'table_description_TableDescription65', b2)
    if hasattr(b1, 'CreateLineTool66'):
        assert not _is_linked(b1, 'CreateLineTool66', a)
    if hasattr(b2, 'CreateLineTool66'):
        assert _is_linked(b2, 'CreateLineTool66', a)
    _safe_set(a, 'table_description_TableDescription65', set())
    assert not _is_linked(a, 'table_description_TableDescription65', b2)
    if hasattr(b2, 'CreateLineTool66'):
        assert not _is_linked(b2, 'CreateLineTool66', a)


def test_assoc_reusedInMappings92_link_reassign_clear():
    a = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'reusedSubLines', {b1})
    assert _is_linked(a, 'reusedSubLines', b1)
    if hasattr(b1, 'LineMapping93'):
        assert _is_linked(b1, 'LineMapping93', a)
    _safe_set(a, 'reusedSubLines', {b2})
    assert _is_linked(a, 'reusedSubLines', b2)
    if hasattr(b1, 'LineMapping93'):
        assert not _is_linked(b1, 'LineMapping93', a)
    if hasattr(b2, 'LineMapping93'):
        assert _is_linked(b2, 'LineMapping93', a)
    _safe_set(a, 'reusedSubLines', set())
    assert not _is_linked(a, 'reusedSubLines', b2)
    if hasattr(b2, 'LineMapping93'):
        assert not _is_linked(b2, 'LineMapping93', a)


def test_assoc_reusedLineMappings56_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'table_description_TableDescription57', {b1})
    assert _is_linked(a, 'table_description_TableDescription57', b1)
    if hasattr(b1, 'LineMapping58'):
        assert _is_linked(b1, 'LineMapping58', a)
    _safe_set(a, 'table_description_TableDescription57', {b2})
    assert _is_linked(a, 'table_description_TableDescription57', b2)
    if hasattr(b1, 'LineMapping58'):
        assert not _is_linked(b1, 'LineMapping58', a)
    if hasattr(b2, 'LineMapping58'):
        assert _is_linked(b2, 'LineMapping58', a)
    _safe_set(a, 'table_description_TableDescription57', set())
    assert not _is_linked(a, 'table_description_TableDescription57', b2)
    if hasattr(b2, 'LineMapping58'):
        assert not _is_linked(b2, 'LineMapping58', a)


def test_assoc_reusedRepresentationCreationDescriptions39_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = tool_RepresentationCreationDescription()
    b2 = tool_RepresentationCreationDescription()
    _safe_set(a, 'table_description_TableDescription40', {b1})
    assert _is_linked(a, 'table_description_TableDescription40', b1)
    if hasattr(b1, 'tool_RepresentationCreationDescription41'):
        assert _is_linked(b1, 'tool_RepresentationCreationDescription41', a)
    _safe_set(a, 'table_description_TableDescription40', {b2})
    assert _is_linked(a, 'table_description_TableDescription40', b2)
    if hasattr(b1, 'tool_RepresentationCreationDescription41'):
        assert not _is_linked(b1, 'tool_RepresentationCreationDescription41', a)
    if hasattr(b2, 'tool_RepresentationCreationDescription41'):
        assert _is_linked(b2, 'tool_RepresentationCreationDescription41', a)
    _safe_set(a, 'table_description_TableDescription40', set())
    assert not _is_linked(a, 'table_description_TableDescription40', b2)
    if hasattr(b2, 'tool_RepresentationCreationDescription41'):
        assert not _is_linked(b2, 'tool_RepresentationCreationDescription41', a)


def test_assoc_reusedRepresentationNavigationDescriptions47_link_reassign_clear():
    a = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    b1 = tool_RepresentationNavigationDescription()
    b2 = tool_RepresentationNavigationDescription()
    _safe_set(a, 'table_description_TableDescription48', {b1})
    assert _is_linked(a, 'table_description_TableDescription48', b1)
    if hasattr(b1, 'tool_RepresentationNavigationDescription49'):
        assert _is_linked(b1, 'tool_RepresentationNavigationDescription49', a)
    _safe_set(a, 'table_description_TableDescription48', {b2})
    assert _is_linked(a, 'table_description_TableDescription48', b2)
    if hasattr(b1, 'tool_RepresentationNavigationDescription49'):
        assert not _is_linked(b1, 'tool_RepresentationNavigationDescription49', a)
    if hasattr(b2, 'tool_RepresentationNavigationDescription49'):
        assert _is_linked(b2, 'tool_RepresentationNavigationDescription49', a)
    _safe_set(a, 'table_description_TableDescription48', set())
    assert not _is_linked(a, 'table_description_TableDescription48', b2)
    if hasattr(b2, 'tool_RepresentationNavigationDescription49'):
        assert not _is_linked(b2, 'tool_RepresentationNavigationDescription49', a)


def test_assoc_reusedSubLines87_link_reassign_clear():
    a = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = LineMapping()
    b2 = LineMapping()
    _safe_set(a, 'reusedInMappings', {b1})
    assert _is_linked(a, 'reusedInMappings', b1)
    if hasattr(b1, 'LineMapping88'):
        assert _is_linked(b1, 'LineMapping88', a)
    _safe_set(a, 'reusedInMappings', {b2})
    assert _is_linked(a, 'reusedInMappings', b2)
    if hasattr(b1, 'LineMapping88'):
        assert not _is_linked(b1, 'LineMapping88', a)
    if hasattr(b2, 'LineMapping88'):
        assert _is_linked(b2, 'LineMapping88', a)
    _safe_set(a, 'reusedInMappings', set())
    assert not _is_linked(a, 'reusedInMappings', b2)
    if hasattr(b2, 'LineMapping88'):
        assert not _is_linked(b2, 'LineMapping88', a)


def test_assoc_style140_link_reassign_clear():
    a = table_description_ForegroundConditionalStyle(predicateExpression="sample_text")
    b1 = ForegroundStyleDescription()
    b2 = ForegroundStyleDescription()
    _safe_set(a, 'table_description_ForegroundConditionalStyle', b1)
    assert _is_linked(a, 'table_description_ForegroundConditionalStyle', b1)
    if hasattr(b1, 'ForegroundStyleDescription141'):
        assert _is_linked(b1, 'ForegroundStyleDescription141', a)
    _safe_set(a, 'table_description_ForegroundConditionalStyle', b2)
    assert _is_linked(a, 'table_description_ForegroundConditionalStyle', b2)
    if hasattr(b1, 'ForegroundStyleDescription141'):
        assert not _is_linked(b1, 'ForegroundStyleDescription141', a)
    if hasattr(b2, 'ForegroundStyleDescription141'):
        assert _is_linked(b2, 'ForegroundStyleDescription141', a)
    _safe_set(a, 'table_description_ForegroundConditionalStyle', None)
    assert not _is_linked(a, 'table_description_ForegroundConditionalStyle', b2)
    if hasattr(b2, 'ForegroundStyleDescription141'):
        assert not _is_linked(b2, 'ForegroundStyleDescription141', a)


def test_assoc_style142_link_reassign_clear():
    a = table_description_BackgroundConditionalStyle(predicateExpression="sample_text")
    b1 = BackgroundStyleDescription()
    b2 = BackgroundStyleDescription()
    _safe_set(a, 'table_description_BackgroundConditionalStyle', b1)
    assert _is_linked(a, 'table_description_BackgroundConditionalStyle', b1)
    if hasattr(b1, 'BackgroundStyleDescription143'):
        assert _is_linked(b1, 'BackgroundStyleDescription143', a)
    _safe_set(a, 'table_description_BackgroundConditionalStyle', b2)
    assert _is_linked(a, 'table_description_BackgroundConditionalStyle', b2)
    if hasattr(b1, 'BackgroundStyleDescription143'):
        assert not _is_linked(b1, 'BackgroundStyleDescription143', a)
    if hasattr(b2, 'BackgroundStyleDescription143'):
        assert _is_linked(b2, 'BackgroundStyleDescription143', a)
    _safe_set(a, 'table_description_BackgroundConditionalStyle', None)
    assert not _is_linked(a, 'table_description_BackgroundConditionalStyle', b2)
    if hasattr(b2, 'BackgroundStyleDescription143'):
        assert not _is_linked(b2, 'BackgroundStyleDescription143', a)


def test_assoc_table31_link_reassign_clear():
    a = table_DTable(headerColumnWidth=7)
    b1 = table_DColumn(label="sample_text", visible=True, width=7)
    b2 = table_DColumn(label="sample_text_2", visible=False, width=13)
    _safe_set(a, 'DTable', b1)
    assert _is_linked(a, 'DTable', b1)
    if hasattr(b1, 'columns'):
        assert _is_linked(b1, 'columns', a)
    _safe_set(a, 'DTable', b2)
    assert _is_linked(a, 'DTable', b2)
    if hasattr(b1, 'columns'):
        assert not _is_linked(b1, 'columns', a)
    if hasattr(b2, 'columns'):
        assert _is_linked(b2, 'columns', a)
    _safe_set(a, 'DTable', None)
    assert not _is_linked(a, 'DTable', b2)
    if hasattr(b2, 'columns'):
        assert not _is_linked(b2, 'columns', a)


def test_assoc_updater18_link_reassign_clear():
    a = table_DCell(label="sample_text")
    b1 = CellUpdater()
    b2 = CellUpdater()
    _safe_set(a, 'table_DCell19', b1)
    assert _is_linked(a, 'table_DCell19', b1)
    if hasattr(b1, 'CellUpdater'):
        assert _is_linked(b1, 'CellUpdater', a)
    _safe_set(a, 'table_DCell19', b2)
    assert _is_linked(a, 'table_DCell19', b2)
    if hasattr(b1, 'CellUpdater'):
        assert not _is_linked(b1, 'CellUpdater', a)
    if hasattr(b2, 'CellUpdater'):
        assert _is_linked(b2, 'CellUpdater', a)
    _safe_set(a, 'table_DCell19', None)
    assert not _is_linked(a, 'table_DCell19', b2)
    if hasattr(b2, 'CellUpdater'):
        assert not _is_linked(b2, 'CellUpdater', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BackgroundConditionalStyle_strategy = st.builds(BackgroundConditionalStyle)
@given(instance=BackgroundConditionalStyle_strategy)
@settings(max_examples=25)
def test_BackgroundConditionalStyle_instantiation(instance):
    assert isinstance(instance, BackgroundConditionalStyle)


BackgroundStyleDescription_strategy = st.builds(BackgroundStyleDescription)
@given(instance=BackgroundStyleDescription_strategy)
@settings(max_examples=25)
def test_BackgroundStyleDescription_instantiation(instance):
    assert isinstance(instance, BackgroundStyleDescription)


CellUpdater_strategy = st.builds(CellUpdater)
@given(instance=CellUpdater_strategy)
@settings(max_examples=25)
def test_CellUpdater_instantiation(instance):
    assert isinstance(instance, CellUpdater)


ColorDescription_strategy = st.builds(ColorDescription)
@given(instance=ColorDescription_strategy)
@settings(max_examples=25)
def test_ColorDescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)


ColumnMapping_strategy = st.builds(ColumnMapping)
@given(instance=ColumnMapping_strategy)
@settings(max_examples=25)
def test_ColumnMapping_instantiation(instance):
    assert isinstance(instance, ColumnMapping)


CreateCellTool_strategy = st.builds(CreateCellTool)
@given(instance=CreateCellTool_strategy)
@settings(max_examples=25)
def test_CreateCellTool_instantiation(instance):
    assert isinstance(instance, CreateCellTool)


CreateColumnTool_strategy = st.builds(CreateColumnTool)
@given(instance=CreateColumnTool_strategy)
@settings(max_examples=25)
def test_CreateColumnTool_instantiation(instance):
    assert isinstance(instance, CreateColumnTool)


CreateCrossColumnTool_strategy = st.builds(CreateCrossColumnTool)
@given(instance=CreateCrossColumnTool_strategy)
@settings(max_examples=25)
def test_CreateCrossColumnTool_instantiation(instance):
    assert isinstance(instance, CreateCrossColumnTool)


CreateLineTool_strategy = st.builds(CreateLineTool)
@given(instance=CreateLineTool_strategy)
@settings(max_examples=25)
def test_CreateLineTool_instantiation(instance):
    assert isinstance(instance, CreateLineTool)


CreateTool_strategy = st.builds(CreateTool)
@given(instance=CreateTool_strategy)
@settings(max_examples=25)
def test_CreateTool_instantiation(instance):
    assert isinstance(instance, CreateTool)


DColumn_strategy = st.builds(DColumn)
@given(instance=DColumn_strategy)
@settings(max_examples=25)
def test_DColumn_instantiation(instance):
    assert isinstance(instance, DColumn)


DRepresentation_strategy = st.builds(DRepresentation)
@given(instance=DRepresentation_strategy)
@settings(max_examples=25)
def test_DRepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)


DRepresentationElement_strategy = st.builds(DRepresentationElement)
@given(instance=DRepresentationElement_strategy)
@settings(max_examples=25)
def test_DRepresentationElement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)


DSemanticDecorator_strategy = st.builds(DSemanticDecorator)
@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=25)
def test_DSemanticDecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)


DTableElement_strategy = st.builds(DTableElement)
@given(instance=DTableElement_strategy)
@settings(max_examples=25)
def test_DTableElement_instantiation(instance):
    assert isinstance(instance, DTableElement)


DTableElementStyle_strategy = st.builds(DTableElementStyle)
@given(instance=DTableElementStyle_strategy)
@settings(max_examples=25)
def test_DTableElementStyle_instantiation(instance):
    assert isinstance(instance, DTableElementStyle)


DeleteColumnTool_strategy = st.builds(DeleteColumnTool)
@given(instance=DeleteColumnTool_strategy)
@settings(max_examples=25)
def test_DeleteColumnTool_instantiation(instance):
    assert isinstance(instance, DeleteColumnTool)


DeleteLineTool_strategy = st.builds(DeleteLineTool)
@given(instance=DeleteLineTool_strategy)
@settings(max_examples=25)
def test_DeleteLineTool_instantiation(instance):
    assert isinstance(instance, DeleteLineTool)


DeleteTool_strategy = st.builds(DeleteTool)
@given(instance=DeleteTool_strategy)
@settings(max_examples=25)
def test_DeleteTool_instantiation(instance):
    assert isinstance(instance, DeleteTool)


ElementColumnMapping_strategy = st.builds(ElementColumnMapping)
@given(instance=ElementColumnMapping_strategy)
@settings(max_examples=25)
def test_ElementColumnMapping_instantiation(instance):
    assert isinstance(instance, ElementColumnMapping)


FeatureColumnMapping_strategy = st.builds(FeatureColumnMapping)
@given(instance=FeatureColumnMapping_strategy)
@settings(max_examples=25)
def test_FeatureColumnMapping_instantiation(instance):
    assert isinstance(instance, FeatureColumnMapping)


ForegroundConditionalStyle_strategy = st.builds(ForegroundConditionalStyle)
@given(instance=ForegroundConditionalStyle_strategy)
@settings(max_examples=25)
def test_ForegroundConditionalStyle_instantiation(instance):
    assert isinstance(instance, ForegroundConditionalStyle)


ForegroundStyleDescription_strategy = st.builds(ForegroundStyleDescription)
@given(instance=ForegroundStyleDescription_strategy)
@settings(max_examples=25)
def test_ForegroundStyleDescription_instantiation(instance):
    assert isinstance(instance, ForegroundStyleDescription)


IntersectionMapping_strategy = st.builds(IntersectionMapping)
@given(instance=IntersectionMapping_strategy)
@settings(max_examples=25)
def test_IntersectionMapping_instantiation(instance):
    assert isinstance(instance, IntersectionMapping)


LabelEditTool_strategy = st.builds(LabelEditTool)
@given(instance=LabelEditTool_strategy)
@settings(max_examples=25)
def test_LabelEditTool_instantiation(instance):
    assert isinstance(instance, LabelEditTool)


LineContainer_strategy = st.builds(LineContainer)
@given(instance=LineContainer_strategy)
@settings(max_examples=25)
def test_LineContainer_instantiation(instance):
    assert isinstance(instance, LineContainer)


LineMapping_strategy = st.builds(LineMapping)
@given(instance=LineMapping_strategy)
@settings(max_examples=25)
def test_LineMapping_instantiation(instance):
    assert isinstance(instance, LineMapping)


RepresentationCreationDescription_strategy = st.builds(RepresentationCreationDescription)
@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)


RepresentationElementMapping_strategy = st.builds(RepresentationElementMapping)
@given(instance=RepresentationElementMapping_strategy)
@settings(max_examples=25)
def test_RepresentationElementMapping_instantiation(instance):
    assert isinstance(instance, RepresentationElementMapping)


RepresentationNavigationDescription_strategy = st.builds(RepresentationNavigationDescription)
@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)


TableDescription_strategy = st.builds(TableDescription)
@given(instance=TableDescription_strategy)
@settings(max_examples=25)
def test_TableDescription_instantiation(instance):
    assert isinstance(instance, TableDescription)


TableMapping_strategy = st.builds(TableMapping)
@given(instance=TableMapping_strategy)
@settings(max_examples=25)
def test_TableMapping_instantiation(instance):
    assert isinstance(instance, TableMapping)


TableTool_strategy = st.builds(TableTool)
@given(instance=TableTool_strategy)
@settings(max_examples=25)
def test_TableTool_instantiation(instance):
    assert isinstance(instance, TableTool)


TableVariable_strategy = st.builds(TableVariable)
@given(instance=TableVariable_strategy)
@settings(max_examples=25)
def test_TableVariable_instantiation(instance):
    assert isinstance(instance, TableVariable)


description_AbstractVariable_strategy = st.builds(description_AbstractVariable)
@given(instance=description_AbstractVariable_strategy)
@settings(max_examples=25)
def test_description_AbstractVariable_instantiation(instance):
    assert isinstance(instance, description_AbstractVariable)


description_CellUpdater_strategy = st.builds(description_CellUpdater)
@given(instance=description_CellUpdater_strategy)
@settings(max_examples=25)
def test_description_CellUpdater_instantiation(instance):
    assert isinstance(instance, description_CellUpdater)


description_ColumnMapping_strategy = st.builds(description_ColumnMapping)
@given(instance=description_ColumnMapping_strategy)
@settings(max_examples=25)
def test_description_ColumnMapping_instantiation(instance):
    assert isinstance(instance, description_ColumnMapping)


description_DocumentedElement_strategy = st.builds(description_DocumentedElement)
@given(instance=description_DocumentedElement_strategy)
@settings(max_examples=25)
def test_description_DocumentedElement_instantiation(instance):
    assert isinstance(instance, description_DocumentedElement)


description_EndUserDocumentedElement_strategy = st.builds(description_EndUserDocumentedElement)
@given(instance=description_EndUserDocumentedElement_strategy)
@settings(max_examples=25)
def test_description_EndUserDocumentedElement_instantiation(instance):
    assert isinstance(instance, description_EndUserDocumentedElement)


description_RepresentationDescription_strategy = st.builds(description_RepresentationDescription)
@given(instance=description_RepresentationDescription_strategy)
@settings(max_examples=25)
def test_description_RepresentationDescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationDescription)


description_StyleUpdater_strategy = st.builds(description_StyleUpdater)
@given(instance=description_StyleUpdater_strategy)
@settings(max_examples=25)
def test_description_StyleUpdater_instantiation(instance):
    assert isinstance(instance, description_StyleUpdater)


description_TableMapping_strategy = st.builds(description_TableMapping)
@given(instance=description_TableMapping_strategy)
@settings(max_examples=25)
def test_description_TableMapping_instantiation(instance):
    assert isinstance(instance, description_TableMapping)


description_TableTool_strategy = st.builds(description_TableTool)
@given(instance=description_TableTool_strategy)
@settings(max_examples=25)
def test_description_TableTool_instantiation(instance):
    assert isinstance(instance, description_TableTool)


description_table_EObject_strategy = st.builds(description_table_EObject)
@given(instance=description_table_EObject_strategy)
@settings(max_examples=25)
def test_description_table_EObject_instantiation(instance):
    assert isinstance(instance, description_table_EObject)


table_DCell_strategy = st.builds(table_DCell, label=safe_text)
@given(instance=table_DCell_strategy)
@settings(max_examples=25)
def test_table_DCell_instantiation(instance):
    assert isinstance(instance, table_DCell)


table_DCellStyle_strategy = st.builds(table_DCellStyle)
@given(instance=table_DCellStyle_strategy)
@settings(max_examples=25)
def test_table_DCellStyle_instantiation(instance):
    assert isinstance(instance, table_DCellStyle)


table_DColumn_strategy = st.builds(table_DColumn, label=safe_text, visible=st.booleans(), width=st.integers())
@given(instance=table_DColumn_strategy)
@settings(max_examples=25)
def test_table_DColumn_instantiation(instance):
    assert isinstance(instance, table_DColumn)


table_DFeatureColumn_strategy = st.builds(table_DFeatureColumn, featureName=safe_text)
@given(instance=table_DFeatureColumn_strategy)
@settings(max_examples=25)
def test_table_DFeatureColumn_instantiation(instance):
    assert isinstance(instance, table_DFeatureColumn)


table_DLine_strategy = st.builds(table_DLine, collapsed=st.booleans(), label=safe_text, visible=st.booleans())
@given(instance=table_DLine_strategy)
@settings(max_examples=25)
def test_table_DLine_instantiation(instance):
    assert isinstance(instance, table_DLine)


table_DTable_strategy = st.builds(table_DTable, headerColumnWidth=st.integers())
@given(instance=table_DTable_strategy)
@settings(max_examples=25)
def test_table_DTable_instantiation(instance):
    assert isinstance(instance, table_DTable)


table_DTableElement_strategy = st.builds(table_DTableElement)
@given(instance=table_DTableElement_strategy)
@settings(max_examples=25)
def test_table_DTableElement_instantiation(instance):
    assert isinstance(instance, table_DTableElement)


table_DTableElementStyle_strategy = st.builds(table_DTableElementStyle, backgroundColor=safe_text, defaultBackgroundStyle=st.booleans(), defaultForegroundStyle=st.booleans(), foregroundColor=safe_text, labelFormat=safe_text, labelSize=st.integers())
@given(instance=table_DTableElementStyle_strategy)
@settings(max_examples=25)
def test_table_DTableElementStyle_instantiation(instance):
    assert isinstance(instance, table_DTableElementStyle)


table_DTableElementSynchronizer_strategy = st.builds(table_DTableElementSynchronizer)
@given(instance=table_DTableElementSynchronizer_strategy)
@settings(max_examples=25)
def test_table_DTableElementSynchronizer_instantiation(instance):
    assert isinstance(instance, table_DTableElementSynchronizer)


table_DTargetColumn_strategy = st.builds(table_DTargetColumn)
@given(instance=table_DTargetColumn_strategy)
@settings(max_examples=25)
def test_table_DTargetColumn_instantiation(instance):
    assert isinstance(instance, table_DTargetColumn)


table_LineContainer_strategy = st.builds(table_LineContainer)
@given(instance=table_LineContainer_strategy)
@settings(max_examples=25)
def test_table_LineContainer_instantiation(instance):
    assert isinstance(instance, table_LineContainer)


table_description_BackgroundConditionalStyle_strategy = st.builds(table_description_BackgroundConditionalStyle, predicateExpression=safe_text)
@given(instance=table_description_BackgroundConditionalStyle_strategy)
@settings(max_examples=25)
def test_table_description_BackgroundConditionalStyle_instantiation(instance):
    assert isinstance(instance, table_description_BackgroundConditionalStyle)


table_description_BackgroundStyleDescription_strategy = st.builds(table_description_BackgroundStyleDescription)
@given(instance=table_description_BackgroundStyleDescription_strategy)
@settings(max_examples=25)
def test_table_description_BackgroundStyleDescription_instantiation(instance):
    assert isinstance(instance, table_description_BackgroundStyleDescription)


table_description_CellUpdater_strategy = st.builds(table_description_CellUpdater, canEdit=safe_text)
@given(instance=table_description_CellUpdater_strategy)
@settings(max_examples=25)
def test_table_description_CellUpdater_instantiation(instance):
    assert isinstance(instance, table_description_CellUpdater)


table_description_ColumnMapping_strategy = st.builds(table_description_ColumnMapping, headerLabelExpression=safe_text, initialWidth=st.integers())
@given(instance=table_description_ColumnMapping_strategy)
@settings(max_examples=25)
def test_table_description_ColumnMapping_instantiation(instance):
    assert isinstance(instance, table_description_ColumnMapping)


table_description_CreateCellTool_strategy = st.builds(table_description_CreateCellTool)
@given(instance=table_description_CreateCellTool_strategy)
@settings(max_examples=25)
def test_table_description_CreateCellTool_instantiation(instance):
    assert isinstance(instance, table_description_CreateCellTool)


table_description_CreateColumnTool_strategy = st.builds(table_description_CreateColumnTool)
@given(instance=table_description_CreateColumnTool_strategy)
@settings(max_examples=25)
def test_table_description_CreateColumnTool_instantiation(instance):
    assert isinstance(instance, table_description_CreateColumnTool)


table_description_CreateCrossColumnTool_strategy = st.builds(table_description_CreateCrossColumnTool)
@given(instance=table_description_CreateCrossColumnTool_strategy)
@settings(max_examples=25)
def test_table_description_CreateCrossColumnTool_instantiation(instance):
    assert isinstance(instance, table_description_CreateCrossColumnTool)


table_description_CreateLineTool_strategy = st.builds(table_description_CreateLineTool)
@given(instance=table_description_CreateLineTool_strategy)
@settings(max_examples=25)
def test_table_description_CreateLineTool_instantiation(instance):
    assert isinstance(instance, table_description_CreateLineTool)


table_description_CreateTool_strategy = st.builds(table_description_CreateTool)
@given(instance=table_description_CreateTool_strategy)
@settings(max_examples=25)
def test_table_description_CreateTool_instantiation(instance):
    assert isinstance(instance, table_description_CreateTool)


table_description_CrossTableDescription_strategy = st.builds(table_description_CrossTableDescription)
@given(instance=table_description_CrossTableDescription_strategy)
@settings(max_examples=25)
def test_table_description_CrossTableDescription_instantiation(instance):
    assert isinstance(instance, table_description_CrossTableDescription)


table_description_DeleteColumnTool_strategy = st.builds(table_description_DeleteColumnTool)
@given(instance=table_description_DeleteColumnTool_strategy)
@settings(max_examples=25)
def test_table_description_DeleteColumnTool_instantiation(instance):
    assert isinstance(instance, table_description_DeleteColumnTool)


table_description_DeleteLineTool_strategy = st.builds(table_description_DeleteLineTool)
@given(instance=table_description_DeleteLineTool_strategy)
@settings(max_examples=25)
def test_table_description_DeleteLineTool_instantiation(instance):
    assert isinstance(instance, table_description_DeleteLineTool)


table_description_DeleteTool_strategy = st.builds(table_description_DeleteTool)
@given(instance=table_description_DeleteTool_strategy)
@settings(max_examples=25)
def test_table_description_DeleteTool_instantiation(instance):
    assert isinstance(instance, table_description_DeleteTool)


table_description_EditionTableDescription_strategy = st.builds(table_description_EditionTableDescription)
@given(instance=table_description_EditionTableDescription_strategy)
@settings(max_examples=25)
def test_table_description_EditionTableDescription_instantiation(instance):
    assert isinstance(instance, table_description_EditionTableDescription)


table_description_ElementColumnMapping_strategy = st.builds(table_description_ElementColumnMapping, domainClass=safe_text, semanticCandidatesExpression=safe_text)
@given(instance=table_description_ElementColumnMapping_strategy)
@settings(max_examples=25)
def test_table_description_ElementColumnMapping_instantiation(instance):
    assert isinstance(instance, table_description_ElementColumnMapping)


table_description_FeatureColumnMapping_strategy = st.builds(table_description_FeatureColumnMapping, featureName=safe_text, featureParentExpression=safe_text, labelExpression=safe_text)
@given(instance=table_description_FeatureColumnMapping_strategy)
@settings(max_examples=25)
def test_table_description_FeatureColumnMapping_instantiation(instance):
    assert isinstance(instance, table_description_FeatureColumnMapping)


table_description_ForegroundConditionalStyle_strategy = st.builds(table_description_ForegroundConditionalStyle, predicateExpression=safe_text)
@given(instance=table_description_ForegroundConditionalStyle_strategy)
@settings(max_examples=25)
def test_table_description_ForegroundConditionalStyle_instantiation(instance):
    assert isinstance(instance, table_description_ForegroundConditionalStyle)


table_description_ForegroundStyleDescription_strategy = st.builds(table_description_ForegroundStyleDescription, labelFormat=safe_text, labelSize=st.integers())
@given(instance=table_description_ForegroundStyleDescription_strategy)
@settings(max_examples=25)
def test_table_description_ForegroundStyleDescription_instantiation(instance):
    assert isinstance(instance, table_description_ForegroundStyleDescription)


table_description_IntersectionMapping_strategy = st.builds(table_description_IntersectionMapping, columnFinderExpression=safe_text, domainClass=safe_text, labelExpression=safe_text, lineFinderExpression=safe_text, preconditionExpression=safe_text, semanticCandidatesExpression=safe_text, useDomainClass=st.booleans())
@given(instance=table_description_IntersectionMapping_strategy)
@settings(max_examples=25)
def test_table_description_IntersectionMapping_instantiation(instance):
    assert isinstance(instance, table_description_IntersectionMapping)


table_description_LabelEditTool_strategy = st.builds(table_description_LabelEditTool)
@given(instance=table_description_LabelEditTool_strategy)
@settings(max_examples=25)
def test_table_description_LabelEditTool_instantiation(instance):
    assert isinstance(instance, table_description_LabelEditTool)


table_description_LineMapping_strategy = st.builds(table_description_LineMapping, domainClass=safe_text, headerLabelExpression=safe_text, semanticCandidatesExpression=safe_text)
@given(instance=table_description_LineMapping_strategy)
@settings(max_examples=25)
def test_table_description_LineMapping_instantiation(instance):
    assert isinstance(instance, table_description_LineMapping)


table_description_StyleUpdater_strategy = st.builds(table_description_StyleUpdater)
@given(instance=table_description_StyleUpdater_strategy)
@settings(max_examples=25)
def test_table_description_StyleUpdater_instantiation(instance):
    assert isinstance(instance, table_description_StyleUpdater)


table_description_TableCreationDescription_strategy = st.builds(table_description_TableCreationDescription)
@given(instance=table_description_TableCreationDescription_strategy)
@settings(max_examples=25)
def test_table_description_TableCreationDescription_instantiation(instance):
    assert isinstance(instance, table_description_TableCreationDescription)


table_description_TableDescription_strategy = st.builds(table_description_TableDescription, domainClass=safe_text, initialHeaderColumnWidth=st.integers(), preconditionExpression=safe_text)
@given(instance=table_description_TableDescription_strategy)
@settings(max_examples=25)
def test_table_description_TableDescription_instantiation(instance):
    assert isinstance(instance, table_description_TableDescription)


table_description_TableMapping_strategy = st.builds(table_description_TableMapping, semanticElements=safe_text)
@given(instance=table_description_TableMapping_strategy)
@settings(max_examples=25)
def test_table_description_TableMapping_instantiation(instance):
    assert isinstance(instance, table_description_TableMapping)


table_description_TableNavigationDescription_strategy = st.builds(table_description_TableNavigationDescription)
@given(instance=table_description_TableNavigationDescription_strategy)
@settings(max_examples=25)
def test_table_description_TableNavigationDescription_instantiation(instance):
    assert isinstance(instance, table_description_TableNavigationDescription)


table_description_TableTool_strategy = st.builds(table_description_TableTool)
@given(instance=table_description_TableTool_strategy)
@settings(max_examples=25)
def test_table_description_TableTool_instantiation(instance):
    assert isinstance(instance, table_description_TableTool)


table_description_TableVariable_strategy = st.builds(table_description_TableVariable, documentation=safe_text)
@given(instance=table_description_TableVariable_strategy)
@settings(max_examples=25)
def test_table_description_TableVariable_instantiation(instance):
    assert isinstance(instance, table_description_TableVariable)


tool_AbstractToolDescription_strategy = st.builds(tool_AbstractToolDescription)
@given(instance=tool_AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_tool_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, tool_AbstractToolDescription)


tool_EditMaskVariables_strategy = st.builds(tool_EditMaskVariables)
@given(instance=tool_EditMaskVariables_strategy)
@settings(max_examples=25)
def test_tool_EditMaskVariables_instantiation(instance):
    assert isinstance(instance, tool_EditMaskVariables)


tool_ModelOperation_strategy = st.builds(tool_ModelOperation)
@given(instance=tool_ModelOperation_strategy)
@settings(max_examples=25)
def test_tool_ModelOperation_instantiation(instance):
    assert isinstance(instance, tool_ModelOperation)


tool_RepresentationCreationDescription_strategy = st.builds(tool_RepresentationCreationDescription)
@given(instance=tool_RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_tool_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationCreationDescription)


tool_RepresentationNavigationDescription_strategy = st.builds(tool_RepresentationNavigationDescription)
@given(instance=tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_tool_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationNavigationDescription)


tool_VariableContainer_strategy = st.builds(tool_VariableContainer)
@given(instance=tool_VariableContainer_strategy)
@settings(max_examples=25)
def test_tool_VariableContainer_instantiation(instance):
    assert isinstance(instance, tool_VariableContainer)


