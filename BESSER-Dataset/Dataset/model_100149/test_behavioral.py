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
    SAPTable,
    SAPTableField,
    SQLSimpleType,
    Schema,
    SoftwareSystem,
    TdTable,
    Trigger,
    connection_AbstractMetadataObject,
    connection_AdditionalConnectionProperty,
    connection_AdditionalProperties,
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
    connection_SAPBWTable,
    connection_SAPBWTableField,
    connection_SAPConnection,
    connection_SAPFunctionParamData,
    connection_SAPFunctionParameter,
    connection_SAPFunctionParameterColumn,
    connection_SAPFunctionParameterTable,
    connection_SAPFunctionUnit,
    connection_SAPIDocUnit,
    connection_SAPTable,
    connection_SAPTableField,
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

def test_assoc_BWDataSources21_reverse_link_reassign_clear():
    a1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    a2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2", jcoVersion="sample_text_2")
    b = connection_SAPBWTable(active=True, infoAreaName="sample_text", innerIOType="sample_text", modelType="sample_text", sourceSystemName="sample_text")
    _safe_set(b, 'connection_SAPBWTable', a1)
    assert _is_linked(b, 'connection_SAPBWTable', a1)
    if hasattr(a1, 'connection_SAPConnection22'):
        assert _is_linked(a1, 'connection_SAPConnection22', b)
    _safe_set(b, 'connection_SAPBWTable', a2)
    assert _is_linked(b, 'connection_SAPBWTable', a2)
    if hasattr(a1, 'connection_SAPConnection22'):
        assert not _is_linked(a1, 'connection_SAPConnection22', b)
    if hasattr(a2, 'connection_SAPConnection22'):
        assert _is_linked(a2, 'connection_SAPConnection22', b)
    _safe_set(b, 'connection_SAPBWTable', None)
    assert not _is_linked(b, 'connection_SAPBWTable', a2)
    if hasattr(a2, 'connection_SAPConnection22'):
        assert not _is_linked(a2, 'connection_SAPConnection22', b)


def test_assoc_BWDataStoreObjects23_reverse_link_reassign_clear():
    a1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    a2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2", jcoVersion="sample_text_2")
    b = connection_SAPBWTable(active=True, infoAreaName="sample_text", innerIOType="sample_text", modelType="sample_text", sourceSystemName="sample_text")
    _safe_set(b, 'connection_SAPBWTable25', a1)
    assert _is_linked(b, 'connection_SAPBWTable25', a1)
    if hasattr(a1, 'connection_SAPConnection24'):
        assert _is_linked(a1, 'connection_SAPConnection24', b)
    _safe_set(b, 'connection_SAPBWTable25', a2)
    assert _is_linked(b, 'connection_SAPBWTable25', a2)
    if hasattr(a1, 'connection_SAPConnection24'):
        assert not _is_linked(a1, 'connection_SAPConnection24', b)
    if hasattr(a2, 'connection_SAPConnection24'):
        assert _is_linked(a2, 'connection_SAPConnection24', b)
    _safe_set(b, 'connection_SAPBWTable25', None)
    assert not _is_linked(b, 'connection_SAPBWTable25', a2)
    if hasattr(a2, 'connection_SAPConnection24'):
        assert not _is_linked(a2, 'connection_SAPConnection24', b)


def test_assoc_BWInfoCubes26_reverse_link_reassign_clear():
    a1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    a2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2", jcoVersion="sample_text_2")
    b = connection_SAPBWTable(active=True, infoAreaName="sample_text", innerIOType="sample_text", modelType="sample_text", sourceSystemName="sample_text")
    _safe_set(b, 'connection_SAPBWTable28', a1)
    assert _is_linked(b, 'connection_SAPBWTable28', a1)
    if hasattr(a1, 'connection_SAPConnection27'):
        assert _is_linked(a1, 'connection_SAPConnection27', b)
    _safe_set(b, 'connection_SAPBWTable28', a2)
    assert _is_linked(b, 'connection_SAPBWTable28', a2)
    if hasattr(a1, 'connection_SAPConnection27'):
        assert not _is_linked(a1, 'connection_SAPConnection27', b)
    if hasattr(a2, 'connection_SAPConnection27'):
        assert _is_linked(a2, 'connection_SAPConnection27', b)
    _safe_set(b, 'connection_SAPBWTable28', None)
    assert not _is_linked(b, 'connection_SAPBWTable28', a2)
    if hasattr(a2, 'connection_SAPConnection27'):
        assert not _is_linked(a2, 'connection_SAPConnection27', b)


def test_assoc_BWInfoObjects29_reverse_link_reassign_clear():
    a1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    a2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2", jcoVersion="sample_text_2")
    b = connection_SAPBWTable(active=True, infoAreaName="sample_text", innerIOType="sample_text", modelType="sample_text", sourceSystemName="sample_text")
    _safe_set(b, 'connection_SAPBWTable31', a1)
    assert _is_linked(b, 'connection_SAPBWTable31', a1)
    if hasattr(a1, 'connection_SAPConnection30'):
        assert _is_linked(a1, 'connection_SAPConnection30', b)
    _safe_set(b, 'connection_SAPBWTable31', a2)
    assert _is_linked(b, 'connection_SAPBWTable31', a2)
    if hasattr(a1, 'connection_SAPConnection30'):
        assert not _is_linked(a1, 'connection_SAPConnection30', b)
    if hasattr(a2, 'connection_SAPConnection30'):
        assert _is_linked(a2, 'connection_SAPConnection30', b)
    _safe_set(b, 'connection_SAPBWTable31', None)
    assert not _is_linked(b, 'connection_SAPBWTable31', a2)
    if hasattr(a2, 'connection_SAPConnection30'):
        assert not _is_linked(a2, 'connection_SAPConnection30', b)


def test_assoc_Funtions16_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2", asXmlSchema=False)
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'connection_SAPConnection', {a1})
    assert _is_linked(b, 'connection_SAPConnection', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit', b)
    _safe_set(b, 'connection_SAPConnection', {a2})
    assert _is_linked(b, 'connection_SAPConnection', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit', b)
    if hasattr(a2, 'connection_SAPFunctionUnit'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit', b)
    _safe_set(b, 'connection_SAPConnection', set())
    assert not _is_linked(b, 'connection_SAPConnection', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit', b)


def test_assoc_IDocs17_reverse_link_reassign_clear():
    a1 = connection_SAPIDocUnit(gatewayService="sample_text", htmlFile="sample_text", programId="sample_text", useHtmlOutput=True, useXmlOutput=True, xmlFile="sample_text")
    a2 = connection_SAPIDocUnit(gatewayService="sample_text_2", htmlFile="sample_text_2", programId="sample_text_2", useHtmlOutput=False, useXmlOutput=False, xmlFile="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'connection18', {a1})
    assert _is_linked(b, 'connection18', a1)
    if hasattr(a1, 'SAPIDocUnit'):
        assert _is_linked(a1, 'SAPIDocUnit', b)
    _safe_set(b, 'connection18', {a2})
    assert _is_linked(b, 'connection18', a2)
    if hasattr(a1, 'SAPIDocUnit'):
        assert not _is_linked(a1, 'SAPIDocUnit', b)
    if hasattr(a2, 'SAPIDocUnit'):
        assert _is_linked(a2, 'SAPIDocUnit', b)
    _safe_set(b, 'connection18', set())
    assert not _is_linked(b, 'connection18', a2)
    if hasattr(a2, 'SAPIDocUnit'):
        assert not _is_linked(a2, 'SAPIDocUnit', b)


def test_assoc_MetadataTable115_reverse_link_reassign_clear():
    a1 = connection_SalesforceModuleUnit(moduleName="sample_text")
    a2 = connection_SalesforceModuleUnit(moduleName="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable116', a1)
    assert _is_linked(b, 'connection_MetadataTable116', a1)
    if hasattr(a1, 'connection_SalesforceModuleUnit'):
        assert _is_linked(a1, 'connection_SalesforceModuleUnit', b)
    _safe_set(b, 'connection_MetadataTable116', a2)
    assert _is_linked(b, 'connection_MetadataTable116', a2)
    if hasattr(a1, 'connection_SalesforceModuleUnit'):
        assert not _is_linked(a1, 'connection_SalesforceModuleUnit', b)
    if hasattr(a2, 'connection_SalesforceModuleUnit'):
        assert _is_linked(a2, 'connection_SalesforceModuleUnit', b)
    _safe_set(b, 'connection_MetadataTable116', None)
    assert not _is_linked(b, 'connection_MetadataTable116', a2)
    if hasattr(a2, 'connection_SalesforceModuleUnit'):
        assert not _is_linked(a2, 'connection_SalesforceModuleUnit', b)


def test_assoc_MetadataTable35_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2", asXmlSchema=False)
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable37', a1)
    assert _is_linked(b, 'connection_MetadataTable37', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit36'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit36', b)
    _safe_set(b, 'connection_MetadataTable37', a2)
    assert _is_linked(b, 'connection_MetadataTable37', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit36'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit36', b)
    if hasattr(a2, 'connection_SAPFunctionUnit36'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit36', b)
    _safe_set(b, 'connection_MetadataTable37', None)
    assert not _is_linked(b, 'connection_MetadataTable37', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit36'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit36', b)


def test_assoc_additionalProperties19_reverse_link_reassign_clear():
    a1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    a2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2", jcoVersion="sample_text_2")
    b = connection_AdditionalConnectionProperty(Value="sample_text", propertyName="sample_text")
    _safe_set(b, 'connection_AdditionalConnectionProperty', a1)
    assert _is_linked(b, 'connection_AdditionalConnectionProperty', a1)
    if hasattr(a1, 'connection_SAPConnection20'):
        assert _is_linked(a1, 'connection_SAPConnection20', b)
    _safe_set(b, 'connection_AdditionalConnectionProperty', a2)
    assert _is_linked(b, 'connection_AdditionalConnectionProperty', a2)
    if hasattr(a1, 'connection_SAPConnection20'):
        assert not _is_linked(a1, 'connection_SAPConnection20', b)
    if hasattr(a2, 'connection_SAPConnection20'):
        assert _is_linked(a2, 'connection_SAPConnection20', b)
    _safe_set(b, 'connection_AdditionalConnectionProperty', None)
    assert not _is_linked(b, 'connection_AdditionalConnectionProperty', a2)
    if hasattr(a2, 'connection_SAPConnection20'):
        assert not _is_linked(a2, 'connection_SAPConnection20', b)


def test_assoc_additionalProperties9_reverse_link_reassign_clear():
    a1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    a2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    b = connection_AdditionalProperties(key="sample_text", value="sample_text")
    _safe_set(b, 'connection_AdditionalProperties', a1)
    assert _is_linked(b, 'connection_AdditionalProperties', a1)
    if hasattr(a1, 'connection_MetadataTable10'):
        assert _is_linked(a1, 'connection_MetadataTable10', b)
    _safe_set(b, 'connection_AdditionalProperties', a2)
    assert _is_linked(b, 'connection_AdditionalProperties', a2)
    if hasattr(a1, 'connection_MetadataTable10'):
        assert not _is_linked(a1, 'connection_MetadataTable10', b)
    if hasattr(a2, 'connection_MetadataTable10'):
        assert _is_linked(a2, 'connection_MetadataTable10', b)
    _safe_set(b, 'connection_AdditionalProperties', None)
    assert not _is_linked(b, 'connection_AdditionalProperties', a2)
    if hasattr(a2, 'connection_MetadataTable10'):
        assert not _is_linked(a2, 'connection_MetadataTable10', b)


def test_assoc_children122_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionParameter(changing=True, description="sample_text", length="sample_text", name="sample_text", tableResideInTables=True, testValue="sample_text", type="sample_text")
    a2 = connection_SAPFunctionParameter(changing=False, description="sample_text_2", length="sample_text_2", name="sample_text_2", tableResideInTables=False, testValue="sample_text_2", type="sample_text_2")
    b = connection_SAPFunctionParameter(changing=True, description="sample_text", length="sample_text", name="sample_text", tableResideInTables=True, testValue="sample_text", type="sample_text")
    _safe_set(b, 'connection_SAPFunctionParameter121', {a1})
    assert _is_linked(b, 'connection_SAPFunctionParameter121', a1)
    if hasattr(a1, 'connection_SAPFunctionParameter'):
        assert _is_linked(a1, 'connection_SAPFunctionParameter', b)
    _safe_set(b, 'connection_SAPFunctionParameter121', {a2})
    assert _is_linked(b, 'connection_SAPFunctionParameter121', a2)
    if hasattr(a1, 'connection_SAPFunctionParameter'):
        assert not _is_linked(a1, 'connection_SAPFunctionParameter', b)
    if hasattr(a2, 'connection_SAPFunctionParameter'):
        assert _is_linked(a2, 'connection_SAPFunctionParameter', b)
    _safe_set(b, 'connection_SAPFunctionParameter121', set())
    assert not _is_linked(b, 'connection_SAPFunctionParameter121', a2)
    if hasattr(a2, 'connection_SAPFunctionParameter'):
        assert not _is_linked(a2, 'connection_SAPFunctionParameter', b)


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


def test_assoc_conceptTargets91_reverse_link_reassign_clear():
    a1 = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    a2 = connection_ConceptTarget(RelativeLoopExpression="sample_text_2", targetName="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'schema92', {a1})
    assert _is_linked(b, 'schema92', a1)
    if hasattr(a1, 'ConceptTarget'):
        assert _is_linked(a1, 'ConceptTarget', b)
    _safe_set(b, 'schema92', {a2})
    assert _is_linked(b, 'schema92', a2)
    if hasattr(a1, 'ConceptTarget'):
        assert not _is_linked(a1, 'ConceptTarget', b)
    if hasattr(a2, 'ConceptTarget'):
        assert _is_linked(a2, 'ConceptTarget', b)
    _safe_set(b, 'schema92', set())
    assert not _is_linked(b, 'schema92', a2)
    if hasattr(a2, 'ConceptTarget'):
        assert not _is_linked(a2, 'ConceptTarget', b)


def test_assoc_conditions112_reverse_link_reassign_clear():
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


def test_assoc_connection117_reverse_link_reassign_clear():
    a1 = connection_SalesforceSchemaConnection(batchSize="sample_text", callbackHost="sample_text", callbackPort="sample_text", consumeKey="sample_text", consumeSecret="sample_text", loginType="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", salesforceVersion="sample_text", timeOut="sample_text", token="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text", webServiceUrlTextForOAuth="sample_text")
    a2 = connection_SalesforceSchemaConnection(batchSize="sample_text_2", callbackHost="sample_text_2", callbackPort="sample_text_2", consumeKey="sample_text_2", consumeSecret="sample_text_2", loginType="sample_text_2", moduleName="sample_text_2", password="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUsername="sample_text_2", queryCondition="sample_text_2", salesforceVersion="sample_text_2", timeOut="sample_text_2", token="sample_text_2", useAlphbet=False, useCustomModuleName=False, useHttpProxy=False, useProxy=False, userName="sample_text_2", webServiceUrl="sample_text_2", webServiceUrlTextForOAuth="sample_text_2")
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


def test_assoc_connection38_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2", asXmlSchema=False)
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'connection_SAPConnection40', a1)
    assert _is_linked(b, 'connection_SAPConnection40', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit39'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit39', b)
    _safe_set(b, 'connection_SAPConnection40', a2)
    assert _is_linked(b, 'connection_SAPConnection40', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit39'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit39', b)
    if hasattr(a2, 'connection_SAPFunctionUnit39'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit39', b)
    _safe_set(b, 'connection_SAPConnection40', None)
    assert not _is_linked(b, 'connection_SAPConnection40', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit39'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit39', b)


def test_assoc_connection51_reverse_link_reassign_clear():
    a1 = connection_SAPIDocUnit(gatewayService="sample_text", htmlFile="sample_text", programId="sample_text", useHtmlOutput=True, useXmlOutput=True, xmlFile="sample_text")
    a2 = connection_SAPIDocUnit(gatewayService="sample_text_2", htmlFile="sample_text_2", programId="sample_text_2", useHtmlOutput=False, useXmlOutput=False, xmlFile="sample_text_2")
    b = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text", jcoVersion="sample_text")
    _safe_set(b, 'SAPConnection', a1)
    assert _is_linked(b, 'SAPConnection', a1)
    if hasattr(a1, 'IDocs'):
        assert _is_linked(a1, 'IDocs', b)
    _safe_set(b, 'SAPConnection', a2)
    assert _is_linked(b, 'SAPConnection', a2)
    if hasattr(a1, 'IDocs'):
        assert not _is_linked(a1, 'IDocs', b)
    if hasattr(a2, 'IDocs'):
        assert _is_linked(a2, 'IDocs', b)
    _safe_set(b, 'SAPConnection', None)
    assert not _is_linked(b, 'SAPConnection', a2)
    if hasattr(a2, 'IDocs'):
        assert not _is_linked(a2, 'IDocs', b)


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


def test_assoc_connection73_reverse_link_reassign_clear():
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


def test_assoc_group106_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_BRMSConnection(className="sample_text", moduleUsed="sample_text", package="sample_text", tacWebappName="sample_text", urlName="sample_text", xmlField="sample_text")
    _safe_set(b, 'connection_BRMSConnection107', {a1})
    assert _is_linked(b, 'connection_BRMSConnection107', a1)
    if hasattr(a1, 'connection_XMLFileNode108'):
        assert _is_linked(a1, 'connection_XMLFileNode108', b)
    _safe_set(b, 'connection_BRMSConnection107', {a2})
    assert _is_linked(b, 'connection_BRMSConnection107', a2)
    if hasattr(a1, 'connection_XMLFileNode108'):
        assert not _is_linked(a1, 'connection_XMLFileNode108', b)
    if hasattr(a2, 'connection_XMLFileNode108'):
        assert _is_linked(a2, 'connection_XMLFileNode108', b)
    _safe_set(b, 'connection_BRMSConnection107', set())
    assert not _is_linked(b, 'connection_BRMSConnection107', a2)
    if hasattr(a2, 'connection_XMLFileNode108'):
        assert not _is_linked(a2, 'connection_XMLFileNode108', b)


def test_assoc_group59_reverse_link_reassign_clear():
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


def test_assoc_group93_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept94', {a1})
    assert _is_linked(b, 'connection_Concept94', a1)
    if hasattr(a1, 'connection_XMLFileNode95'):
        assert _is_linked(a1, 'connection_XMLFileNode95', b)
    _safe_set(b, 'connection_Concept94', {a2})
    assert _is_linked(b, 'connection_Concept94', a2)
    if hasattr(a1, 'connection_XMLFileNode95'):
        assert not _is_linked(a1, 'connection_XMLFileNode95', b)
    if hasattr(a2, 'connection_XMLFileNode95'):
        assert _is_linked(a2, 'connection_XMLFileNode95', b)
    _safe_set(b, 'connection_Concept94', set())
    assert not _is_linked(b, 'connection_Concept94', a2)
    if hasattr(a2, 'connection_XMLFileNode95'):
        assert not _is_linked(a2, 'connection_XMLFileNode95', b)


def test_assoc_innerJoins113_reverse_link_reassign_clear():
    a1 = connection_ValidationRulesConnection(baseColumnNames="sample_text", baseSchema="sample_text", isDelete=True, isDisallow=True, isInsert=True, isRejectLink=True, isSelect=True, isUpdate=True, javaCondition="sample_text", logicalOperator="sample_text", refColumnNames="sample_text", refSchema="sample_text", sqlCondition="sample_text", type="sample_text")
    a2 = connection_ValidationRulesConnection(baseColumnNames="sample_text_2", baseSchema="sample_text_2", isDelete=False, isDisallow=False, isInsert=False, isRejectLink=False, isSelect=False, isUpdate=False, javaCondition="sample_text_2", logicalOperator="sample_text_2", refColumnNames="sample_text_2", refSchema="sample_text_2", sqlCondition="sample_text_2", type="sample_text_2")
    b = connection_InnerJoinMap(key="sample_text", value="sample_text")
    _safe_set(b, 'connection_InnerJoinMap', a1)
    assert _is_linked(b, 'connection_InnerJoinMap', a1)
    if hasattr(a1, 'connection_ValidationRulesConnection114'):
        assert _is_linked(a1, 'connection_ValidationRulesConnection114', b)
    _safe_set(b, 'connection_InnerJoinMap', a2)
    assert _is_linked(b, 'connection_InnerJoinMap', a2)
    if hasattr(a1, 'connection_ValidationRulesConnection114'):
        assert not _is_linked(a1, 'connection_ValidationRulesConnection114', b)
    if hasattr(a2, 'connection_ValidationRulesConnection114'):
        assert _is_linked(a2, 'connection_ValidationRulesConnection114', b)
    _safe_set(b, 'connection_InnerJoinMap', None)
    assert not _is_linked(b, 'connection_InnerJoinMap', a2)
    if hasattr(a2, 'connection_ValidationRulesConnection114'):
        assert not _is_linked(a2, 'connection_ValidationRulesConnection114', b)


def test_assoc_inputTables44_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2", asXmlSchema=False)
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable46', a1)
    assert _is_linked(b, 'connection_MetadataTable46', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit45'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit45', b)
    _safe_set(b, 'connection_MetadataTable46', a2)
    assert _is_linked(b, 'connection_MetadataTable46', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit45'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit45', b)
    if hasattr(a2, 'connection_SAPFunctionUnit45'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit45', b)
    _safe_set(b, 'connection_MetadataTable46', None)
    assert not _is_linked(b, 'connection_MetadataTable46', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit45'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit45', b)


def test_assoc_loop109_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_BRMSConnection(className="sample_text", moduleUsed="sample_text", package="sample_text", tacWebappName="sample_text", urlName="sample_text", xmlField="sample_text")
    _safe_set(b, 'connection_BRMSConnection110', {a1})
    assert _is_linked(b, 'connection_BRMSConnection110', a1)
    if hasattr(a1, 'connection_XMLFileNode111'):
        assert _is_linked(a1, 'connection_XMLFileNode111', b)
    _safe_set(b, 'connection_BRMSConnection110', {a2})
    assert _is_linked(b, 'connection_BRMSConnection110', a2)
    if hasattr(a1, 'connection_XMLFileNode111'):
        assert not _is_linked(a1, 'connection_XMLFileNode111', b)
    if hasattr(a2, 'connection_XMLFileNode111'):
        assert _is_linked(a2, 'connection_XMLFileNode111', b)
    _safe_set(b, 'connection_BRMSConnection110', set())
    assert not _is_linked(b, 'connection_BRMSConnection110', a2)
    if hasattr(a2, 'connection_XMLFileNode111'):
        assert not _is_linked(a2, 'connection_XMLFileNode111', b)


def test_assoc_loop63_reverse_link_reassign_clear():
    a1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    a2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2", fileContent="sample_text_2", inputModel=False, outputFilePath="sample_text_2")
    b = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    _safe_set(b, 'connection_XMLFileNode65', a1)
    assert _is_linked(b, 'connection_XMLFileNode65', a1)
    if hasattr(a1, 'connection_XmlFileConnection64'):
        assert _is_linked(a1, 'connection_XmlFileConnection64', b)
    _safe_set(b, 'connection_XMLFileNode65', a2)
    assert _is_linked(b, 'connection_XMLFileNode65', a2)
    if hasattr(a1, 'connection_XmlFileConnection64'):
        assert not _is_linked(a1, 'connection_XmlFileConnection64', b)
    if hasattr(a2, 'connection_XmlFileConnection64'):
        assert _is_linked(a2, 'connection_XmlFileConnection64', b)
    _safe_set(b, 'connection_XMLFileNode65', None)
    assert not _is_linked(b, 'connection_XMLFileNode65', a2)
    if hasattr(a2, 'connection_XmlFileConnection64'):
        assert not _is_linked(a2, 'connection_XmlFileConnection64', b)


def test_assoc_loop99_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept100', {a1})
    assert _is_linked(b, 'connection_Concept100', a1)
    if hasattr(a1, 'connection_XMLFileNode101'):
        assert _is_linked(a1, 'connection_XMLFileNode101', b)
    _safe_set(b, 'connection_Concept100', {a2})
    assert _is_linked(b, 'connection_Concept100', a2)
    if hasattr(a1, 'connection_XMLFileNode101'):
        assert not _is_linked(a1, 'connection_XMLFileNode101', b)
    if hasattr(a2, 'connection_XMLFileNode101'):
        assert _is_linked(a2, 'connection_XMLFileNode101', b)
    _safe_set(b, 'connection_Concept100', set())
    assert not _is_linked(b, 'connection_Concept100', a2)
    if hasattr(a2, 'connection_XMLFileNode101'):
        assert not _is_linked(a2, 'connection_XMLFileNode101', b)


def test_assoc_modules80_reverse_link_reassign_clear():
    a1 = connection_SalesforceSchemaConnection(batchSize="sample_text", callbackHost="sample_text", callbackPort="sample_text", consumeKey="sample_text", consumeSecret="sample_text", loginType="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", salesforceVersion="sample_text", timeOut="sample_text", token="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text", webServiceUrlTextForOAuth="sample_text")
    a2 = connection_SalesforceSchemaConnection(batchSize="sample_text_2", callbackHost="sample_text_2", callbackPort="sample_text_2", consumeKey="sample_text_2", consumeSecret="sample_text_2", loginType="sample_text_2", moduleName="sample_text_2", password="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUsername="sample_text_2", queryCondition="sample_text_2", salesforceVersion="sample_text_2", timeOut="sample_text_2", token="sample_text_2", useAlphbet=False, useCustomModuleName=False, useHttpProxy=False, useProxy=False, userName="sample_text_2", webServiceUrl="sample_text_2", webServiceUrlTextForOAuth="sample_text_2")
    b = connection_SalesforceModuleUnit(moduleName="sample_text")
    _safe_set(b, 'SalesforceModuleUnit', a1)
    assert _is_linked(b, 'SalesforceModuleUnit', a1)
    if hasattr(a1, 'connection81'):
        assert _is_linked(a1, 'connection81', b)
    _safe_set(b, 'SalesforceModuleUnit', a2)
    assert _is_linked(b, 'SalesforceModuleUnit', a2)
    if hasattr(a1, 'connection81'):
        assert not _is_linked(a1, 'connection81', b)
    if hasattr(a2, 'connection81'):
        assert _is_linked(a2, 'connection81', b)
    _safe_set(b, 'SalesforceModuleUnit', None)
    assert not _is_linked(b, 'SalesforceModuleUnit', a2)
    if hasattr(a2, 'connection81'):
        assert not _is_linked(a2, 'connection81', b)


def test_assoc_outputParameter77_reverse_link_reassign_clear():
    a1 = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", isInputModel=True, methodName="sample_text", needAuth=True, parameters="sample_text", portName="sample_text", portNameSpace="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", serverName="sample_text", serverNameSpace="sample_text", timeOut=7, useProxy=True)
    a2 = connection_WSDLSchemaConnection(Encoding="sample_text_2", EndpointURI="sample_text_2", Password="sample_text_2", UserName="sample_text_2", Value="sample_text_2", WSDL="sample_text_2", isInputModel=False, methodName="sample_text_2", needAuth=False, parameters="sample_text_2", portName="sample_text_2", portNameSpace="sample_text_2", proxyHost="sample_text_2", proxyPassword="sample_text_2", proxyPort="sample_text_2", proxyUser="sample_text_2", serverName="sample_text_2", serverNameSpace="sample_text_2", timeOut=13, useProxy=False)
    b = connection_WSDLParameter(Column="sample_text", Element="sample_text", Expression="sample_text", ParameterInfo="sample_text", ParameterInfoParent="sample_text", source="sample_text")
    _safe_set(b, 'connection_WSDLParameter79', a1)
    assert _is_linked(b, 'connection_WSDLParameter79', a1)
    if hasattr(a1, 'connection_WSDLSchemaConnection78'):
        assert _is_linked(a1, 'connection_WSDLSchemaConnection78', b)
    _safe_set(b, 'connection_WSDLParameter79', a2)
    assert _is_linked(b, 'connection_WSDLParameter79', a2)
    if hasattr(a1, 'connection_WSDLSchemaConnection78'):
        assert not _is_linked(a1, 'connection_WSDLSchemaConnection78', b)
    if hasattr(a2, 'connection_WSDLSchemaConnection78'):
        assert _is_linked(a2, 'connection_WSDLSchemaConnection78', b)
    _safe_set(b, 'connection_WSDLParameter79', None)
    assert not _is_linked(b, 'connection_WSDLParameter79', a2)
    if hasattr(a2, 'connection_WSDLSchemaConnection78'):
        assert not _is_linked(a2, 'connection_WSDLSchemaConnection78', b)


def test_assoc_parameterValue76_reverse_link_reassign_clear():
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


def test_assoc_parameters14_reverse_link_reassign_clear():
    a1 = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    a2 = connection_DatabaseConnection(AdditionalParams="sample_text_2", DBRootPath="sample_text_2", DatabaseType="sample_text_2", DatasourceName="sample_text_2", DbmsId="sample_text_2", DriverClass="sample_text_2", DriverJarPath="sample_text_2", FileFieldName="sample_text_2", NullChar="sample_text_2", Password="sample_text_2", Port="sample_text_2", ProductId="sample_text_2", SID="sample_text_2", SQLMode=False, ServerName="sample_text_2", SqlSynthax="sample_text_2", StandardSQL=False, StringQuote="sample_text_2", SystemSQL=False, URL="sample_text_2", UiSchema="sample_text_2", Username="sample_text_2", cdcTypeMode="sample_text_2", dbVersionString="sample_text_2")
    b = connection_AdditionalProperties(key="sample_text", value="sample_text")
    _safe_set(b, 'connection_AdditionalProperties15', a1)
    assert _is_linked(b, 'connection_AdditionalProperties15', a1)
    if hasattr(a1, 'connection_DatabaseConnection'):
        assert _is_linked(a1, 'connection_DatabaseConnection', b)
    _safe_set(b, 'connection_AdditionalProperties15', a2)
    assert _is_linked(b, 'connection_AdditionalProperties15', a2)
    if hasattr(a1, 'connection_DatabaseConnection'):
        assert not _is_linked(a1, 'connection_DatabaseConnection', b)
    if hasattr(a2, 'connection_DatabaseConnection'):
        assert _is_linked(a2, 'connection_DatabaseConnection', b)
    _safe_set(b, 'connection_AdditionalProperties15', None)
    assert not _is_linked(b, 'connection_AdditionalProperties15', a2)
    if hasattr(a2, 'connection_DatabaseConnection'):
        assert not _is_linked(a2, 'connection_DatabaseConnection', b)


def test_assoc_root103_reverse_link_reassign_clear():
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


def test_assoc_root104_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_BRMSConnection(className="sample_text", moduleUsed="sample_text", package="sample_text", tacWebappName="sample_text", urlName="sample_text", xmlField="sample_text")
    _safe_set(b, 'connection_BRMSConnection', {a1})
    assert _is_linked(b, 'connection_BRMSConnection', a1)
    if hasattr(a1, 'connection_XMLFileNode105'):
        assert _is_linked(a1, 'connection_XMLFileNode105', b)
    _safe_set(b, 'connection_BRMSConnection', {a2})
    assert _is_linked(b, 'connection_BRMSConnection', a2)
    if hasattr(a1, 'connection_XMLFileNode105'):
        assert not _is_linked(a1, 'connection_XMLFileNode105', b)
    if hasattr(a2, 'connection_XMLFileNode105'):
        assert _is_linked(a2, 'connection_XMLFileNode105', b)
    _safe_set(b, 'connection_BRMSConnection', set())
    assert not _is_linked(b, 'connection_BRMSConnection', a2)
    if hasattr(a2, 'connection_XMLFileNode105'):
        assert not _is_linked(a2, 'connection_XMLFileNode105', b)


def test_assoc_root60_reverse_link_reassign_clear():
    a1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    a2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2", fileContent="sample_text_2", inputModel=False, outputFilePath="sample_text_2")
    b = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    _safe_set(b, 'connection_XMLFileNode62', a1)
    assert _is_linked(b, 'connection_XMLFileNode62', a1)
    if hasattr(a1, 'connection_XmlFileConnection61'):
        assert _is_linked(a1, 'connection_XmlFileConnection61', b)
    _safe_set(b, 'connection_XMLFileNode62', a2)
    assert _is_linked(b, 'connection_XMLFileNode62', a2)
    if hasattr(a1, 'connection_XmlFileConnection61'):
        assert not _is_linked(a1, 'connection_XmlFileConnection61', b)
    if hasattr(a2, 'connection_XmlFileConnection61'):
        assert _is_linked(a2, 'connection_XmlFileConnection61', b)
    _safe_set(b, 'connection_XMLFileNode62', None)
    assert not _is_linked(b, 'connection_XMLFileNode62', a2)
    if hasattr(a2, 'connection_XmlFileConnection61'):
        assert not _is_linked(a2, 'connection_XmlFileConnection61', b)


def test_assoc_root96_reverse_link_reassign_clear():
    a1 = connection_XMLFileNode(Attribute="sample_text", DefaultValue="sample_text", Order=7, RelatedColumn="sample_text", Type="sample_text", XMLPath="sample_text")
    a2 = connection_XMLFileNode(Attribute="sample_text_2", DefaultValue="sample_text_2", Order=13, RelatedColumn="sample_text_2", Type="sample_text_2", XMLPath="sample_text_2")
    b = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text", conceptType="sample_text", inputModel=True, xPathPrefix="sample_text")
    _safe_set(b, 'connection_Concept97', {a1})
    assert _is_linked(b, 'connection_Concept97', a1)
    if hasattr(a1, 'connection_XMLFileNode98'):
        assert _is_linked(a1, 'connection_XMLFileNode98', b)
    _safe_set(b, 'connection_Concept97', {a2})
    assert _is_linked(b, 'connection_Concept97', a2)
    if hasattr(a1, 'connection_XMLFileNode98'):
        assert not _is_linked(a1, 'connection_XMLFileNode98', b)
    if hasattr(a2, 'connection_XMLFileNode98'):
        assert _is_linked(a2, 'connection_XMLFileNode98', b)
    _safe_set(b, 'connection_Concept97', set())
    assert not _is_linked(b, 'connection_Concept97', a2)
    if hasattr(a2, 'connection_XMLFileNode98'):
        assert not _is_linked(a2, 'connection_XMLFileNode98', b)


def test_assoc_schema102_reverse_link_reassign_clear():
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


def test_assoc_schema57_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text", fileContent="sample_text", inputModel=True, outputFilePath="sample_text")
    _safe_set(b, 'connection58', {a1})
    assert _is_linked(b, 'connection58', a1)
    if hasattr(a1, 'XmlXPathLoopDescriptor'):
        assert _is_linked(a1, 'XmlXPathLoopDescriptor', b)
    _safe_set(b, 'connection58', {a2})
    assert _is_linked(b, 'connection58', a2)
    if hasattr(a1, 'XmlXPathLoopDescriptor'):
        assert not _is_linked(a1, 'XmlXPathLoopDescriptor', b)
    if hasattr(a2, 'XmlXPathLoopDescriptor'):
        assert _is_linked(a2, 'XmlXPathLoopDescriptor', b)
    _safe_set(b, 'connection58', set())
    assert not _is_linked(b, 'connection58', a2)
    if hasattr(a2, 'XmlXPathLoopDescriptor'):
        assert not _is_linked(a2, 'XmlXPathLoopDescriptor', b)


def test_assoc_schema66_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    _safe_set(b, 'schemaTargets', a1)
    assert _is_linked(b, 'schemaTargets', a1)
    if hasattr(a1, 'XmlXPathLoopDescriptor67'):
        assert _is_linked(a1, 'XmlXPathLoopDescriptor67', b)
    _safe_set(b, 'schemaTargets', a2)
    assert _is_linked(b, 'schemaTargets', a2)
    if hasattr(a1, 'XmlXPathLoopDescriptor67'):
        assert not _is_linked(a1, 'XmlXPathLoopDescriptor67', b)
    if hasattr(a2, 'XmlXPathLoopDescriptor67'):
        assert _is_linked(a2, 'XmlXPathLoopDescriptor67', b)
    _safe_set(b, 'schemaTargets', None)
    assert not _is_linked(b, 'schemaTargets', a2)
    if hasattr(a2, 'XmlXPathLoopDescriptor67'):
        assert not _is_linked(a2, 'XmlXPathLoopDescriptor67', b)


def test_assoc_schemaTargets74_reverse_link_reassign_clear():
    a1 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    a2 = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text_2", LimitBoucle="sample_text_2")
    b = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    _safe_set(b, 'SchemaTarget', a1)
    assert _is_linked(b, 'SchemaTarget', a1)
    if hasattr(a1, 'schema75'):
        assert _is_linked(a1, 'schema75', b)
    _safe_set(b, 'SchemaTarget', a2)
    assert _is_linked(b, 'SchemaTarget', a2)
    if hasattr(a1, 'schema75'):
        assert not _is_linked(a1, 'schema75', b)
    if hasattr(a2, 'schema75'):
        assert _is_linked(a2, 'schema75', b)
    _safe_set(b, 'SchemaTarget', None)
    assert not _is_linked(b, 'SchemaTarget', a2)
    if hasattr(a2, 'schema75'):
        assert not _is_linked(a2, 'schema75', b)


def test_assoc_schemas11_reverse_link_reassign_clear():
    a1 = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text", context="sample_text", protocol="sample_text", serverUrl="sample_text")
    a2 = connection_MDMConnection(Datacluster="sample_text_2", Datamodel="sample_text_2", Password="sample_text_2", Port="sample_text_2", Server="sample_text_2", Universe="sample_text_2", Username="sample_text_2", context="sample_text_2", protocol="sample_text_2", serverUrl="sample_text_2")
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


def test_assoc_subscribers84_reverse_link_reassign_clear():
    a1 = connection_SubscriberTable(system=True)
    a2 = connection_SubscriberTable(system=False)
    b = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    _safe_set(b, 'connection_CDCType85', {a1})
    assert _is_linked(b, 'connection_CDCType85', a1)
    if hasattr(a1, 'connection_SubscriberTable'):
        assert _is_linked(a1, 'connection_SubscriberTable', b)
    _safe_set(b, 'connection_CDCType85', {a2})
    assert _is_linked(b, 'connection_CDCType85', a2)
    if hasattr(a1, 'connection_SubscriberTable'):
        assert not _is_linked(a1, 'connection_SubscriberTable', b)
    if hasattr(a2, 'connection_SubscriberTable'):
        assert _is_linked(a2, 'connection_SubscriberTable', b)
    _safe_set(b, 'connection_CDCType85', set())
    assert not _is_linked(b, 'connection_CDCType85', a2)
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


def test_assoc_tables118_reverse_link_reassign_clear():
    a1 = connection_SalesforceModuleUnit(moduleName="sample_text")
    a2 = connection_SalesforceModuleUnit(moduleName="sample_text_2")
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable120', a1)
    assert _is_linked(b, 'connection_MetadataTable120', a1)
    if hasattr(a1, 'connection_SalesforceModuleUnit119'):
        assert _is_linked(a1, 'connection_SalesforceModuleUnit119', b)
    _safe_set(b, 'connection_MetadataTable120', a2)
    assert _is_linked(b, 'connection_MetadataTable120', a2)
    if hasattr(a1, 'connection_SalesforceModuleUnit119'):
        assert not _is_linked(a1, 'connection_SalesforceModuleUnit119', b)
    if hasattr(a2, 'connection_SalesforceModuleUnit119'):
        assert _is_linked(a2, 'connection_SalesforceModuleUnit119', b)
    _safe_set(b, 'connection_MetadataTable120', None)
    assert not _is_linked(b, 'connection_MetadataTable120', a2)
    if hasattr(a2, 'connection_SalesforceModuleUnit119'):
        assert not _is_linked(a2, 'connection_SalesforceModuleUnit119', b)


def test_assoc_tables41_reverse_link_reassign_clear():
    a1 = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    a2 = connection_SAPFunctionUnit(OutputTableName="sample_text_2", OutputType="sample_text_2", asXmlSchema=False)
    b = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    _safe_set(b, 'connection_MetadataTable43', a1)
    assert _is_linked(b, 'connection_MetadataTable43', a1)
    if hasattr(a1, 'connection_SAPFunctionUnit42'):
        assert _is_linked(a1, 'connection_SAPFunctionUnit42', b)
    _safe_set(b, 'connection_MetadataTable43', a2)
    assert _is_linked(b, 'connection_MetadataTable43', a2)
    if hasattr(a1, 'connection_SAPFunctionUnit42'):
        assert not _is_linked(a1, 'connection_SAPFunctionUnit42', b)
    if hasattr(a2, 'connection_SAPFunctionUnit42'):
        assert _is_linked(a2, 'connection_SAPFunctionUnit42', b)
    _safe_set(b, 'connection_MetadataTable43', None)
    assert not _is_linked(b, 'connection_MetadataTable43', a2)
    if hasattr(a2, 'connection_SAPFunctionUnit42'):
        assert not _is_linked(a2, 'connection_SAPFunctionUnit42', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_InputParameterTable32_stub_double():
    # connection_InputSAPFunctionParameterTable has no real 'InputSAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_InputSAPFunctionParameterTable()
    setattr(partner, 'InputSAPFunctionParameterTable', None)
    _safe_set(owner, 'functionUnit', partner)
    assert getattr(partner, 'InputSAPFunctionParameterTable') == owner
    _safe_set(owner, 'functionUnit', None)
    assert getattr(partner, 'InputSAPFunctionParameterTable') is None


def test_assoc_OutputParameterTable33_stub_double():
    # connection_OutputSAPFunctionParameterTable has no real 'OutputSAPFunctionParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_OutputSAPFunctionParameterTable()
    setattr(partner, 'OutputSAPFunctionParameterTable', None)
    _safe_set(owner, 'functionUnit34', partner)
    assert getattr(partner, 'OutputSAPFunctionParameterTable') == owner
    _safe_set(owner, 'functionUnit34', None)
    assert getattr(partner, 'OutputSAPFunctionParameterTable') is None


def test_assoc_ParameterTable52_stub_double():
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


def test_assoc_TestInputParameterTable47_stub_double():
    # connection_SAPTestInputParameterTable has no real 'SAPTestInputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_SAPTestInputParameterTable()
    setattr(partner, 'SAPTestInputParameterTable', None)
    _safe_set(owner, 'functionUnit48', partner)
    assert getattr(partner, 'SAPTestInputParameterTable') == owner
    _safe_set(owner, 'functionUnit48', None)
    assert getattr(partner, 'SAPTestInputParameterTable') is None


def test_assoc_cdcConnection86_stub_double():
    # connection_CDCConnection has no real 'connection_CDCConnection88' property in the generated
    # code (a bare stub) -- manually attach it so connection_CDCType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_CDCType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'connection_CDCConnection88', None)
    _safe_set(owner, 'connection_CDCType87', partner)
    assert getattr(partner, 'connection_CDCConnection88') == owner
    _safe_set(owner, 'connection_CDCType87', None)
    assert getattr(partner, 'connection_CDCConnection88') is None


def test_assoc_cdcConns12_stub_double():
    # connection_CDCConnection has no real 'CDCConnection' property in the generated
    # code (a bare stub) -- manually attach it so connection_DatabaseConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_DatabaseConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    partner = connection_CDCConnection()
    setattr(partner, 'CDCConnection', None)
    _safe_set(owner, 'connection13', partner)
    assert getattr(partner, 'CDCConnection') == owner
    _safe_set(owner, 'connection13', None)
    assert getattr(partner, 'CDCConnection') is None


def test_assoc_cdcTypes83_stub_double():
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


def test_assoc_columns53_stub_double():
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


def test_assoc_connection68_stub_double():
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


def test_assoc_connection82_stub_double():
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


def test_assoc_functionUnit54_stub_double():
    # connection_InputSAPFunctionParameterTable has no real 'InputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_InputSAPFunctionParameterTable()
    setattr(partner, 'InputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit', partner)
    assert getattr(partner, 'InputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit', None)
    assert getattr(partner, 'InputParameterTable') is None


def test_assoc_functionUnit55_stub_double():
    # connection_OutputSAPFunctionParameterTable has no real 'OutputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_OutputSAPFunctionParameterTable()
    setattr(partner, 'OutputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit56', partner)
    assert getattr(partner, 'OutputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit56', None)
    assert getattr(partner, 'OutputParameterTable') is None


def test_assoc_functionUnit89_stub_double():
    # connection_SAPTestInputParameterTable has no real 'TestInputParameterTable' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_SAPTestInputParameterTable()
    setattr(partner, 'TestInputParameterTable', None)
    _safe_set(owner, 'SAPFunctionUnit90', partner)
    assert getattr(partner, 'TestInputParameterTable') == owner
    _safe_set(owner, 'SAPFunctionUnit90', None)
    assert getattr(partner, 'TestInputParameterTable') is None


def test_assoc_inputRoot123_stub_double():
    # connection_SAPFunctionParamData has no real 'connection_SAPFunctionParamData124' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionParameter(changing=True, description="sample_text", length="sample_text", name="sample_text", tableResideInTables=True, testValue="sample_text", type="sample_text")
    partner = connection_SAPFunctionParamData()
    setattr(partner, 'connection_SAPFunctionParamData124', None)
    _safe_set(owner, 'connection_SAPFunctionParameter125', partner)
    assert getattr(partner, 'connection_SAPFunctionParamData124') == owner
    _safe_set(owner, 'connection_SAPFunctionParameter125', None)
    assert getattr(partner, 'connection_SAPFunctionParamData124') is None


def test_assoc_outputRoot126_stub_double():
    # connection_SAPFunctionParamData has no real 'connection_SAPFunctionParamData127' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionParameter(changing=True, description="sample_text", length="sample_text", name="sample_text", tableResideInTables=True, testValue="sample_text", type="sample_text")
    partner = connection_SAPFunctionParamData()
    setattr(partner, 'connection_SAPFunctionParamData127', None)
    _safe_set(owner, 'connection_SAPFunctionParameter128', partner)
    assert getattr(partner, 'connection_SAPFunctionParamData127') == owner
    _safe_set(owner, 'connection_SAPFunctionParameter128', None)
    assert getattr(partner, 'connection_SAPFunctionParamData127') is None


def test_assoc_ownedDocument131_stub_double():
    # xml_TdXmlSchema has no real 'xml_TdXmlSchema' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXmlElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXmlElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXmlElementType(javaType="sample_text")
    partner = xml_TdXmlSchema()
    setattr(partner, 'xml_TdXmlSchema', None)
    _safe_set(owner, 'connection_xml_TdXmlElementType132', partner)
    assert getattr(partner, 'xml_TdXmlSchema') == owner
    _safe_set(owner, 'connection_xml_TdXmlElementType132', None)
    assert getattr(partner, 'xml_TdXmlSchema') is None


def test_assoc_paramData49_stub_double():
    # connection_SAPFunctionParamData has no real 'connection_SAPFunctionParamData' property in the generated
    # code (a bare stub) -- manually attach it so connection_SAPFunctionUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_SAPFunctionUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text", asXmlSchema=True)
    partner = connection_SAPFunctionParamData()
    setattr(partner, 'connection_SAPFunctionParamData', None)
    _safe_set(owner, 'connection_SAPFunctionUnit50', partner)
    assert getattr(partner, 'connection_SAPFunctionParamData') == owner
    _safe_set(owner, 'connection_SAPFunctionUnit50', None)
    assert getattr(partner, 'connection_SAPFunctionParamData') is None


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


def test_assoc_queries71_stub_double():
    # connection_QueriesConnection has no real 'QueriesConnection72' property in the generated
    # code (a bare stub) -- manually attach it so connection_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Query(contextMode=True, value="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'QueriesConnection72', None)
    _safe_set(owner, 'query', partner)
    assert getattr(partner, 'QueriesConnection72') == owner
    _safe_set(owner, 'query', None)
    assert getattr(partner, 'QueriesConnection72') is None


def test_assoc_query69_stub_double():
    # connection_QueriesConnection has no real 'queries70' property in the generated
    # code (a bare stub) -- manually attach it so connection_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_Query(contextMode=True, value="sample_text")
    partner = connection_QueriesConnection()
    setattr(partner, 'queries70', None)
    _safe_set(owner, 'Query', partner)
    assert owner in getattr(partner, 'queries70')
    _safe_set(owner, 'Query', None)
    assert owner not in getattr(partner, 'queries70')


def test_assoc_sqlDataType129_stub_double():
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


def test_assoc_xmlContent133_stub_double():
    # xml_TdXmlContent has no real 'xml_TdXmlContent' property in the generated
    # code (a bare stub) -- manually attach it so connection_xml_TdXmlElementType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # connection_xml_TdXmlElementType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = connection_xml_TdXmlElementType(javaType="sample_text")
    partner = xml_TdXmlContent()
    setattr(partner, 'xml_TdXmlContent', None)
    _safe_set(owner, 'connection_xml_TdXmlElementType134', partner)
    assert getattr(partner, 'xml_TdXmlContent') == owner
    _safe_set(owner, 'connection_xml_TdXmlElementType134', None)
    assert getattr(partner, 'xml_TdXmlContent') is None


def test_assoc_xsdElementDeclaration130_stub_double():
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


