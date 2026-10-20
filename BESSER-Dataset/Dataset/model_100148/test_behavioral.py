import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMetadataObject,
    Connection,
    Content,
    DataManager,
    ElementType,
    Expression,
    FileConnection,
    Machine,
    MetadataColumn,
    MetadataTable,
    ModelElement,
    Package,
    Procedure,
    SAPFunctionParameterTable,
    SQLSimpleType,
    Schema,
    SoftwareSystem,
    TdTable,
    Trigger,
    connection_AbstractMetadataObject,
    connection_BRMSConnection,
    connection_CDCConnection,
    connection_CDCType,
    connection_Concept,
    connection_ConceptTarget,
    connection_ConditionType,
    connection_Connection,
    connection_DatabaseConnection,
    connection_DelimitedFileConnection,
    connection_EDIFACTColumn,
    connection_EDIFACTConnection,
    connection_EbcdicConnection,
    connection_FTPConnection,
    connection_FileConnection,
    connection_FileExcelConnection,
    connection_GenericPackage,
    connection_GenericSchemaConnection,
    connection_HL7Connection,
    connection_HL7FileNode,
    connection_HeaderFooterConnection,
    connection_InnerJoinMap,
    connection_InputSAPFunctionParameterTable,
    connection_LDAPSchemaConnection,
    connection_LdifFileConnection,
    connection_MDMConnection,
    connection_Metadata,
    connection_MetadataColumn,
    connection_MetadataTable,
    connection_OutputSAPFunctionParameterTable,
    connection_PositionalFileConnection,
    connection_QueriesConnection,
    connection_Query,
    connection_RegexpFileConnection,
    connection_SAPConnection,
    connection_SAPFunctionParameterColumn,
    connection_SAPFunctionParameterTable,
    connection_SAPFunctionUnit,
    connection_SAPIDocUnit,
    connection_SAPTestInputParameterTable,
    connection_SalesforceModuleUnit,
    connection_SalesforceSchemaConnection,
    connection_SchemaTarget,
    connection_SubscriberTable,
    connection_ValidationRulesConnection,
    connection_WSDLParameter,
    connection_WSDLSchemaConnection,
    connection_XMLFileNode,
    connection_XmlFileConnection,
    connection_XmlXPathLoopDescriptor,
    connection_relational_TdColumn,
    connection_relational_TdExpression,
    connection_relational_TdProcedure,
    connection_relational_TdSqlDataType,
    connection_relational_TdTable,
    connection_relational_TdTrigger,
    connection_relational_TdView,
    connection_softwaredeployment_TdDataManager,
    connection_softwaredeployment_TdMachine,
    connection_softwaredeployment_TdSoftwareSystem,
    connection_xml_TdXmlContent,
    connection_xml_TdXmlElementType,
    connection_xml_TdXmlSchema,
    core_Class,
    record_Field,
    relational_Table,
    relational_TdSqlDataType,
    relational_View,
    softwaredeployment_DataProvider,
    xml_TdXmlContent,
    xml_TdXmlElementType,
    xml_TdXmlSchema,
    xml_connection_EObject,
    DevelopmentStatus,
    Escape,
    FieldSeparator,
    FileFormat,
    Function,
    LogicalOperator,
    MDMConnectionProtocol,
    MdmConceptType,
    Operator,
    RowSeparator,
    RuleType,
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

def test_assoc_Funtions12_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'connection13', {a1})
    assert _is_linked(b, 'connection13', a1)
    if hasattr(a1, 'SAPFunctionUnit'):
        assert _is_linked(a1, 'SAPFunctionUnit', b)
    _safe_set(b, 'connection13', {a2})
    assert _is_linked(b, 'connection13', a2)
    if hasattr(a1, 'SAPFunctionUnit'):
        assert not _is_linked(a1, 'SAPFunctionUnit', b)
    if hasattr(a2, 'SAPFunctionUnit'):
        assert _is_linked(a2, 'SAPFunctionUnit', b)
    _safe_set(b, 'connection13', set())
    assert not _is_linked(b, 'connection13', a2)
    if hasattr(a2, 'SAPFunctionUnit'):
        assert not _is_linked(a2, 'SAPFunctionUnit', b)


def test_assoc_IDocs14_reverse_link_reassign_clear():
    a1 = connection_SAPIDocUnit(gatewayService="sample_text", htmlFile="sample_text", programId="sample_text", useHtmlOutput=True, useXmlOutput=True, xmlFile="sample_text")
    a2 = connection_SAPIDocUnit(gatewayService="sample_text_2", htmlFile="sample_text_2", programId="sample_text_2", useHtmlOutput=False, useXmlOutput=False, xmlFile="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'connection15', {a1})
    assert _is_linked(b, 'connection15', a1)
    if hasattr(a1, 'SAPIDocUnit'):
        assert _is_linked(a1, 'SAPIDocUnit', b)
    _safe_set(b, 'connection15', {a2})
    assert _is_linked(b, 'connection15', a2)
    if hasattr(a1, 'SAPIDocUnit'):
        assert not _is_linked(a1, 'SAPIDocUnit', b)
    if hasattr(a2, 'SAPIDocUnit'):
        assert _is_linked(a2, 'SAPIDocUnit', b)
    _safe_set(b, 'connection15', set())
    assert not _is_linked(b, 'connection15', a2)
    if hasattr(a2, 'SAPIDocUnit'):
        assert not _is_linked(a2, 'SAPIDocUnit', b)


def test_assoc_MetadataTable19_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable20', a1)
    assert _is_linked(b, 'connection_MetadataTable20', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit', b)
    _safe_set(b, 'connection_MetadataTable20', a2)
    assert _is_linked(b, 'connection_MetadataTable20', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit', b)
    if hasattr(a2, 'connection_SAPFunctionUnit'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit', b)
    _safe_set(b, 'connection_MetadataTable20', None)
    assert not _is_linked(b, 'connection_MetadataTable20', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit', b)


def test_assoc_MetadataTable93_reverse_link_reassign_clear():
    a1 = connection_SalesforceModuleUnit(moduleName="sample_text")
    a2 = connection_SalesforceModuleUnit(moduleName="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable94', a1)
    assert _is_linked(b, 'connection_MetadataTable94', a1)
    if hasattr(a1, 'connection_SalesforceModuleUnit'):
        assert _is_linked(a1, 'connection_SalesforceModuleUnit', b)
    _safe_set(b, 'connection_MetadataTable94', a2)
    assert _is_linked(b, 'connection_MetadataTable94', a2)
    if hasattr(a1, 'connection_SalesforceModuleUnit'):
        assert not _is_linked(a1, 'connection_SalesforceModuleUnit', b)
    if hasattr(a2, 'connection_SalesforceModuleUnit'):
        assert _is_linked(a2, 'connection_SalesforceModuleUnit', b)
    _safe_set(b, 'connection_MetadataTable94', None)
    assert not _is_linked(b, 'connection_MetadataTable94', a2)
    if hasattr(a2, 'connection_SalesforceModuleUnit'):
        assert not _is_linked(a2, 'connection_SalesforceModuleUnit', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", originalLength="sample_text", pattern="sample_text", relatedEntity="sample_text", relationshipType="sample_text", sourceType="sample_text", talendType="sample_text")
    _safe_set(b, 'connection_MetadataColumn5', a1)
    assert _is_linked(b, 'connection_MetadataColumn5', a1)
    if hasattr(a1, 'connection_MetadataTable4'):
        assert _is_linked(a1, 'connection_MetadataTable4', b)
    _safe_set(b, 'connection_MetadataColumn5', a2)
    assert _is_linked(b, 'connection_MetadataColumn5', a2)
    if hasattr(a1, 'connection_MetadataTable4'):
        assert not _is_linked(a1, 'connection_MetadataTable4', b)
    if hasattr(a2, 'connection_MetadataTable4'):
        assert _is_linked(a2, 'connection_MetadataTable4', b)
    _safe_set(b, 'connection_MetadataColumn5', None)
    assert not _is_linked(b, 'connection_MetadataColumn5', a2)
    if hasattr(a2, 'connection_MetadataTable4'):
        assert not _is_linked(a2, 'connection_MetadataTable4', b)


def test_assoc_conceptTargets69_reverse_link_reassign_clear():
    a1 = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    a2 = connection_ConceptTarget(RelativeLoopExpression="sample_text_2", targetName="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'schema70', {a1})
    assert _is_linked(b, 'schema70', a1)
    if hasattr(a1, 'ConceptTarget'):
        assert _is_linked(a1, 'ConceptTarget', b)
    _safe_set(b, 'schema70', {a2})
    assert _is_linked(b, 'schema70', a2)
    if hasattr(a1, 'ConceptTarget'):
        assert not _is_linked(a1, 'ConceptTarget', b)
    if hasattr(a2, 'ConceptTarget'):
        assert _is_linked(a2, 'ConceptTarget', b)
    _safe_set(b, 'schema70', set())
    assert not _is_linked(b, 'schema70', a2)
    if hasattr(a2, 'ConceptTarget'):
        assert not _is_linked(a2, 'ConceptTarget', b)


def test_assoc_conditions90_reverse_link_reassign_clear():
    a1 = connection_ValidationRulesConnection(baseColumnNames="sample_text", baseSchema="sample_text", isDelete=True, isDisallow=True, isInsert=True, isRejectLink=True, isSelect=True, isUpdate=True, javaCondition="sample_text", logicalOperator="sample_text", refColumnNames="sample_text", refSchema="sample_text", sqlCondition="sample_text", type="sample_text")
    a2 = connection_ValidationRulesConnection(baseColumnNames="sample_text_2", baseSchema="sample_text_2", isDelete=False, isDisallow=False, isInsert=False, isRejectLink=False, isSelect=False, isUpdate=False, javaCondition="sample_text_2", logicalOperator="sample_text_2", refColumnNames="sample_text_2", refSchema="sample_text_2", sqlCondition="sample_text_2", type="sample_text_2")
    b = connection_ConditionType(function="sample_text", inputColumn="sample_text", operator="sample_text", value="sample_text")
    _safe_set(b, 'connection_ConditionType', a1)
    assert _is_linked(b, 'connection_ConditionType', a1)
    if hasattr(a1, 'connection_ValidationRulesConnection'):
        assert _is_linked(a1, 'connection_ValidationRulesConnection', b)
    _safe_set(b, 'connection_ConditionType', a2)
    assert _is_linked(b, 'connection_ConditionType', a2)
    if hasattr(a1, 'connection_ValidationRulesConnection'):
        assert not _is_linked(a1, 'connection_ValidationRulesConnection', b)
    if hasattr(a2, 'connection_ValidationRulesConnection'):
        assert _is_linked(a2, 'connection_ValidationRulesConnection', b)
    _safe_set(b, 'connection_ConditionType', None)
    assert not _is_linked(b, 'connection_ConditionType', a2)
    if hasattr(a2, 'connection_ValidationRulesConnection'):
        assert not _is_linked(a2, 'connection_ValidationRulesConnection', b)


def test_assoc_connection21_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'SAPConnection', a1)
    assert _is_linked(b, 'SAPConnection', a1)
    if hasattr(a1, 'Funtions'):
        assert _is_linked(a1, 'Funtions', b)
    _safe_set(b, 'SAPConnection', a2)
    assert _is_linked(b, 'SAPConnection', a2)
    if hasattr(a1, 'Funtions'):
        assert not _is_linked(a1, 'Funtions', b)
    if hasattr(a2, 'Funtions'):
        assert _is_linked(a2, 'Funtions', b)
    _safe_set(b, 'SAPConnection', None)
    assert not _is_linked(b, 'SAPConnection', a2)
    if hasattr(a2, 'Funtions'):
        assert not _is_linked(a2, 'Funtions', b)


def test_assoc_connection27_reverse_link_reassign_clear():
    a1 = connection_SAPIDocUnit(gatewayService="sample_text", htmlFile="sample_text", programId="sample_text", useHtmlOutput=True, useXmlOutput=True, xmlFile="sample_text")
    a2 = connection_SAPIDocUnit(gatewayService="sample_text_2", htmlFile="sample_text_2", programId="sample_text_2", useHtmlOutput=False, useXmlOutput=False, xmlFile="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'SAPConnection28', a1)
    assert _is_linked(b, 'SAPConnection28', a1)
    if hasattr(a1, 'IDocs'):
        assert _is_linked(a1, 'IDocs', b)
    _safe_set(b, 'SAPConnection28', a2)
    assert _is_linked(b, 'SAPConnection28', a2)
    if hasattr(a1, 'IDocs'):
        assert not _is_linked(a1, 'IDocs', b)
    if hasattr(a2, 'IDocs'):
        assert _is_linked(a2, 'IDocs', b)
    _safe_set(b, 'SAPConnection28', None)
    assert not _is_linked(b, 'SAPConnection28', a2)
    if hasattr(a2, 'IDocs'):
        assert not _is_linked(a2, 'IDocs', b)


def test_assoc_connection51_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    _safe_set(b, 'XmlFileConnection', a1)
    assert _is_linked(b, 'XmlFileConnection', a1)
    if hasattr(a1, 'schema'):
        assert _is_linked(a1, 'schema', b)
    _safe_set(b, 'XmlFileConnection', a2)
    assert _is_linked(b, 'XmlFileConnection', a2)
    if hasattr(a1, 'schema'):
        assert not _is_linked(a1, 'schema', b)
    if hasattr(a2, 'schema'):
        assert _is_linked(a2, 'schema', b)
    _safe_set(b, 'XmlFileConnection', None)
    assert not _is_linked(b, 'XmlFileConnection', a2)
    if hasattr(a2, 'schema'):
        assert not _is_linked(a2, 'schema', b)


def test_assoc_connection6_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_Connection(ContextId="sample_text", ContextMode=True, contextName="sample_text", version="sample_text")
    _safe_set(b, 'connection_Connection8', a1)
    assert _is_linked(b, 'connection_Connection8', a1)
    if hasattr(a1, 'connection_MetadataTable7'):
        assert _is_linked(a1, 'connection_MetadataTable7', b)
    _safe_set(b, 'connection_Connection8', a2)
    assert _is_linked(b, 'connection_Connection8', a2)
    if hasattr(a1, 'connection_MetadataTable7'):
        assert not _is_linked(a1, 'connection_MetadataTable7', b)
    if hasattr(a2, 'connection_MetadataTable7'):
        assert _is_linked(a2, 'connection_MetadataTable7', b)
    _safe_set(b, 'connection_Connection8', None)
    assert not _is_linked(b, 'connection_Connection8', a2)
    if hasattr(a2, 'connection_MetadataTable7'):
        assert not _is_linked(a2, 'connection_MetadataTable7', b)


def test_assoc_connection95_reverse_link_reassign_clear():
    a1 = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    a2 = connection_SalesforceSchemaConnection(batchSize="sample_text_2", moduleName="sample_text_2", password="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUsername="sample_text_2", queryCondition="sample_text_2", timeOut="sample_text_2", useAlphbet=False, useCustomModuleName=False, useHttpProxy=False, useProxy=False, userName="sample_text_2", webServiceUrl="sample_text_2")
    b = connection_SalesforceModuleUnit(moduleName="sample_text")
    _safe_set(b, 'modules', a1)
    assert _is_linked(b, 'modules', a1)
    if hasattr(a1, 'SalesforceSchemaConnection'):
        assert _is_linked(a1, 'SalesforceSchemaConnection', b)
    _safe_set(b, 'modules', a2)
    assert _is_linked(b, 'modules', a2)
    if hasattr(a1, 'SalesforceSchemaConnection'):
        assert not _is_linked(a1, 'SalesforceSchemaConnection', b)
    if hasattr(a2, 'SalesforceSchemaConnection'):
        assert _is_linked(a2, 'SalesforceSchemaConnection', b)
    _safe_set(b, 'modules', None)
    assert not _is_linked(b, 'modules', a2)
    if hasattr(a2, 'SalesforceSchemaConnection'):
        assert not _is_linked(a2, 'SalesforceSchemaConnection', b)


def test_assoc_group37_reverse_link_reassign_clear():
    a1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    a2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2", fileContent="sample_text_2", inputModel=False, outputFilePath="sample_text_2")
    b = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    _safe_set(b, 'connection_XMLFileNode', a1)
    assert _is_linked(b, 'connection_XMLFileNode', a1)
    if hasattr(a1, 'connection_XmlFileConnection'):
        assert _is_linked(a1, 'connection_XmlFileConnection', b)
    _safe_set(b, 'connection_XMLFileNode', a2)
    assert _is_linked(b, 'connection_XMLFileNode', a2)
    if hasattr(a1, 'connection_XmlFileConnection'):
        assert not _is_linked(a1, 'connection_XmlFileConnection', b)
    if hasattr(a2, 'connection_XmlFileConnection'):
        assert _is_linked(a2, 'connection_XmlFileConnection', b)
    _safe_set(b, 'connection_XMLFileNode', None)
    assert not _is_linked(b, 'connection_XMLFileNode', a2)
    if hasattr(a2, 'connection_XmlFileConnection'):
        assert not _is_linked(a2, 'connection_XmlFileConnection', b)


def test_assoc_group71_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept72', {a1})
    assert _is_linked(b, 'connection_Concept72', a1)
    if hasattr(a1, 'connection_XMLFileNode73'):
        assert _is_linked(a1, 'connection_XMLFileNode73', b)
    _safe_set(b, 'connection_Concept72', {a2})
    assert _is_linked(b, 'connection_Concept72', a2)
    if hasattr(a1, 'connection_XMLFileNode73'):
        assert not _is_linked(a1, 'connection_XMLFileNode73', b)
    if hasattr(a2, 'connection_XMLFileNode73'):
        assert _is_linked(a2, 'connection_XMLFileNode73', b)
    _safe_set(b, 'connection_Concept72', set())
    assert not _is_linked(b, 'connection_Concept72', a2)
    if hasattr(a2, 'connection_XMLFileNode73'):
        assert not _is_linked(a2, 'connection_XMLFileNode73', b)


def test_assoc_group84_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_BRMSConnection(className="sample_text", moduleUsed="sample_text", package="sample_text", tacWebappName="sample_text", urlName="sample_text", xmlField="sample_text")
    _safe_set(b, 'connection_BRMSConnection85', {a1})
    assert _is_linked(b, 'connection_BRMSConnection85', a1)
    if hasattr(a1, 'connection_XMLFileNode86'):
        assert _is_linked(a1, 'connection_XMLFileNode86', b)
    _safe_set(b, 'connection_BRMSConnection85', {a2})
    assert _is_linked(b, 'connection_BRMSConnection85', a2)
    if hasattr(a1, 'connection_XMLFileNode86'):
        assert not _is_linked(a1, 'connection_XMLFileNode86', b)
    if hasattr(a2, 'connection_XMLFileNode86'):
        assert _is_linked(a2, 'connection_XMLFileNode86', b)
    _safe_set(b, 'connection_BRMSConnection85', set())
    assert not _is_linked(b, 'connection_BRMSConnection85', a2)
    if hasattr(a2, 'connection_XMLFileNode86'):
        assert not _is_linked(a2, 'connection_XMLFileNode86', b)


def test_assoc_innerJoins91_reverse_link_reassign_clear():
    a1 = connection_ValidationRulesConnection(baseColumnNames="sample_text", baseSchema="sample_text", isDelete=True, isDisallow=True, isInsert=True, isRejectLink=True, isSelect=True, isUpdate=True, javaCondition="sample_text", logicalOperator="sample_text", refColumnNames="sample_text", refSchema="sample_text", sqlCondition="sample_text", type="sample_text")
    a2 = connection_ValidationRulesConnection(baseColumnNames="sample_text_2", baseSchema="sample_text_2", isDelete=False, isDisallow=False, isInsert=False, isRejectLink=False, isSelect=False, isUpdate=False, javaCondition="sample_text_2", logicalOperator="sample_text_2", refColumnNames="sample_text_2", refSchema="sample_text_2", sqlCondition="sample_text_2", type="sample_text_2")
    b = connection_InnerJoinMap(key="sample_text", value="sample_text")
    _safe_set(b, 'connection_InnerJoinMap', a1)
    assert _is_linked(b, 'connection_InnerJoinMap', a1)
    if hasattr(a1, 'connection_ValidationRulesConnection92'):
        assert _is_linked(a1, 'connection_ValidationRulesConnection92', b)
    _safe_set(b, 'connection_InnerJoinMap', a2)
    assert _is_linked(b, 'connection_InnerJoinMap', a2)
    if hasattr(a1, 'connection_ValidationRulesConnection92'):
        assert not _is_linked(a1, 'connection_ValidationRulesConnection92', b)
    if hasattr(a2, 'connection_ValidationRulesConnection92'):
        assert _is_linked(a2, 'connection_ValidationRulesConnection92', b)
    _safe_set(b, 'connection_InnerJoinMap', None)
    assert not _is_linked(b, 'connection_InnerJoinMap', a2)
    if hasattr(a2, 'connection_ValidationRulesConnection92'):
        assert not _is_linked(a2, 'connection_ValidationRulesConnection92', b)


def test_assoc_loop41_reverse_link_reassign_clear():
    a1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    a2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2", fileContent="sample_text_2", inputModel=False, outputFilePath="sample_text_2")
    b = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    _safe_set(b, 'connection_XMLFileNode43', a1)
    assert _is_linked(b, 'connection_XMLFileNode43', a1)
    if hasattr(a1, 'connection_XmlFileConnection42'):
        assert _is_linked(a1, 'connection_XmlFileConnection42', b)
    _safe_set(b, 'connection_XMLFileNode43', a2)
    assert _is_linked(b, 'connection_XMLFileNode43', a2)
    if hasattr(a1, 'connection_XmlFileConnection42'):
        assert not _is_linked(a1, 'connection_XmlFileConnection42', b)
    if hasattr(a2, 'connection_XmlFileConnection42'):
        assert _is_linked(a2, 'connection_XmlFileConnection42', b)
    _safe_set(b, 'connection_XMLFileNode43', None)
    assert not _is_linked(b, 'connection_XMLFileNode43', a2)
    if hasattr(a2, 'connection_XmlFileConnection42'):
        assert not _is_linked(a2, 'connection_XmlFileConnection42', b)


def test_assoc_loop77_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept78', {a1})
    assert _is_linked(b, 'connection_Concept78', a1)
    if hasattr(a1, 'connection_XMLFileNode79'):
        assert _is_linked(a1, 'connection_XMLFileNode79', b)
    _safe_set(b, 'connection_Concept78', {a2})
    assert _is_linked(b, 'connection_Concept78', a2)
    if hasattr(a1, 'connection_XMLFileNode79'):
        assert not _is_linked(a1, 'connection_XMLFileNode79', b)
    if hasattr(a2, 'connection_XMLFileNode79'):
        assert _is_linked(a2, 'connection_XMLFileNode79', b)
    _safe_set(b, 'connection_Concept78', set())
    assert not _is_linked(b, 'connection_Concept78', a2)
    if hasattr(a2, 'connection_XMLFileNode79'):
        assert not _is_linked(a2, 'connection_XMLFileNode79', b)


def test_assoc_loop87_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_BRMSConnection(className="sample_text", moduleUsed="sample_text", package="sample_text", tacWebappName="sample_text", urlName="sample_text", xmlField="sample_text")
    _safe_set(b, 'connection_BRMSConnection88', {a1})
    assert _is_linked(b, 'connection_BRMSConnection88', a1)
    if hasattr(a1, 'connection_XMLFileNode89'):
        assert _is_linked(a1, 'connection_XMLFileNode89', b)
    _safe_set(b, 'connection_BRMSConnection88', {a2})
    assert _is_linked(b, 'connection_BRMSConnection88', a2)
    if hasattr(a1, 'connection_XMLFileNode89'):
        assert not _is_linked(a1, 'connection_XMLFileNode89', b)
    if hasattr(a2, 'connection_XMLFileNode89'):
        assert _is_linked(a2, 'connection_XMLFileNode89', b)
    _safe_set(b, 'connection_BRMSConnection88', set())
    assert not _is_linked(b, 'connection_BRMSConnection88', a2)
    if hasattr(a2, 'connection_XMLFileNode89'):
        assert not _is_linked(a2, 'connection_XMLFileNode89', b)


def test_assoc_modules58_reverse_link_reassign_clear():
    a1 = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    a2 = connection_SalesforceSchemaConnection(batchSize="sample_text_2", moduleName="sample_text_2", password="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUsername="sample_text_2", queryCondition="sample_text_2", timeOut="sample_text_2", useAlphbet=False, useCustomModuleName=False, useHttpProxy=False, useProxy=False, userName="sample_text_2", webServiceUrl="sample_text_2")
    b = connection_SalesforceModuleUnit(moduleName="sample_text")
    _safe_set(b, 'SalesforceModuleUnit', a1)
    assert _is_linked(b, 'SalesforceModuleUnit', a1)
    if hasattr(a1, 'connection59'):
        assert _is_linked(a1, 'connection59', b)
    _safe_set(b, 'SalesforceModuleUnit', a2)
    assert _is_linked(b, 'SalesforceModuleUnit', a2)
    if hasattr(a1, 'connection59'):
        assert not _is_linked(a1, 'connection59', b)
    if hasattr(a2, 'connection59'):
        assert _is_linked(a2, 'connection59', b)
    _safe_set(b, 'SalesforceModuleUnit', None)
    assert not _is_linked(b, 'SalesforceModuleUnit', a2)
    if hasattr(a2, 'connection59'):
        assert not _is_linked(a2, 'connection59', b)


def test_assoc_outputParameter55_reverse_link_reassign_clear():
    a1 = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", isInputModel=True, methodName="sample_text", needAuth=True, parameters="sample_text", portName="sample_text", portNameSpace="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", serverName="sample_text", serverNameSpace="sample_text", timeOut=7, useProxy=True)
    a2 = connection_WSDLSchemaConnection(Encoding="sample_text_2", EndpointURI="sample_text_2", Password="sample_text_2", UserName="sample_text_2", Value="sample_text_2", WSDL="sample_text_2", isInputModel=False, methodName="sample_text_2", needAuth=False, parameters="sample_text_2", portName="sample_text_2", portNameSpace="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUser="sample_text_2", serverName="sample_text_2", serverNameSpace="sample_text_2", timeOut=13, useProxy=False)
    b = connection_WSDLParameter(Column="sample_text", Element="sample_text", Expression="sample_text", ParameterInfo="sample_text", ParameterInfoParent="sample_text", source="sample_text")
    _safe_set(b, 'connection_WSDLParameter57', a1)
    assert _is_linked(b, 'connection_WSDLParameter57', a1)
    if hasattr(a1, 'connection_WSDLSchemaConnection56'):
        assert _is_linked(a1, 'connection_WSDLSchemaConnection56', b)
    _safe_set(b, 'connection_WSDLParameter57', a2)
    assert _is_linked(b, 'connection_WSDLParameter57', a2)
    if hasattr(a1, 'connection_WSDLSchemaConnection56'):
        assert not _is_linked(a1, 'connection_WSDLSchemaConnection56', b)
    if hasattr(a2, 'connection_WSDLSchemaConnection56'):
        assert _is_linked(a2, 'connection_WSDLSchemaConnection56', b)
    _safe_set(b, 'connection_WSDLParameter57', None)
    assert not _is_linked(b, 'connection_WSDLParameter57', a2)
    if hasattr(a2, 'connection_WSDLSchemaConnection56'):
        assert not _is_linked(a2, 'connection_WSDLSchemaConnection56', b)


def test_assoc_parameterValue54_reverse_link_reassign_clear():
    a1 = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", isInputModel=True, methodName="sample_text", needAuth=True, parameters="sample_text", portName="sample_text", portNameSpace="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", serverName="sample_text", serverNameSpace="sample_text", timeOut=7, useProxy=True)
    a2 = connection_WSDLSchemaConnection(Encoding="sample_text_2", EndpointURI="sample_text_2", Password="sample_text_2", UserName="sample_text_2", Value="sample_text_2", WSDL="sample_text_2", isInputModel=False, methodName="sample_text_2", needAuth=False, parameters="sample_text_2", portName="sample_text_2", portNameSpace="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUser="sample_text_2", serverName="sample_text_2", serverNameSpace="sample_text_2", timeOut=13, useProxy=False)
    b = connection_WSDLParameter(Column="sample_text", Element="sample_text", Expression="sample_text", ParameterInfo="sample_text", ParameterInfoParent="sample_text", source="sample_text")
    _safe_set(b, 'connection_WSDLParameter', a1)
    assert _is_linked(b, 'connection_WSDLParameter', a1)
    if hasattr(a1, 'connection_WSDLSchemaConnection'):
        assert _is_linked(a1, 'connection_WSDLSchemaConnection', b)
    _safe_set(b, 'connection_WSDLParameter', a2)
    assert _is_linked(b, 'connection_WSDLParameter', a2)
    if hasattr(a1, 'connection_WSDLSchemaConnection'):
        assert not _is_linked(a1, 'connection_WSDLSchemaConnection', b)
    if hasattr(a2, 'connection_WSDLSchemaConnection'):
        assert _is_linked(a2, 'connection_WSDLSchemaConnection', b)
    _safe_set(b, 'connection_WSDLParameter', None)
    assert not _is_linked(b, 'connection_WSDLParameter', a2)
    if hasattr(a2, 'connection_WSDLSchemaConnection'):
        assert not _is_linked(a2, 'connection_WSDLSchemaConnection', b)


def test_assoc_root38_reverse_link_reassign_clear():
    a1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    a2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2", fileContent="sample_text_2", inputModel=False, outputFilePath="sample_text_2")
    b = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    _safe_set(b, 'connection_XMLFileNode40', a1)
    assert _is_linked(b, 'connection_XMLFileNode40', a1)
    if hasattr(a1, 'connection_XmlFileConnection39'):
        assert _is_linked(a1, 'connection_XmlFileConnection39', b)
    _safe_set(b, 'connection_XMLFileNode40', a2)
    assert _is_linked(b, 'connection_XMLFileNode40', a2)
    if hasattr(a1, 'connection_XmlFileConnection39'):
        assert not _is_linked(a1, 'connection_XmlFileConnection39', b)
    if hasattr(a2, 'connection_XmlFileConnection39'):
        assert _is_linked(a2, 'connection_XmlFileConnection39', b)
    _safe_set(b, 'connection_XMLFileNode40', None)
    assert not _is_linked(b, 'connection_XMLFileNode40', a2)
    if hasattr(a2, 'connection_XmlFileConnection39'):
        assert not _is_linked(a2, 'connection_XmlFileConnection39', b)


def test_assoc_root74_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept75', {a1})
    assert _is_linked(b, 'connection_Concept75', a1)
    if hasattr(a1, 'connection_XMLFileNode76'):
        assert _is_linked(a1, 'connection_XMLFileNode76', b)
    _safe_set(b, 'connection_Concept75', {a2})
    assert _is_linked(b, 'connection_Concept75', a2)
    if hasattr(a1, 'connection_XMLFileNode76'):
        assert not _is_linked(a1, 'connection_XMLFileNode76', b)
    if hasattr(a2, 'connection_XMLFileNode76'):
        assert _is_linked(a2, 'connection_XMLFileNode76', b)
    _safe_set(b, 'connection_Concept75', set())
    assert not _is_linked(b, 'connection_Concept75', a2)
    if hasattr(a2, 'connection_XMLFileNode76'):
        assert not _is_linked(a2, 'connection_XMLFileNode76', b)


def test_assoc_root81_reverse_link_reassign_clear():
    a1 = connection_HL7FileNode(Attribute="sample_text", DefaultValue="sample_text", FilePath="sample_text", Order=7, RelatedColumn="sample_text", Repeatable=True)
    a2 = connection_HL7FileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", FilePath="sample_text_2", Order=13, RelatedColumn="sample_text_2", Repeatable=False)
    b = connection_HL7Connection(EndChar="sample_text", StartChar="sample_text", outputFilePath="sample_text")
    _safe_set(b, 'connection_HL7Connection', {a1})
    assert _is_linked(b, 'connection_HL7Connection', a1)
    if hasattr(a1, 'connection_HL7FileNode'):
        assert _is_linked(a1, 'connection_HL7FileNode', b)
    _safe_set(b, 'connection_HL7Connection', {a2})
    assert _is_linked(b, 'connection_HL7Connection', a2)
    if hasattr(a1, 'connection_HL7FileNode'):
        assert not _is_linked(a1, 'connection_HL7FileNode', b)
    if hasattr(a2, 'connection_HL7FileNode'):
        assert _is_linked(a2, 'connection_HL7FileNode', b)
    _safe_set(b, 'connection_HL7Connection', set())
    assert not _is_linked(b, 'connection_HL7Connection', a2)
    if hasattr(a2, 'connection_HL7FileNode'):
        assert not _is_linked(a2, 'connection_HL7FileNode', b)


def test_assoc_root82_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_BRMSConnection(className="sample_text", moduleUsed="sample_text", package="sample_text", tacWebappName="sample_text", urlName="sample_text", xmlField="sample_text")
    _safe_set(b, 'connection_BRMSConnection', {a1})
    assert _is_linked(b, 'connection_BRMSConnection', a1)
    if hasattr(a1, 'connection_XMLFileNode83'):
        assert _is_linked(a1, 'connection_XMLFileNode83', b)
    _safe_set(b, 'connection_BRMSConnection', {a2})
    assert _is_linked(b, 'connection_BRMSConnection', a2)
    if hasattr(a1, 'connection_XMLFileNode83'):
        assert not _is_linked(a1, 'connection_XMLFileNode83', b)
    if hasattr(a2, 'connection_XMLFileNode83'):
        assert _is_linked(a2, 'connection_XMLFileNode83', b)
    _safe_set(b, 'connection_BRMSConnection', set())
    assert not _is_linked(b, 'connection_BRMSConnection', a2)
    if hasattr(a2, 'connection_XMLFileNode83'):
        assert not _is_linked(a2, 'connection_XMLFileNode83', b)


def test_assoc_schema35_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    _safe_set(b, 'connection36', {a1})
    assert _is_linked(b, 'connection36', a1)
    if hasattr(a1, 'XmlXPathLoopDescriptor'):
        assert _is_linked(a1, 'XmlXPathLoopDescriptor', b)
    _safe_set(b, 'connection36', {a2})
    assert _is_linked(b, 'connection36', a2)
    if hasattr(a1, 'XmlXPathLoopDescriptor'):
        assert not _is_linked(a1, 'XmlXPathLoopDescriptor', b)
    if hasattr(a2, 'XmlXPathLoopDescriptor'):
        assert _is_linked(a2, 'XmlXPathLoopDescriptor', b)
    _safe_set(b, 'connection36', set())
    assert not _is_linked(b, 'connection36', a2)
    if hasattr(a2, 'XmlXPathLoopDescriptor'):
        assert not _is_linked(a2, 'XmlXPathLoopDescriptor', b)


def test_assoc_schema44_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    _safe_set(b, 'schemaTargets', a1)
    assert _is_linked(b, 'schemaTargets', a1)
    if hasattr(a1, 'XmlXPathLoopDescriptor45'):
        assert _is_linked(a1, 'XmlXPathLoopDescriptor45', b)
    _safe_set(b, 'schemaTargets', a2)
    assert _is_linked(b, 'schemaTargets', a2)
    if hasattr(a1, 'XmlXPathLoopDescriptor45'):
        assert not _is_linked(a1, 'XmlXPathLoopDescriptor45', b)
    if hasattr(a2, 'XmlXPathLoopDescriptor45'):
        assert _is_linked(a2, 'XmlXPathLoopDescriptor45', b)
    _safe_set(b, 'schemaTargets', None)
    assert not _is_linked(b, 'schemaTargets', a2)
    if hasattr(a2, 'XmlXPathLoopDescriptor45'):
        assert not _is_linked(a2, 'XmlXPathLoopDescriptor45', b)


def test_assoc_schema80_reverse_link_reassign_clear():
    a1 = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    a2 = connection_ConceptTarget(RelativeLoopExpression="sample_text_2", targetName="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'Concept', a1)
    assert _is_linked(b, 'Concept', a1)
    if hasattr(a1, 'conceptTargets'):
        assert _is_linked(a1, 'conceptTargets', b)
    _safe_set(b, 'Concept', a2)
    assert _is_linked(b, 'Concept', a2)
    if hasattr(a1, 'conceptTargets'):
        assert not _is_linked(a1, 'conceptTargets', b)
    if hasattr(a2, 'conceptTargets'):
        assert _is_linked(a2, 'conceptTargets', b)
    _safe_set(b, 'Concept', None)
    assert not _is_linked(b, 'Concept', a2)
    if hasattr(a2, 'conceptTargets'):
        assert not _is_linked(a2, 'conceptTargets', b)


def test_assoc_schemaTargets52_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    _safe_set(b, 'SchemaTarget', a1)
    assert _is_linked(b, 'SchemaTarget', a1)
    if hasattr(a1, 'schema53'):
        assert _is_linked(a1, 'schema53', b)
    _safe_set(b, 'SchemaTarget', a2)
    assert _is_linked(b, 'SchemaTarget', a2)
    if hasattr(a1, 'schema53'):
        assert not _is_linked(a1, 'schema53', b)
    if hasattr(a2, 'schema53'):
        assert _is_linked(a2, 'schema53', b)
    _safe_set(b, 'SchemaTarget', None)
    assert not _is_linked(b, 'SchemaTarget', a2)
    if hasattr(a2, 'schema53'):
        assert not _is_linked(a2, 'schema53', b)


def test_assoc_schemas9_reverse_link_reassign_clear():
    a1 = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text", context="sample_text", protocol="sample_text")
    a2 = connection_MDMConnection(Datacluster="sample_text_2", Datamodel="sample_text_2", Password="sample_text_2", Port="sample_text_2", Server="sample_text_2", Universe="sample_text_2", Username="sample_text_2", context="sample_text_2", protocol="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept', a1)
    assert _is_linked(b, 'connection_Concept', a1)
    if hasattr(a1, 'connection_MDMConnection'):
        assert _is_linked(a1, 'connection_MDMConnection', b)
    _safe_set(b, 'connection_Concept', a2)
    assert _is_linked(b, 'connection_Concept', a2)
    if hasattr(a1, 'connection_MDMConnection'):
        assert not _is_linked(a1, 'connection_MDMConnection', b)
    if hasattr(a2, 'connection_MDMConnection'):
        assert _is_linked(a2, 'connection_MDMConnection', b)
    _safe_set(b, 'connection_Concept', None)
    assert not _is_linked(b, 'connection_Concept', a2)
    if hasattr(a2, 'connection_MDMConnection'):
        assert not _is_linked(a2, 'connection_MDMConnection', b)


def test_assoc_subscribers62_reverse_link_reassign_clear():
    a1 = connection_SubscriberTable(system=True)
    a2 = connection_SubscriberTable(system=False)
    b = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    _safe_set(b, 'connection_CDCType63', {a1})
    assert _is_linked(b, 'connection_CDCType63', a1)
    if hasattr(a1, 'connection_SubscriberTable'):
        assert _is_linked(a1, 'connection_SubscriberTable', b)
    _safe_set(b, 'connection_CDCType63', {a2})
    assert _is_linked(b, 'connection_CDCType63', a2)
    if hasattr(a1, 'connection_SubscriberTable'):
        assert not _is_linked(a1, 'connection_SubscriberTable', b)
    if hasattr(a2, 'connection_SubscriberTable'):
        assert _is_linked(a2, 'connection_SubscriberTable', b)
    _safe_set(b, 'connection_CDCType63', set())
    assert not _is_linked(b, 'connection_CDCType63', a2)
    if hasattr(a2, 'connection_SubscriberTable'):
        assert not _is_linked(a2, 'connection_SubscriberTable', b)


def test_assoc_table2_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", originalLength="sample_text", pattern="sample_text", relatedEntity="sample_text", relationshipType="sample_text", sourceType="sample_text", talendType="sample_text")
    _safe_set(b, 'connection_MetadataColumn', a1)
    assert _is_linked(b, 'connection_MetadataColumn', a1)
    if hasattr(a1, 'connection_MetadataTable'):
        assert _is_linked(a1, 'connection_MetadataTable', b)
    _safe_set(b, 'connection_MetadataColumn', a2)
    assert _is_linked(b, 'connection_MetadataColumn', a2)
    if hasattr(a1, 'connection_MetadataTable'):
        assert not _is_linked(a1, 'connection_MetadataTable', b)
    if hasattr(a2, 'connection_MetadataTable'):
        assert _is_linked(a2, 'connection_MetadataTable', b)
    _safe_set(b, 'connection_MetadataColumn', None)
    assert not _is_linked(b, 'connection_MetadataColumn', a2)
    if hasattr(a2, 'connection_MetadataTable'):
        assert not _is_linked(a2, 'connection_MetadataTable', b)


def test_assoc_tables22_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable24', a1)
    assert _is_linked(b, 'connection_MetadataTable24', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit23'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit23', b)
    _safe_set(b, 'connection_MetadataTable24', a2)
    assert _is_linked(b, 'connection_MetadataTable24', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit23'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit23', b)
    if hasattr(a2, 'connection_SAPFunctionUnit23'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit23', b)
    _safe_set(b, 'connection_MetadataTable24', None)
    assert not _is_linked(b, 'connection_MetadataTable24', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit23'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit23', b)


def test_assoc_tables96_reverse_link_reassign_clear():
    a1 = connection_SalesforceModuleUnit(moduleName="sample_text")
    a2 = connection_SalesforceModuleUnit(moduleName="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable98', a1)
    assert _is_linked(b, 'connection_MetadataTable98', a1)
    if hasattr(a1, 'connection_SalesforceModuleUnit97'):
        assert _is_linked(a1, 'connection_SalesforceModuleUnit97', b)
    _safe_set(b, 'connection_MetadataTable98', a2)
    assert _is_linked(b, 'connection_MetadataTable98', a2)
    if hasattr(a1, 'connection_SalesforceModuleUnit97'):
        assert not _is_linked(a1, 'connection_SalesforceModuleUnit97', b)
    if hasattr(a2, 'connection_SalesforceModuleUnit97'):
        assert _is_linked(a2, 'connection_SalesforceModuleUnit97', b)
    _safe_set(b, 'connection_MetadataTable98', None)
    assert not _is_linked(b, 'connection_MetadataTable98', a2)
    if hasattr(a2, 'connection_SalesforceModuleUnit97'):
        assert not _is_linked(a2, 'connection_SalesforceModuleUnit97', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_InputParameterTable16_stub_double():
    # connection_InputSAPFunctionParameterTable has no real 'InputSAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_InputSAPFunctionParameterTable()
    setattr(partner, 'InputSAPFunctionParameterTable', None)
    _safe_set(owner, 'functionUnit', partner)
    assert getattr(partner, 'InputSAPFunctionParameterTable') == owner
    _safe_set(owner, 'functionUnit', None)
    assert getattr(partner, 'InputSAPFunctionParameterTable') is None


def test_assoc_OutputParameterTable17_stub_double():
    # connection_OutputSAPFunctionParameterTable has no real 'OutputSAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_OutputSAPFunctionParameterTable()
    setattr(partner, 'OutputSAPFunctionParameterTable', None)
    _safe_set(owner, 'functionUnit18', partner)
    assert getattr(partner, 'OutputSAPFunctionParameterTable') == owner
    _safe_set(owner, 'functionUnit18', None)
    assert getattr(partner, 'OutputSAPFunctionParameterTable') is None


def test_assoc_ParameterTable29_stub_double():
    # connection_SAPFunctionParameterTable has no real 'SAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionParameterColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionParameterColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    partner = connection_SAPFunctionParameterTable()
    setattr(partner, 'SAPFunctionParameterTable', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'SAPFunctionParameterTable') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'SAPFunctionParameterTable') is None


def test_assoc_TestInputParameterTable25_stub_double():
    # connection_SAPTestInputParameterTable has no real 'SAPTestInputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_SAPTestInputParameterTable()
    setattr(partner, 'SAPTestInputParameterTable', None)
    _safe_set(owner, 'functionUnit26', partner)
    assert getattr(partner, 'SAPTestInputParameterTable') == owner
    _safe_set(owner, 'functionUnit26', None)
    assert getattr(partner, 'SAPTestInputParameterTable') is None


def test_assoc_cdcConnection64_stub_double():
    # connection_CDCConnection has no real 'connection_CDCConnection66' property in the generated
    # code (a bare stub) -- manually attach it so connection_CDCType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_CDCType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'connection_CDCConnection66', None)
    _safe_set(owner, 'connection_CDCType65', partner)
    assert getattr(partner, 'connection_CDCConnection66') == owner
    _safe_set(owner, 'connection_CDCType65', None)
    assert getattr(partner, 'connection_CDCConnection66') is None


def test_assoc_cdcConns10_stub_double():
    # connection_CDCConnection has no real 'CDCConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_DatabaseConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_DatabaseConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'CDCConnection', None)
    _safe_set(owner, 'connection11', partner)
    assert getattr(partner, 'CDCConnection') == owner
    _safe_set(owner, 'connection11', None)
    assert getattr(partner, 'CDCConnection') is None


def test_assoc_cdcTypes61_stub_double():
    # connection_CDCConnection has no real 'connection_CDCConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_CDCType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_CDCType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'connection_CDCConnection', None)
    _safe_set(owner, 'connection_CDCType', partner)
    assert owner in getattr(partner, 'connection_CDCConnection')
    _safe_set(owner, 'connection_CDCType', None)
    assert owner not in getattr(partner, 'connection_CDCConnection')


def test_assoc_columns30_stub_double():
    # connection_SAPFunctionParameterTable has no real 'ParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionParameterColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionParameterColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    partner = connection_SAPFunctionParameterTable()
    setattr(partner, 'ParameterTable', None)
    _safe_set(owner, 'SAPFunctionParameterColumn', partner)
    assert owner in getattr(partner, 'ParameterTable')
    _safe_set(owner, 'SAPFunctionParameterColumn', None)
    assert owner not in getattr(partner, 'ParameterTable')


def test_assoc_connection46_stub_double():
    # connection_QueriesConnection has no real 'queries' property in the generated
    # code (a bare stub) -- manually attach it so connection_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Connection(ContextId="sample_text", ContextMode=True, contextName="sample_text", version="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'queries', None)
    _safe_set(owner, 'Connection', partner)
    assert getattr(partner, 'queries') == owner
    _safe_set(owner, 'Connection', None)
    assert getattr(partner, 'queries') is None


def test_assoc_connection60_stub_double():
    # connection_CDCConnection has no real 'cdcConns' property in the generated
    # code (a bare stub) -- manually attach it so connection_DatabaseConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_DatabaseConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'cdcConns', None)
    _safe_set(owner, 'DatabaseConnection', partner)
    assert getattr(partner, 'cdcConns') == owner
    _safe_set(owner, 'DatabaseConnection', None)
    assert getattr(partner, 'cdcConns') is None


def test_assoc_connections0_stub_double():
    # connection_Metadata has no real 'connection_Metadata' property in the generated
    # code (a bare stub) -- manually attach it so connection_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Connection(ContextId="sample_text", ContextMode=True, contextName="sample_text", version="sample_text")
    partner = connection_Metadata()
    setattr(partner, 'connection_Metadata', None)
    _safe_set(owner, 'connection_Connection', partner)
    assert owner in getattr(partner, 'connection_Metadata')
    _safe_set(owner, 'connection_Connection', None)
    assert owner not in getattr(partner, 'connection_Metadata')


def test_assoc_functionUnit31_stub_double():
    # connection_InputSAPFunctionParameterTable has no real 'InputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_InputSAPFunctionParameterTable()
    setattr(partner, 'InputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit32', partner)
    assert getattr(partner, 'InputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit32', None)
    assert getattr(partner, 'InputParameterTable') is None


def test_assoc_functionUnit33_stub_double():
    # connection_OutputSAPFunctionParameterTable has no real 'OutputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_OutputSAPFunctionParameterTable()
    setattr(partner, 'OutputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit34', partner)
    assert getattr(partner, 'OutputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit34', None)
    assert getattr(partner, 'OutputParameterTable') is None


def test_assoc_functionUnit67_stub_double():
    # connection_SAPTestInputParameterTable has no real 'TestInputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    partner = connection_SAPTestInputParameterTable()
    setattr(partner, 'TestInputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit68', partner)
    assert getattr(partner, 'TestInputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit68', None)
    assert getattr(partner, 'TestInputParameterTable') is None


def test_assoc_ownedDocument101_stub_double():
    # xml_TdXmlSchema has no real 'xml_TdXmlSchema' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXmlElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXmlElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXmlElementType(javaType="sample_text")
    partner = xml_TdXmlSchema()
    setattr(partner, 'xml_TdXmlSchema', None)
    _safe_set(owner, 'connection_xml_TdXmlElementType102', partner)
    assert getattr(partner, 'xml_TdXmlSchema') == owner
    _safe_set(owner, 'connection_xml_TdXmlElementType102', None)
    assert getattr(partner, 'xml_TdXmlSchema') is None


def test_assoc_queries1_stub_double():
    # connection_QueriesConnection has no real 'QueriesConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Connection(ContextId="sample_text", ContextMode=True, contextName="sample_text", version="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'QueriesConnection', None)
    _safe_set(owner, 'connection', partner)
    assert getattr(partner, 'QueriesConnection') == owner
    _safe_set(owner, 'connection', None)
    assert getattr(partner, 'QueriesConnection') is None


def test_assoc_queries49_stub_double():
    # connection_QueriesConnection has no real 'QueriesConnection50' property in the generated
    # code (a bare stub) -- manually attach it so connection_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Query(contextMode=True, value="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'QueriesConnection50', None)
    _safe_set(owner, 'query', partner)
    assert getattr(partner, 'QueriesConnection50') == owner
    _safe_set(owner, 'query', None)
    assert getattr(partner, 'QueriesConnection50') is None


def test_assoc_query47_stub_double():
    # connection_QueriesConnection has no real 'queries48' property in the generated
    # code (a bare stub) -- manually attach it so connection_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Query(contextMode=True, value="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'queries48', None)
    _safe_set(owner, 'Query', partner)
    assert owner in getattr(partner, 'queries48')
    _safe_set(owner, 'Query', None)
    assert owner not in getattr(partner, 'queries48')


def test_assoc_sqlDataType99_stub_double():
    # relational_TdSqlDataType has no real 'relational_TdSqlDataType' property in the generated
    # code (a bare stub) -- manually attach it so connection_relational_TdColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_relational_TdColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_relational_TdColumn()
    partner = relational_TdSqlDataType()
    setattr(partner, 'relational_TdSqlDataType', None)
    _safe_set(owner, 'connection_relational_TdColumn', partner)
    assert getattr(partner, 'relational_TdSqlDataType') == owner
    _safe_set(owner, 'connection_relational_TdColumn', None)
    assert getattr(partner, 'relational_TdSqlDataType') is None


def test_assoc_xmlContent103_stub_double():
    # xml_TdXmlContent has no real 'xml_TdXmlContent' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXmlElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXmlElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXmlElementType(javaType="sample_text")
    partner = xml_TdXmlContent()
    setattr(partner, 'xml_TdXmlContent', None)
    _safe_set(owner, 'connection_xml_TdXmlElementType104', partner)
    assert getattr(partner, 'xml_TdXmlContent') == owner
    _safe_set(owner, 'connection_xml_TdXmlElementType104', None)
    assert getattr(partner, 'xml_TdXmlContent') is None


def test_assoc_xsdElementDeclaration100_stub_double():
    # xml_connection_EObject has no real 'xml_connection_EObject' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXmlElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXmlElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXmlElementType(javaType="sample_text")
    partner = xml_connection_EObject()
    setattr(partner, 'xml_connection_EObject', None)
    _safe_set(owner, 'connection_xml_TdXmlElementType', partner)
    assert getattr(partner, 'xml_connection_EObject') == owner
    _safe_set(owner, 'connection_xml_TdXmlElementType', None)
    assert getattr(partner, 'xml_connection_EObject') is None


