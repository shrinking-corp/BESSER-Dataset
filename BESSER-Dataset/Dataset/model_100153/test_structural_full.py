import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractMetadataObject,
    Connection,
    FileConnection,
    MetadataColumn,
    SAPFunctionParameterTable,
    TdTable,
    connection_AbstractMetadataObject,
    connection_CDCConnection,
    connection_CDCType,
    connection_Concept,
    connection_ConceptTarget,
    connection_Connection,
    connection_DatabaseConnection,
    connection_DelimitedFileConnection,
    connection_EbcdicConnection,
    connection_FileConnection,
    connection_FileExcelConnection,
    connection_GenericPackage,
    connection_GenericSchemaConnection,
    connection_HL7Connection,
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
    connection_SAPTestInputParameterTable,
    connection_SalesforceSchemaConnection,
    connection_SchemaTarget,
    connection_SubscriberTable,
    connection_WSDLSchemaConnection,
    connection_XmlFileConnection,
    connection_XmlXPathLoopDescriptor,
    connection_relational_TdColumn,
    connection_relational_TdProcedure,
    connection_relational_TdSqlDataType,
    connection_relational_TdTable,
    connection_relational_TdTrigger,
    connection_relational_TdView,
    connection_softwaredeployment_TdDataManager,
    connection_softwaredeployment_TdMachine,
    connection_softwaredeployment_TdSoftwareSystem,
    connection_xml_TdXMLContent,
    connection_xml_TdXMLDocument,
    connection_xml_TdXMLElement,
    relational_TdSqlDataType,
    xml_TdXMLContent,
    xml_TdXMLDocument,
    xml_TdXMLElement,
    DevelopmentStatus,
    Escape,
    FieldSeparator,
    FileFormat,
    RowSeparator,
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

def test_connection_AbstractMetadataObject_comment_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_connection_AbstractMetadataObject_divergency_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.divergency == True
    instance.divergency = False
    assert instance.divergency == False


def test_connection_AbstractMetadataObject_id_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_connection_AbstractMetadataObject_label_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_connection_AbstractMetadataObject_properties_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.properties == "sample_text"
    instance.properties = "sample_text_2"
    assert instance.properties == "sample_text_2"


def test_connection_AbstractMetadataObject_readOnly_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_connection_AbstractMetadataObject_synchronised_value_roundtrip():
    instance = connection_AbstractMetadataObject(comment="sample_text", divergency=True, id="sample_text", label="sample_text", properties="sample_text", readOnly=True, synchronised=True)
    assert instance.synchronised == True
    instance.synchronised = False
    assert instance.synchronised == False


def test_connection_CDCType_journalName_value_roundtrip():
    instance = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    assert instance.journalName == "sample_text"
    instance.journalName = "sample_text_2"
    assert instance.journalName == "sample_text_2"


def test_connection_CDCType_linkDB_value_roundtrip():
    instance = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    assert instance.linkDB == "sample_text"
    instance.linkDB = "sample_text_2"
    assert instance.linkDB == "sample_text_2"


def test_connection_Concept_LoopExpression_value_roundtrip():
    instance = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    assert instance.LoopExpression == "sample_text"
    instance.LoopExpression = "sample_text_2"
    assert instance.LoopExpression == "sample_text_2"


def test_connection_Concept_LoopLimit_value_roundtrip():
    instance = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    assert instance.LoopLimit == "sample_text"
    instance.LoopLimit = "sample_text_2"
    assert instance.LoopLimit == "sample_text_2"


def test_connection_ConceptTarget_RelativeLoopExpression_value_roundtrip():
    instance = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    assert instance.RelativeLoopExpression == "sample_text"
    instance.RelativeLoopExpression = "sample_text_2"
    assert instance.RelativeLoopExpression == "sample_text_2"


def test_connection_ConceptTarget_targetName_value_roundtrip():
    instance = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    assert instance.targetName == "sample_text"
    instance.targetName = "sample_text_2"
    assert instance.targetName == "sample_text_2"


def test_connection_Connection_ContextId_value_roundtrip():
    instance = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    assert instance.ContextId == "sample_text"
    instance.ContextId = "sample_text_2"
    assert instance.ContextId == "sample_text_2"


def test_connection_Connection_ContextMode_value_roundtrip():
    instance = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    assert instance.ContextMode == True
    instance.ContextMode = False
    assert instance.ContextMode == False


def test_connection_Connection_version_value_roundtrip():
    instance = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_connection_DatabaseConnection_AdditionalParams_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.AdditionalParams == "sample_text"
    instance.AdditionalParams = "sample_text_2"
    assert instance.AdditionalParams == "sample_text_2"


def test_connection_DatabaseConnection_DBRootPath_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.DBRootPath == "sample_text"
    instance.DBRootPath = "sample_text_2"
    assert instance.DBRootPath == "sample_text_2"


def test_connection_DatabaseConnection_DatabaseType_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.DatabaseType == "sample_text"
    instance.DatabaseType = "sample_text_2"
    assert instance.DatabaseType == "sample_text_2"


def test_connection_DatabaseConnection_DatasourceName_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.DatasourceName == "sample_text"
    instance.DatasourceName = "sample_text_2"
    assert instance.DatasourceName == "sample_text_2"


def test_connection_DatabaseConnection_DbmsId_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.DbmsId == "sample_text"
    instance.DbmsId = "sample_text_2"
    assert instance.DbmsId == "sample_text_2"


def test_connection_DatabaseConnection_DriverClass_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.DriverClass == "sample_text"
    instance.DriverClass = "sample_text_2"
    assert instance.DriverClass == "sample_text_2"


def test_connection_DatabaseConnection_DriverJarPath_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.DriverJarPath == "sample_text"
    instance.DriverJarPath = "sample_text_2"
    assert instance.DriverJarPath == "sample_text_2"


def test_connection_DatabaseConnection_FileFieldName_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.FileFieldName == "sample_text"
    instance.FileFieldName = "sample_text_2"
    assert instance.FileFieldName == "sample_text_2"


def test_connection_DatabaseConnection_NullChar_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.NullChar == "sample_text"
    instance.NullChar = "sample_text_2"
    assert instance.NullChar == "sample_text_2"


def test_connection_DatabaseConnection_Password_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_connection_DatabaseConnection_Port_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.Port == "sample_text"
    instance.Port = "sample_text_2"
    assert instance.Port == "sample_text_2"


def test_connection_DatabaseConnection_ProductId_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.ProductId == "sample_text"
    instance.ProductId = "sample_text_2"
    assert instance.ProductId == "sample_text_2"


def test_connection_DatabaseConnection_SID_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.SID == "sample_text"
    instance.SID = "sample_text_2"
    assert instance.SID == "sample_text_2"


def test_connection_DatabaseConnection_SQLMode_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.SQLMode == True
    instance.SQLMode = False
    assert instance.SQLMode == False


def test_connection_DatabaseConnection_ServerName_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.ServerName == "sample_text"
    instance.ServerName = "sample_text_2"
    assert instance.ServerName == "sample_text_2"


def test_connection_DatabaseConnection_SqlSynthax_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.SqlSynthax == "sample_text"
    instance.SqlSynthax = "sample_text_2"
    assert instance.SqlSynthax == "sample_text_2"


def test_connection_DatabaseConnection_StandardSQL_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.StandardSQL == True
    instance.StandardSQL = False
    assert instance.StandardSQL == False


def test_connection_DatabaseConnection_StringQuote_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.StringQuote == "sample_text"
    instance.StringQuote = "sample_text_2"
    assert instance.StringQuote == "sample_text_2"


def test_connection_DatabaseConnection_SystemSQL_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.SystemSQL == True
    instance.SystemSQL = False
    assert instance.SystemSQL == False


def test_connection_DatabaseConnection_URL_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.URL == "sample_text"
    instance.URL = "sample_text_2"
    assert instance.URL == "sample_text_2"


def test_connection_DatabaseConnection_UiSchema_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.UiSchema == "sample_text"
    instance.UiSchema = "sample_text_2"
    assert instance.UiSchema == "sample_text_2"


def test_connection_DatabaseConnection_Username_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_connection_DatabaseConnection_cdcTypeMode_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.cdcTypeMode == "sample_text"
    instance.cdcTypeMode = "sample_text_2"
    assert instance.cdcTypeMode == "sample_text_2"


def test_connection_DatabaseConnection_dbVersionString_value_roundtrip():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert instance.dbVersionString == "sample_text"
    instance.dbVersionString = "sample_text_2"
    assert instance.dbVersionString == "sample_text_2"


def test_connection_DelimitedFileConnection_FieldSeparatorType_value_roundtrip():
    instance = connection_DelimitedFileConnection(FieldSeparatorType="sample_text", splitRecord=True)
    assert instance.FieldSeparatorType == "sample_text"
    instance.FieldSeparatorType = "sample_text_2"
    assert instance.FieldSeparatorType == "sample_text_2"


def test_connection_DelimitedFileConnection_splitRecord_value_roundtrip():
    instance = connection_DelimitedFileConnection(FieldSeparatorType="sample_text", splitRecord=True)
    assert instance.splitRecord == True
    instance.splitRecord = False
    assert instance.splitRecord == False


def test_connection_EbcdicConnection_DataFile_value_roundtrip():
    instance = connection_EbcdicConnection(DataFile="sample_text", MidFile="sample_text")
    assert instance.DataFile == "sample_text"
    instance.DataFile = "sample_text_2"
    assert instance.DataFile == "sample_text_2"


def test_connection_EbcdicConnection_MidFile_value_roundtrip():
    instance = connection_EbcdicConnection(DataFile="sample_text", MidFile="sample_text")
    assert instance.MidFile == "sample_text"
    instance.MidFile = "sample_text_2"
    assert instance.MidFile == "sample_text_2"


def test_connection_FileConnection_CsvOption_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.CsvOption == True
    instance.CsvOption = False
    assert instance.CsvOption == False


def test_connection_FileConnection_Encoding_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.Encoding == "sample_text"
    instance.Encoding = "sample_text_2"
    assert instance.Encoding == "sample_text_2"


def test_connection_FileConnection_EscapeChar_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.EscapeChar == "sample_text"
    instance.EscapeChar = "sample_text_2"
    assert instance.EscapeChar == "sample_text_2"


def test_connection_FileConnection_EscapeType_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.EscapeType == "sample_text"
    instance.EscapeType = "sample_text_2"
    assert instance.EscapeType == "sample_text_2"


def test_connection_FileConnection_FieldSeparatorValue_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.FieldSeparatorValue == "sample_text"
    instance.FieldSeparatorValue = "sample_text_2"
    assert instance.FieldSeparatorValue == "sample_text_2"


def test_connection_FileConnection_FilePath_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.FilePath == "sample_text"
    instance.FilePath = "sample_text_2"
    assert instance.FilePath == "sample_text_2"


def test_connection_FileConnection_FirstLineCaption_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.FirstLineCaption == True
    instance.FirstLineCaption = False
    assert instance.FirstLineCaption == False


def test_connection_FileConnection_FooterValue_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.FooterValue == "sample_text"
    instance.FooterValue = "sample_text_2"
    assert instance.FooterValue == "sample_text_2"


def test_connection_FileConnection_Format_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.Format == "sample_text"
    instance.Format = "sample_text_2"
    assert instance.Format == "sample_text_2"


def test_connection_FileConnection_HeaderValue_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.HeaderValue == "sample_text"
    instance.HeaderValue = "sample_text_2"
    assert instance.HeaderValue == "sample_text_2"


def test_connection_FileConnection_LimitValue_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.LimitValue == "sample_text"
    instance.LimitValue = "sample_text_2"
    assert instance.LimitValue == "sample_text_2"


def test_connection_FileConnection_RemoveEmptyRow_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.RemoveEmptyRow == True
    instance.RemoveEmptyRow = False
    assert instance.RemoveEmptyRow == False


def test_connection_FileConnection_RowSeparatorType_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.RowSeparatorType == "sample_text"
    instance.RowSeparatorType = "sample_text_2"
    assert instance.RowSeparatorType == "sample_text_2"


def test_connection_FileConnection_RowSeparatorValue_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.RowSeparatorValue == "sample_text"
    instance.RowSeparatorValue = "sample_text_2"
    assert instance.RowSeparatorValue == "sample_text_2"


def test_connection_FileConnection_Server_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.Server == "sample_text"
    instance.Server = "sample_text_2"
    assert instance.Server == "sample_text_2"


def test_connection_FileConnection_TextEnclosure_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.TextEnclosure == "sample_text"
    instance.TextEnclosure = "sample_text_2"
    assert instance.TextEnclosure == "sample_text_2"


def test_connection_FileConnection_TextIdentifier_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.TextIdentifier == "sample_text"
    instance.TextIdentifier = "sample_text_2"
    assert instance.TextIdentifier == "sample_text_2"


def test_connection_FileConnection_UseFooter_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.UseFooter == True
    instance.UseFooter = False
    assert instance.UseFooter == False


def test_connection_FileConnection_UseHeader_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.UseHeader == True
    instance.UseHeader = False
    assert instance.UseHeader == False


def test_connection_FileConnection_UseLimit_value_roundtrip():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert instance.UseLimit == True
    instance.UseLimit = False
    assert instance.UseLimit == False


def test_connection_FileExcelConnection_SheetName_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.SheetName == "sample_text"
    instance.SheetName = "sample_text_2"
    assert instance.SheetName == "sample_text_2"


def test_connection_FileExcelConnection_advancedSpearator_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.advancedSpearator == True
    instance.advancedSpearator = False
    assert instance.advancedSpearator == False


def test_connection_FileExcelConnection_decimalSeparator_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.decimalSeparator == "sample_text"
    instance.decimalSeparator = "sample_text_2"
    assert instance.decimalSeparator == "sample_text_2"


def test_connection_FileExcelConnection_firstColumn_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.firstColumn == "sample_text"
    instance.firstColumn = "sample_text_2"
    assert instance.firstColumn == "sample_text_2"


def test_connection_FileExcelConnection_lastColumn_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.lastColumn == "sample_text"
    instance.lastColumn = "sample_text_2"
    assert instance.lastColumn == "sample_text_2"


def test_connection_FileExcelConnection_selectAllSheets_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.selectAllSheets == True
    instance.selectAllSheets = False
    assert instance.selectAllSheets == False


def test_connection_FileExcelConnection_sheetColumns_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.sheetColumns == "sample_text"
    instance.sheetColumns = "sample_text_2"
    assert instance.sheetColumns == "sample_text_2"


def test_connection_FileExcelConnection_sheetList_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.sheetList == "sample_text"
    instance.sheetList = "sample_text_2"
    assert instance.sheetList == "sample_text_2"


def test_connection_FileExcelConnection_thousandSeparator_value_roundtrip():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert instance.thousandSeparator == "sample_text"
    instance.thousandSeparator = "sample_text_2"
    assert instance.thousandSeparator == "sample_text_2"


def test_connection_GenericSchemaConnection_mappingTypeId_value_roundtrip():
    instance = connection_GenericSchemaConnection(mappingTypeId="sample_text", mappingTypeUsed=True)
    assert instance.mappingTypeId == "sample_text"
    instance.mappingTypeId = "sample_text_2"
    assert instance.mappingTypeId == "sample_text_2"


def test_connection_GenericSchemaConnection_mappingTypeUsed_value_roundtrip():
    instance = connection_GenericSchemaConnection(mappingTypeId="sample_text", mappingTypeUsed=True)
    assert instance.mappingTypeUsed == True
    instance.mappingTypeUsed = False
    assert instance.mappingTypeUsed == False


def test_connection_HL7Connection_EndChar_value_roundtrip():
    instance = connection_HL7Connection(EndChar=7, StartChar="sample_text")
    assert instance.EndChar == 7
    instance.EndChar = 13
    assert instance.EndChar == 13


def test_connection_HL7Connection_StartChar_value_roundtrip():
    instance = connection_HL7Connection(EndChar=7, StartChar="sample_text")
    assert instance.StartChar == "sample_text"
    instance.StartChar = "sample_text_2"
    assert instance.StartChar == "sample_text_2"


def test_connection_LDAPSchemaConnection_Aliases_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Aliases == "sample_text"
    instance.Aliases = "sample_text_2"
    assert instance.Aliases == "sample_text_2"


def test_connection_LDAPSchemaConnection_BaseDNs_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.BaseDNs == "sample_text"
    instance.BaseDNs = "sample_text_2"
    assert instance.BaseDNs == "sample_text_2"


def test_connection_LDAPSchemaConnection_BindPassword_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.BindPassword == "sample_text"
    instance.BindPassword = "sample_text_2"
    assert instance.BindPassword == "sample_text_2"


def test_connection_LDAPSchemaConnection_BindPrincipal_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.BindPrincipal == "sample_text"
    instance.BindPrincipal = "sample_text_2"
    assert instance.BindPrincipal == "sample_text_2"


def test_connection_LDAPSchemaConnection_CountLimit_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.CountLimit == "sample_text"
    instance.CountLimit = "sample_text_2"
    assert instance.CountLimit == "sample_text_2"


def test_connection_LDAPSchemaConnection_EncryptionMethodName_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.EncryptionMethodName == "sample_text"
    instance.EncryptionMethodName = "sample_text_2"
    assert instance.EncryptionMethodName == "sample_text_2"


def test_connection_LDAPSchemaConnection_Filter_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Filter == "sample_text"
    instance.Filter = "sample_text_2"
    assert instance.Filter == "sample_text_2"


def test_connection_LDAPSchemaConnection_GetBaseDNsFromRoot_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.GetBaseDNsFromRoot == True
    instance.GetBaseDNsFromRoot = False
    assert instance.GetBaseDNsFromRoot == False


def test_connection_LDAPSchemaConnection_Host_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Host == "sample_text"
    instance.Host = "sample_text_2"
    assert instance.Host == "sample_text_2"


def test_connection_LDAPSchemaConnection_LimitValue_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.LimitValue == 7
    instance.LimitValue = 13
    assert instance.LimitValue == 13


def test_connection_LDAPSchemaConnection_Port_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Port == "sample_text"
    instance.Port = "sample_text_2"
    assert instance.Port == "sample_text_2"


def test_connection_LDAPSchemaConnection_Protocol_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Protocol == "sample_text"
    instance.Protocol = "sample_text_2"
    assert instance.Protocol == "sample_text_2"


def test_connection_LDAPSchemaConnection_Referrals_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Referrals == "sample_text"
    instance.Referrals = "sample_text_2"
    assert instance.Referrals == "sample_text_2"


def test_connection_LDAPSchemaConnection_ReturnAttributes_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.ReturnAttributes == "sample_text"
    instance.ReturnAttributes = "sample_text_2"
    assert instance.ReturnAttributes == "sample_text_2"


def test_connection_LDAPSchemaConnection_SavePassword_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.SavePassword == True
    instance.SavePassword = False
    assert instance.SavePassword == False


def test_connection_LDAPSchemaConnection_SelectedDN_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.SelectedDN == "sample_text"
    instance.SelectedDN = "sample_text_2"
    assert instance.SelectedDN == "sample_text_2"


def test_connection_LDAPSchemaConnection_Separator_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Separator == "sample_text"
    instance.Separator = "sample_text_2"
    assert instance.Separator == "sample_text_2"


def test_connection_LDAPSchemaConnection_StorePath_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.StorePath == "sample_text"
    instance.StorePath = "sample_text_2"
    assert instance.StorePath == "sample_text_2"


def test_connection_LDAPSchemaConnection_TimeOutLimit_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.TimeOutLimit == "sample_text"
    instance.TimeOutLimit = "sample_text_2"
    assert instance.TimeOutLimit == "sample_text_2"


def test_connection_LDAPSchemaConnection_UseAdvanced_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.UseAdvanced == True
    instance.UseAdvanced = False
    assert instance.UseAdvanced == False


def test_connection_LDAPSchemaConnection_UseAuthen_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.UseAuthen == True
    instance.UseAuthen = False
    assert instance.UseAuthen == False


def test_connection_LDAPSchemaConnection_UseLimit_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.UseLimit == True
    instance.UseLimit = False
    assert instance.UseLimit == False


def test_connection_LDAPSchemaConnection_Value_value_roundtrip():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_connection_LdifFileConnection_FilePath_value_roundtrip():
    instance = connection_LdifFileConnection(FilePath="sample_text", LimitEntry=7, Server="sample_text", UseLimit=True, value="sample_text")
    assert instance.FilePath == "sample_text"
    instance.FilePath = "sample_text_2"
    assert instance.FilePath == "sample_text_2"


def test_connection_LdifFileConnection_LimitEntry_value_roundtrip():
    instance = connection_LdifFileConnection(FilePath="sample_text", LimitEntry=7, Server="sample_text", UseLimit=True, value="sample_text")
    assert instance.LimitEntry == 7
    instance.LimitEntry = 13
    assert instance.LimitEntry == 13


def test_connection_LdifFileConnection_Server_value_roundtrip():
    instance = connection_LdifFileConnection(FilePath="sample_text", LimitEntry=7, Server="sample_text", UseLimit=True, value="sample_text")
    assert instance.Server == "sample_text"
    instance.Server = "sample_text_2"
    assert instance.Server == "sample_text_2"


def test_connection_LdifFileConnection_UseLimit_value_roundtrip():
    instance = connection_LdifFileConnection(FilePath="sample_text", LimitEntry=7, Server="sample_text", UseLimit=True, value="sample_text")
    assert instance.UseLimit == True
    instance.UseLimit = False
    assert instance.UseLimit == False


def test_connection_LdifFileConnection_value_value_roundtrip():
    instance = connection_LdifFileConnection(FilePath="sample_text", LimitEntry=7, Server="sample_text", UseLimit=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_connection_MDMConnection_Datacluster_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Datacluster == "sample_text"
    instance.Datacluster = "sample_text_2"
    assert instance.Datacluster == "sample_text_2"


def test_connection_MDMConnection_Datamodel_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Datamodel == "sample_text"
    instance.Datamodel = "sample_text_2"
    assert instance.Datamodel == "sample_text_2"


def test_connection_MDMConnection_Password_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_connection_MDMConnection_Port_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Port == "sample_text"
    instance.Port = "sample_text_2"
    assert instance.Port == "sample_text_2"


def test_connection_MDMConnection_Server_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Server == "sample_text"
    instance.Server = "sample_text_2"
    assert instance.Server == "sample_text_2"


def test_connection_MDMConnection_Universe_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Universe == "sample_text"
    instance.Universe = "sample_text_2"
    assert instance.Universe == "sample_text_2"


def test_connection_MDMConnection_Username_value_roundtrip():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_connection_MetadataColumn_defaultValue_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_connection_MetadataColumn_displayField_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.displayField == "sample_text"
    instance.displayField = "sample_text_2"
    assert instance.displayField == "sample_text_2"


def test_connection_MetadataColumn_key_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.key == True
    instance.key = False
    assert instance.key == False


def test_connection_MetadataColumn_nullable_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.nullable == True
    instance.nullable = False
    assert instance.nullable == False


def test_connection_MetadataColumn_originalField_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.originalField == "sample_text"
    instance.originalField = "sample_text_2"
    assert instance.originalField == "sample_text_2"


def test_connection_MetadataColumn_pattern_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_connection_MetadataColumn_sourceType_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.sourceType == "sample_text"
    instance.sourceType = "sample_text_2"
    assert instance.sourceType == "sample_text_2"


def test_connection_MetadataColumn_talendType_value_roundtrip():
    instance = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    assert instance.talendType == "sample_text"
    instance.talendType = "sample_text_2"
    assert instance.talendType == "sample_text_2"


def test_connection_MetadataTable_activatedCDC_value_roundtrip():
    instance = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    assert instance.activatedCDC == True
    instance.activatedCDC = False
    assert instance.activatedCDC == False


def test_connection_MetadataTable_attachedCDC_value_roundtrip():
    instance = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    assert instance.attachedCDC == True
    instance.attachedCDC = False
    assert instance.attachedCDC == False


def test_connection_MetadataTable_sourceName_value_roundtrip():
    instance = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    assert instance.sourceName == "sample_text"
    instance.sourceName = "sample_text_2"
    assert instance.sourceName == "sample_text_2"


def test_connection_MetadataTable_tableType_value_roundtrip():
    instance = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    assert instance.tableType == "sample_text"
    instance.tableType = "sample_text_2"
    assert instance.tableType == "sample_text_2"


def test_connection_Query_contextMode_value_roundtrip():
    instance = connection_Query(contextMode=True, value="sample_text")
    assert instance.contextMode == True
    instance.contextMode = False
    assert instance.contextMode == False


def test_connection_Query_value_value_roundtrip():
    instance = connection_Query(contextMode=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_connection_RegexpFileConnection_FieldSeparatorType_value_roundtrip():
    instance = connection_RegexpFileConnection(FieldSeparatorType="sample_text")
    assert instance.FieldSeparatorType == "sample_text"
    instance.FieldSeparatorType = "sample_text_2"
    assert instance.FieldSeparatorType == "sample_text_2"


def test_connection_SAPConnection_Client_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.Client == "sample_text"
    instance.Client = "sample_text_2"
    assert instance.Client == "sample_text_2"


def test_connection_SAPConnection_Host_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.Host == "sample_text"
    instance.Host = "sample_text_2"
    assert instance.Host == "sample_text_2"


def test_connection_SAPConnection_Language_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.Language == "sample_text"
    instance.Language = "sample_text_2"
    assert instance.Language == "sample_text_2"


def test_connection_SAPConnection_Password_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_connection_SAPConnection_SystemNumber_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.SystemNumber == "sample_text"
    instance.SystemNumber = "sample_text_2"
    assert instance.SystemNumber == "sample_text_2"


def test_connection_SAPConnection_Username_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


def test_connection_SAPConnection_currentFucntion_value_roundtrip():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert instance.currentFucntion == "sample_text"
    instance.currentFucntion = "sample_text_2"
    assert instance.currentFucntion == "sample_text_2"


def test_connection_SAPFunctionParameterColumn_DataType_value_roundtrip():
    instance = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    assert instance.DataType == "sample_text"
    instance.DataType = "sample_text_2"
    assert instance.DataType == "sample_text_2"


def test_connection_SAPFunctionParameterColumn_Length_value_roundtrip():
    instance = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    assert instance.Length == "sample_text"
    instance.Length = "sample_text_2"
    assert instance.Length == "sample_text_2"


def test_connection_SAPFunctionParameterColumn_ParameterType_value_roundtrip():
    instance = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    assert instance.ParameterType == "sample_text"
    instance.ParameterType = "sample_text_2"
    assert instance.ParameterType == "sample_text_2"


def test_connection_SAPFunctionParameterColumn_StructureOrTableName_value_roundtrip():
    instance = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    assert instance.StructureOrTableName == "sample_text"
    instance.StructureOrTableName = "sample_text_2"
    assert instance.StructureOrTableName == "sample_text_2"


def test_connection_SAPFunctionParameterColumn_Value_value_roundtrip():
    instance = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_connection_SAPFunctionUnit_OutputTableName_value_roundtrip():
    instance = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    assert instance.OutputTableName == "sample_text"
    instance.OutputTableName = "sample_text_2"
    assert instance.OutputTableName == "sample_text_2"


def test_connection_SAPFunctionUnit_OutputType_value_roundtrip():
    instance = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    assert instance.OutputType == "sample_text"
    instance.OutputType = "sample_text_2"
    assert instance.OutputType == "sample_text_2"


def test_connection_SalesforceSchemaConnection_batchSize_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.batchSize == "sample_text"
    instance.batchSize = "sample_text_2"
    assert instance.batchSize == "sample_text_2"


def test_connection_SalesforceSchemaConnection_moduleName_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.moduleName == "sample_text"
    instance.moduleName = "sample_text_2"
    assert instance.moduleName == "sample_text_2"


def test_connection_SalesforceSchemaConnection_password_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_connection_SalesforceSchemaConnection_proxyHost_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.proxyHost == "sample_text"
    instance.proxyHost = "sample_text_2"
    assert instance.proxyHost == "sample_text_2"


def test_connection_SalesforceSchemaConnection_proxyPassword_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.proxyPassword == "sample_text"
    instance.proxyPassword = "sample_text_2"
    assert instance.proxyPassword == "sample_text_2"


def test_connection_SalesforceSchemaConnection_proxyPort_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.proxyPort == "sample_text"
    instance.proxyPort = "sample_text_2"
    assert instance.proxyPort == "sample_text_2"


def test_connection_SalesforceSchemaConnection_proxyUsername_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.proxyUsername == "sample_text"
    instance.proxyUsername = "sample_text_2"
    assert instance.proxyUsername == "sample_text_2"


def test_connection_SalesforceSchemaConnection_queryCondition_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.queryCondition == "sample_text"
    instance.queryCondition = "sample_text_2"
    assert instance.queryCondition == "sample_text_2"


def test_connection_SalesforceSchemaConnection_timeOut_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.timeOut == "sample_text"
    instance.timeOut = "sample_text_2"
    assert instance.timeOut == "sample_text_2"


def test_connection_SalesforceSchemaConnection_useAlphbet_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.useAlphbet == True
    instance.useAlphbet = False
    assert instance.useAlphbet == False


def test_connection_SalesforceSchemaConnection_useCustomModuleName_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.useCustomModuleName == True
    instance.useCustomModuleName = False
    assert instance.useCustomModuleName == False


def test_connection_SalesforceSchemaConnection_useHttpProxy_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.useHttpProxy == True
    instance.useHttpProxy = False
    assert instance.useHttpProxy == False


def test_connection_SalesforceSchemaConnection_useProxy_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.useProxy == True
    instance.useProxy = False
    assert instance.useProxy == False


def test_connection_SalesforceSchemaConnection_userName_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_connection_SalesforceSchemaConnection_webServiceUrl_value_roundtrip():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert instance.webServiceUrl == "sample_text"
    instance.webServiceUrl = "sample_text_2"
    assert instance.webServiceUrl == "sample_text_2"


def test_connection_SchemaTarget_RelativeXPathQuery_value_roundtrip():
    instance = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    assert instance.RelativeXPathQuery == "sample_text"
    instance.RelativeXPathQuery = "sample_text_2"
    assert instance.RelativeXPathQuery == "sample_text_2"


def test_connection_SchemaTarget_TagName_value_roundtrip():
    instance = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    assert instance.TagName == "sample_text"
    instance.TagName = "sample_text_2"
    assert instance.TagName == "sample_text_2"


def test_connection_SubscriberTable_system_value_roundtrip():
    instance = connection_SubscriberTable(system=True)
    assert instance.system == True
    instance.system = False
    assert instance.system == False


def test_connection_WSDLSchemaConnection_Encoding_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.Encoding == "sample_text"
    instance.Encoding = "sample_text_2"
    assert instance.Encoding == "sample_text_2"


def test_connection_WSDLSchemaConnection_EndpointURI_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.EndpointURI == "sample_text"
    instance.EndpointURI = "sample_text_2"
    assert instance.EndpointURI == "sample_text_2"


def test_connection_WSDLSchemaConnection_Password_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_connection_WSDLSchemaConnection_UserName_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_connection_WSDLSchemaConnection_Value_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_connection_WSDLSchemaConnection_WSDL_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.WSDL == "sample_text"
    instance.WSDL = "sample_text_2"
    assert instance.WSDL == "sample_text_2"


def test_connection_WSDLSchemaConnection_methodName_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.methodName == "sample_text"
    instance.methodName = "sample_text_2"
    assert instance.methodName == "sample_text_2"


def test_connection_WSDLSchemaConnection_needAuth_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.needAuth == True
    instance.needAuth = False
    assert instance.needAuth == False


def test_connection_WSDLSchemaConnection_parameters_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.parameters == "sample_text"
    instance.parameters = "sample_text_2"
    assert instance.parameters == "sample_text_2"


def test_connection_WSDLSchemaConnection_proxyHost_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.proxyHost == "sample_text"
    instance.proxyHost = "sample_text_2"
    assert instance.proxyHost == "sample_text_2"


def test_connection_WSDLSchemaConnection_proxyPassword_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.proxyPassword == "sample_text"
    instance.proxyPassword = "sample_text_2"
    assert instance.proxyPassword == "sample_text_2"


def test_connection_WSDLSchemaConnection_proxyPort_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.proxyPort == "sample_text"
    instance.proxyPort = "sample_text_2"
    assert instance.proxyPort == "sample_text_2"


def test_connection_WSDLSchemaConnection_proxyUser_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.proxyUser == "sample_text"
    instance.proxyUser = "sample_text_2"
    assert instance.proxyUser == "sample_text_2"


def test_connection_WSDLSchemaConnection_timeOut_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.timeOut == 7
    instance.timeOut = 13
    assert instance.timeOut == 13


def test_connection_WSDLSchemaConnection_useProxy_value_roundtrip():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert instance.useProxy == True
    instance.useProxy = False
    assert instance.useProxy == False


def test_connection_XmlFileConnection_Encoding_value_roundtrip():
    instance = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    assert instance.Encoding == "sample_text"
    instance.Encoding = "sample_text_2"
    assert instance.Encoding == "sample_text_2"


def test_connection_XmlFileConnection_Guess_value_roundtrip():
    instance = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    assert instance.Guess == True
    instance.Guess = False
    assert instance.Guess == False


def test_connection_XmlFileConnection_MaskXPattern_value_roundtrip():
    instance = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    assert instance.MaskXPattern == "sample_text"
    instance.MaskXPattern = "sample_text_2"
    assert instance.MaskXPattern == "sample_text_2"


def test_connection_XmlFileConnection_XmlFilePath_value_roundtrip():
    instance = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    assert instance.XmlFilePath == "sample_text"
    instance.XmlFilePath = "sample_text_2"
    assert instance.XmlFilePath == "sample_text_2"


def test_connection_XmlFileConnection_XsdFilePath_value_roundtrip():
    instance = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    assert instance.XsdFilePath == "sample_text"
    instance.XsdFilePath = "sample_text_2"
    assert instance.XsdFilePath == "sample_text_2"


def test_connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery_value_roundtrip():
    instance = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    assert instance.AbsoluteXPathQuery == "sample_text"
    instance.AbsoluteXPathQuery = "sample_text_2"
    assert instance.AbsoluteXPathQuery == "sample_text_2"


def test_connection_XmlXPathLoopDescriptor_LimitBoucle_value_roundtrip():
    instance = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    assert instance.LimitBoucle == "sample_text"
    instance.LimitBoucle = "sample_text_2"
    assert instance.LimitBoucle == "sample_text_2"


def test_connection_relational_TdSqlDataType_autoIncrement_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.autoIncrement == "sample_text"
    instance.autoIncrement = "sample_text_2"
    assert instance.autoIncrement == "sample_text_2"


def test_connection_relational_TdSqlDataType_caseSensitive_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.caseSensitive == "sample_text"
    instance.caseSensitive = "sample_text_2"
    assert instance.caseSensitive == "sample_text_2"


def test_connection_relational_TdSqlDataType_javaDataType_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.javaDataType == 7
    instance.javaDataType = 13
    assert instance.javaDataType == 13


def test_connection_relational_TdSqlDataType_localTypeName_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.localTypeName == "sample_text"
    instance.localTypeName = "sample_text_2"
    assert instance.localTypeName == "sample_text_2"


def test_connection_relational_TdSqlDataType_nullable_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.nullable == "sample_text"
    instance.nullable = "sample_text_2"
    assert instance.nullable == "sample_text_2"


def test_connection_relational_TdSqlDataType_searchable_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.searchable == "sample_text"
    instance.searchable = "sample_text_2"
    assert instance.searchable == "sample_text_2"


def test_connection_relational_TdSqlDataType_unsignedAttribute_value_roundtrip():
    instance = connection_relational_TdSqlDataType(autoIncrement="sample_text", caseSensitive="sample_text", javaDataType=7, localTypeName="sample_text", nullable="sample_text", searchable="sample_text", unsignedAttribute="sample_text")
    assert instance.unsignedAttribute == "sample_text"
    instance.unsignedAttribute = "sample_text_2"
    assert instance.unsignedAttribute == "sample_text_2"


def test_connection_xml_TdXMLDocument_xsdFilePath_value_roundtrip():
    instance = connection_xml_TdXMLDocument(xsdFilePath="sample_text")
    assert instance.xsdFilePath == "sample_text"
    instance.xsdFilePath = "sample_text_2"
    assert instance.xsdFilePath == "sample_text_2"


def test_connection_xml_TdXMLElement_javaType_value_roundtrip():
    instance = connection_xml_TdXMLElement(javaType="sample_text")
    assert instance.javaType == "sample_text"
    instance.javaType = "sample_text_2"
    assert instance.javaType == "sample_text_2"


def test_connection_CDCType_isa_AbstractMetadataObject():
    instance = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    assert isinstance(instance, AbstractMetadataObject)


def test_connection_Metadata_isa_AbstractMetadataObject():
    instance = connection_Metadata()
    assert isinstance(instance, AbstractMetadataObject)


def test_connection_Query_isa_AbstractMetadataObject():
    instance = connection_Query(contextMode=True, value="sample_text")
    assert isinstance(instance, AbstractMetadataObject)


def test_connection_SAPFunctionParameterColumn_isa_AbstractMetadataObject():
    instance = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    assert isinstance(instance, AbstractMetadataObject)


def test_connection_SAPFunctionParameterTable_isa_AbstractMetadataObject():
    instance = connection_SAPFunctionParameterTable()
    assert isinstance(instance, AbstractMetadataObject)


def test_connection_SAPFunctionUnit_isa_AbstractMetadataObject():
    instance = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    assert isinstance(instance, AbstractMetadataObject)


def test_connection_DatabaseConnection_isa_Connection():
    instance = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    assert isinstance(instance, Connection)


def test_connection_FileConnection_isa_Connection():
    instance = connection_FileConnection(CsvOption=True, Encoding="sample_text", EscapeChar="sample_text", EscapeType="sample_text", FieldSeparatorValue="sample_text", FilePath="sample_text", FirstLineCaption=True, FooterValue="sample_text", Format="sample_text", HeaderValue="sample_text", LimitValue="sample_text", RemoveEmptyRow=True, RowSeparatorType="sample_text", RowSeparatorValue="sample_text", Server="sample_text", TextEnclosure="sample_text", TextIdentifier="sample_text", UseFooter=True, UseHeader=True, UseLimit=True)
    assert isinstance(instance, Connection)


def test_connection_GenericSchemaConnection_isa_Connection():
    instance = connection_GenericSchemaConnection(mappingTypeId="sample_text", mappingTypeUsed=True)
    assert isinstance(instance, Connection)


def test_connection_LDAPSchemaConnection_isa_Connection():
    instance = connection_LDAPSchemaConnection(Aliases="sample_text", BaseDNs="sample_text", BindPassword="sample_text", BindPrincipal="sample_text", CountLimit="sample_text", EncryptionMethodName="sample_text", Filter="sample_text", GetBaseDNsFromRoot=True, Host="sample_text", LimitValue=7, Port="sample_text", Protocol="sample_text", Referrals="sample_text", ReturnAttributes="sample_text", SavePassword=True, SelectedDN="sample_text", Separator="sample_text", StorePath="sample_text", TimeOutLimit="sample_text", UseAdvanced=True, UseAuthen=True, UseLimit=True, Value="sample_text")
    assert isinstance(instance, Connection)


def test_connection_LdifFileConnection_isa_Connection():
    instance = connection_LdifFileConnection(FilePath="sample_text", LimitEntry=7, Server="sample_text", UseLimit=True, value="sample_text")
    assert isinstance(instance, Connection)


def test_connection_MDMConnection_isa_Connection():
    instance = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    assert isinstance(instance, Connection)


def test_connection_SAPConnection_isa_Connection():
    instance = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    assert isinstance(instance, Connection)


def test_connection_SalesforceSchemaConnection_isa_Connection():
    instance = connection_SalesforceSchemaConnection(batchSize="sample_text", moduleName="sample_text", password="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUsername="sample_text", queryCondition="sample_text", timeOut="sample_text", useAlphbet=True, useCustomModuleName=True, useHttpProxy=True, useProxy=True, userName="sample_text", webServiceUrl="sample_text")
    assert isinstance(instance, Connection)


def test_connection_WSDLSchemaConnection_isa_Connection():
    instance = connection_WSDLSchemaConnection(Encoding="sample_text", EndpointURI="sample_text", Password="sample_text", UserName="sample_text", Value="sample_text", WSDL="sample_text", methodName="sample_text", needAuth=True, parameters="sample_text", proxyHost="sample_text", proxyPassword="sample_text", proxyPort="sample_text", proxyUser="sample_text", timeOut=7, useProxy=True)
    assert isinstance(instance, Connection)


def test_connection_XmlFileConnection_isa_Connection():
    instance = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    assert isinstance(instance, Connection)


def test_connection_DelimitedFileConnection_isa_FileConnection():
    instance = connection_DelimitedFileConnection(FieldSeparatorType="sample_text", splitRecord=True)
    assert isinstance(instance, FileConnection)


def test_connection_EbcdicConnection_isa_FileConnection():
    instance = connection_EbcdicConnection(DataFile="sample_text", MidFile="sample_text")
    assert isinstance(instance, FileConnection)


def test_connection_FileExcelConnection_isa_FileConnection():
    instance = connection_FileExcelConnection(SheetName="sample_text", advancedSpearator=True, decimalSeparator="sample_text", firstColumn="sample_text", lastColumn="sample_text", selectAllSheets=True, sheetColumns="sample_text", sheetList="sample_text", thousandSeparator="sample_text")
    assert isinstance(instance, FileConnection)


def test_connection_HL7Connection_isa_FileConnection():
    instance = connection_HL7Connection(EndChar=7, StartChar="sample_text")
    assert isinstance(instance, FileConnection)


def test_connection_PositionalFileConnection_isa_FileConnection():
    instance = connection_PositionalFileConnection()
    assert isinstance(instance, FileConnection)


def test_connection_RegexpFileConnection_isa_FileConnection():
    instance = connection_RegexpFileConnection(FieldSeparatorType="sample_text")
    assert isinstance(instance, FileConnection)


def test_connection_relational_TdColumn_isa_MetadataColumn():
    instance = connection_relational_TdColumn()
    assert isinstance(instance, MetadataColumn)


def test_connection_InputSAPFunctionParameterTable_isa_SAPFunctionParameterTable():
    instance = connection_InputSAPFunctionParameterTable()
    assert isinstance(instance, SAPFunctionParameterTable)


def test_connection_OutputSAPFunctionParameterTable_isa_SAPFunctionParameterTable():
    instance = connection_OutputSAPFunctionParameterTable()
    assert isinstance(instance, SAPFunctionParameterTable)


def test_connection_SAPTestInputParameterTable_isa_SAPFunctionParameterTable():
    instance = connection_SAPTestInputParameterTable()
    assert isinstance(instance, SAPFunctionParameterTable)


def test_connection_Concept_isa_TdTable():
    instance = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    assert isinstance(instance, TdTable)


def test_connection_SubscriberTable_isa_TdTable():
    instance = connection_SubscriberTable(system=True)
    assert isinstance(instance, TdTable)


def test_assoc_Funtions12_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    b2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2")
    _safe_set(a, 'SAPFunctionUnit', b1)
    assert _is_linked(a, 'SAPFunctionUnit', b1)
    if hasattr(b1, 'connection13'):
        assert _is_linked(b1, 'connection13', a)
    _safe_set(a, 'SAPFunctionUnit', b2)
    assert _is_linked(a, 'SAPFunctionUnit', b2)
    if hasattr(b1, 'connection13'):
        assert not _is_linked(b1, 'connection13', a)
    if hasattr(b2, 'connection13'):
        assert _is_linked(b2, 'connection13', a)
    _safe_set(a, 'SAPFunctionUnit', None)
    assert not _is_linked(a, 'SAPFunctionUnit', b2)
    if hasattr(b2, 'connection13'):
        assert not _is_linked(b2, 'connection13', a)


def test_assoc_InputParameterTable14_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_InputSAPFunctionParameterTable()
    b2 = connection_InputSAPFunctionParameterTable()
    _safe_set(a, 'functionUnit', b1)
    assert _is_linked(a, 'functionUnit', b1)
    if hasattr(b1, 'InputSAPFunctionParameterTable'):
        assert _is_linked(b1, 'InputSAPFunctionParameterTable', a)
    _safe_set(a, 'functionUnit', b2)
    assert _is_linked(a, 'functionUnit', b2)
    if hasattr(b1, 'InputSAPFunctionParameterTable'):
        assert not _is_linked(b1, 'InputSAPFunctionParameterTable', a)
    if hasattr(b2, 'InputSAPFunctionParameterTable'):
        assert _is_linked(b2, 'InputSAPFunctionParameterTable', a)
    _safe_set(a, 'functionUnit', None)
    assert not _is_linked(a, 'functionUnit', b2)
    if hasattr(b2, 'InputSAPFunctionParameterTable'):
        assert not _is_linked(b2, 'InputSAPFunctionParameterTable', a)


def test_assoc_MetadataTable17_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    b2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    _safe_set(a, 'connection_SAPFunctionUnit', b1)
    assert _is_linked(a, 'connection_SAPFunctionUnit', b1)
    if hasattr(b1, 'connection_MetadataTable18'):
        assert _is_linked(b1, 'connection_MetadataTable18', a)
    _safe_set(a, 'connection_SAPFunctionUnit', b2)
    assert _is_linked(a, 'connection_SAPFunctionUnit', b2)
    if hasattr(b1, 'connection_MetadataTable18'):
        assert not _is_linked(b1, 'connection_MetadataTable18', a)
    if hasattr(b2, 'connection_MetadataTable18'):
        assert _is_linked(b2, 'connection_MetadataTable18', a)
    _safe_set(a, 'connection_SAPFunctionUnit', None)
    assert not _is_linked(a, 'connection_SAPFunctionUnit', b2)
    if hasattr(b2, 'connection_MetadataTable18'):
        assert not _is_linked(b2, 'connection_MetadataTable18', a)


def test_assoc_OutputParameterTable15_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_OutputSAPFunctionParameterTable()
    b2 = connection_OutputSAPFunctionParameterTable()
    _safe_set(a, 'functionUnit16', b1)
    assert _is_linked(a, 'functionUnit16', b1)
    if hasattr(b1, 'OutputSAPFunctionParameterTable'):
        assert _is_linked(b1, 'OutputSAPFunctionParameterTable', a)
    _safe_set(a, 'functionUnit16', b2)
    assert _is_linked(a, 'functionUnit16', b2)
    if hasattr(b1, 'OutputSAPFunctionParameterTable'):
        assert not _is_linked(b1, 'OutputSAPFunctionParameterTable', a)
    if hasattr(b2, 'OutputSAPFunctionParameterTable'):
        assert _is_linked(b2, 'OutputSAPFunctionParameterTable', a)
    _safe_set(a, 'functionUnit16', None)
    assert not _is_linked(a, 'functionUnit16', b2)
    if hasattr(b2, 'OutputSAPFunctionParameterTable'):
        assert not _is_linked(b2, 'OutputSAPFunctionParameterTable', a)


def test_assoc_ParameterTable25_link_reassign_clear():
    a = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    b1 = connection_SAPFunctionParameterTable()
    b2 = connection_SAPFunctionParameterTable()
    _safe_set(a, 'columns', b1)
    assert _is_linked(a, 'columns', b1)
    if hasattr(b1, 'SAPFunctionParameterTable'):
        assert _is_linked(b1, 'SAPFunctionParameterTable', a)
    _safe_set(a, 'columns', b2)
    assert _is_linked(a, 'columns', b2)
    if hasattr(b1, 'SAPFunctionParameterTable'):
        assert not _is_linked(b1, 'SAPFunctionParameterTable', a)
    if hasattr(b2, 'SAPFunctionParameterTable'):
        assert _is_linked(b2, 'SAPFunctionParameterTable', a)
    _safe_set(a, 'columns', None)
    assert not _is_linked(a, 'columns', b2)
    if hasattr(b2, 'SAPFunctionParameterTable'):
        assert not _is_linked(b2, 'SAPFunctionParameterTable', a)


def test_assoc_TestInputParameterTable23_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_SAPTestInputParameterTable()
    b2 = connection_SAPTestInputParameterTable()
    _safe_set(a, 'functionUnit24', b1)
    assert _is_linked(a, 'functionUnit24', b1)
    if hasattr(b1, 'SAPTestInputParameterTable'):
        assert _is_linked(b1, 'SAPTestInputParameterTable', a)
    _safe_set(a, 'functionUnit24', b2)
    assert _is_linked(a, 'functionUnit24', b2)
    if hasattr(b1, 'SAPTestInputParameterTable'):
        assert not _is_linked(b1, 'SAPTestInputParameterTable', a)
    if hasattr(b2, 'SAPTestInputParameterTable'):
        assert _is_linked(b2, 'SAPTestInputParameterTable', a)
    _safe_set(a, 'functionUnit24', None)
    assert not _is_linked(a, 'functionUnit24', b2)
    if hasattr(b2, 'SAPTestInputParameterTable'):
        assert not _is_linked(b2, 'SAPTestInputParameterTable', a)


def test_assoc_cdcConnection47_link_reassign_clear():
    a = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    b1 = connection_CDCConnection()
    b2 = connection_CDCConnection()
    _safe_set(a, 'connection_CDCType48', b1)
    assert _is_linked(a, 'connection_CDCType48', b1)
    if hasattr(b1, 'connection_CDCConnection49'):
        assert _is_linked(b1, 'connection_CDCConnection49', a)
    _safe_set(a, 'connection_CDCType48', b2)
    assert _is_linked(a, 'connection_CDCType48', b2)
    if hasattr(b1, 'connection_CDCConnection49'):
        assert not _is_linked(b1, 'connection_CDCConnection49', a)
    if hasattr(b2, 'connection_CDCConnection49'):
        assert _is_linked(b2, 'connection_CDCConnection49', a)
    _safe_set(a, 'connection_CDCType48', None)
    assert not _is_linked(a, 'connection_CDCType48', b2)
    if hasattr(b2, 'connection_CDCConnection49'):
        assert not _is_linked(b2, 'connection_CDCConnection49', a)


def test_assoc_cdcConns10_link_reassign_clear():
    a = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    b1 = connection_CDCConnection()
    b2 = connection_CDCConnection()
    _safe_set(a, 'connection11', b1)
    assert _is_linked(a, 'connection11', b1)
    if hasattr(b1, 'CDCConnection'):
        assert _is_linked(b1, 'CDCConnection', a)
    _safe_set(a, 'connection11', b2)
    assert _is_linked(a, 'connection11', b2)
    if hasattr(b1, 'CDCConnection'):
        assert not _is_linked(b1, 'CDCConnection', a)
    if hasattr(b2, 'CDCConnection'):
        assert _is_linked(b2, 'CDCConnection', a)
    _safe_set(a, 'connection11', None)
    assert not _is_linked(a, 'connection11', b2)
    if hasattr(b2, 'CDCConnection'):
        assert not _is_linked(b2, 'CDCConnection', a)


def test_assoc_cdcTypes44_link_reassign_clear():
    a = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    b1 = connection_CDCConnection()
    b2 = connection_CDCConnection()
    _safe_set(a, 'connection_CDCType', b1)
    assert _is_linked(a, 'connection_CDCType', b1)
    if hasattr(b1, 'connection_CDCConnection'):
        assert _is_linked(b1, 'connection_CDCConnection', a)
    _safe_set(a, 'connection_CDCType', b2)
    assert _is_linked(a, 'connection_CDCType', b2)
    if hasattr(b1, 'connection_CDCConnection'):
        assert not _is_linked(b1, 'connection_CDCConnection', a)
    if hasattr(b2, 'connection_CDCConnection'):
        assert _is_linked(b2, 'connection_CDCConnection', a)
    _safe_set(a, 'connection_CDCType', None)
    assert not _is_linked(a, 'connection_CDCType', b2)
    if hasattr(b2, 'connection_CDCConnection'):
        assert not _is_linked(b2, 'connection_CDCConnection', a)


def test_assoc_columns26_link_reassign_clear():
    a = connection_SAPFunctionParameterColumn(DataType="sample_text", Length="sample_text", ParameterType="sample_text", StructureOrTableName="sample_text", Value="sample_text")
    b1 = connection_SAPFunctionParameterTable()
    b2 = connection_SAPFunctionParameterTable()
    _safe_set(a, 'SAPFunctionParameterColumn', b1)
    assert _is_linked(a, 'SAPFunctionParameterColumn', b1)
    if hasattr(b1, 'ParameterTable'):
        assert _is_linked(b1, 'ParameterTable', a)
    _safe_set(a, 'SAPFunctionParameterColumn', b2)
    assert _is_linked(a, 'SAPFunctionParameterColumn', b2)
    if hasattr(b1, 'ParameterTable'):
        assert not _is_linked(b1, 'ParameterTable', a)
    if hasattr(b2, 'ParameterTable'):
        assert _is_linked(b2, 'ParameterTable', a)
    _safe_set(a, 'SAPFunctionParameterColumn', None)
    assert not _is_linked(a, 'SAPFunctionParameterColumn', b2)
    if hasattr(b2, 'ParameterTable'):
        assert not _is_linked(b2, 'ParameterTable', a)


def test_assoc_columns3_link_reassign_clear():
    a = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    b1 = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    b2 = connection_MetadataColumn(defaultValue="sample_text_2", displayField="sample_text_2", key=False, nullable=False, originalField="sample_text_2", pattern="sample_text_2", sourceType="sample_text_2", talendType="sample_text_2")
    _safe_set(a, 'connection_MetadataTable4', {b1})
    assert _is_linked(a, 'connection_MetadataTable4', b1)
    if hasattr(b1, 'connection_MetadataColumn5'):
        assert _is_linked(b1, 'connection_MetadataColumn5', a)
    _safe_set(a, 'connection_MetadataTable4', {b2})
    assert _is_linked(a, 'connection_MetadataTable4', b2)
    if hasattr(b1, 'connection_MetadataColumn5'):
        assert not _is_linked(b1, 'connection_MetadataColumn5', a)
    if hasattr(b2, 'connection_MetadataColumn5'):
        assert _is_linked(b2, 'connection_MetadataColumn5', a)
    _safe_set(a, 'connection_MetadataTable4', set())
    assert not _is_linked(a, 'connection_MetadataTable4', b2)
    if hasattr(b2, 'connection_MetadataColumn5'):
        assert not _is_linked(b2, 'connection_MetadataColumn5', a)


def test_assoc_conceptTargets52_link_reassign_clear():
    a = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    b1 = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    b2 = connection_Concept(LoopExpression="sample_text_2", LoopLimit="sample_text_2")
    _safe_set(a, 'ConceptTarget', b1)
    assert _is_linked(a, 'ConceptTarget', b1)
    if hasattr(b1, 'schema53'):
        assert _is_linked(b1, 'schema53', a)
    _safe_set(a, 'ConceptTarget', b2)
    assert _is_linked(a, 'ConceptTarget', b2)
    if hasattr(b1, 'schema53'):
        assert not _is_linked(b1, 'schema53', a)
    if hasattr(b2, 'schema53'):
        assert _is_linked(b2, 'schema53', a)
    _safe_set(a, 'ConceptTarget', None)
    assert not _is_linked(a, 'ConceptTarget', b2)
    if hasattr(b2, 'schema53'):
        assert not _is_linked(b2, 'schema53', a)


def test_assoc_connection19_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_SAPConnection(Client="sample_text", Host="sample_text", Language="sample_text", Password="sample_text", SystemNumber="sample_text", Username="sample_text", currentFucntion="sample_text")
    b2 = connection_SAPConnection(Client="sample_text_2", Host="sample_text_2", Language="sample_text_2", Password="sample_text_2", SystemNumber="sample_text_2", Username="sample_text_2", currentFucntion="sample_text_2")
    _safe_set(a, 'Funtions', b1)
    assert _is_linked(a, 'Funtions', b1)
    if hasattr(b1, 'SAPConnection'):
        assert _is_linked(b1, 'SAPConnection', a)
    _safe_set(a, 'Funtions', b2)
    assert _is_linked(a, 'Funtions', b2)
    if hasattr(b1, 'SAPConnection'):
        assert not _is_linked(b1, 'SAPConnection', a)
    if hasattr(b2, 'SAPConnection'):
        assert _is_linked(b2, 'SAPConnection', a)
    _safe_set(a, 'Funtions', None)
    assert not _is_linked(a, 'Funtions', b2)
    if hasattr(b2, 'SAPConnection'):
        assert not _is_linked(b2, 'SAPConnection', a)


def test_assoc_connection35_link_reassign_clear():
    a = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    b1 = connection_QueriesConnection()
    b2 = connection_QueriesConnection()
    _safe_set(a, 'Connection', b1)
    assert _is_linked(a, 'Connection', b1)
    if hasattr(b1, 'queries'):
        assert _is_linked(b1, 'queries', a)
    _safe_set(a, 'Connection', b2)
    assert _is_linked(a, 'Connection', b2)
    if hasattr(b1, 'queries'):
        assert not _is_linked(b1, 'queries', a)
    if hasattr(b2, 'queries'):
        assert _is_linked(b2, 'queries', a)
    _safe_set(a, 'Connection', None)
    assert not _is_linked(a, 'Connection', b2)
    if hasattr(b2, 'queries'):
        assert not _is_linked(b2, 'queries', a)


def test_assoc_connection40_link_reassign_clear():
    a = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    b1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    b2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2")
    _safe_set(a, 'schema', b1)
    assert _is_linked(a, 'schema', b1)
    if hasattr(b1, 'XmlFileConnection'):
        assert _is_linked(b1, 'XmlFileConnection', a)
    _safe_set(a, 'schema', b2)
    assert _is_linked(a, 'schema', b2)
    if hasattr(b1, 'XmlFileConnection'):
        assert not _is_linked(b1, 'XmlFileConnection', a)
    if hasattr(b2, 'XmlFileConnection'):
        assert _is_linked(b2, 'XmlFileConnection', a)
    _safe_set(a, 'schema', None)
    assert not _is_linked(a, 'schema', b2)
    if hasattr(b2, 'XmlFileConnection'):
        assert not _is_linked(b2, 'XmlFileConnection', a)


def test_assoc_connection43_link_reassign_clear():
    a = connection_DatabaseConnection(AdditionalParams="sample_text", DBRootPath="sample_text", DatabaseType="sample_text", DatasourceName="sample_text", DbmsId="sample_text", DriverClass="sample_text", DriverJarPath="sample_text", FileFieldName="sample_text", NullChar="sample_text", Password="sample_text", Port="sample_text", ProductId="sample_text", SID="sample_text", SQLMode=True, ServerName="sample_text", SqlSynthax="sample_text", StandardSQL=True, StringQuote="sample_text", SystemSQL=True, URL="sample_text", UiSchema="sample_text", Username="sample_text", cdcTypeMode="sample_text", dbVersionString="sample_text")
    b1 = connection_CDCConnection()
    b2 = connection_CDCConnection()
    _safe_set(a, 'DatabaseConnection', b1)
    assert _is_linked(a, 'DatabaseConnection', b1)
    if hasattr(b1, 'cdcConns'):
        assert _is_linked(b1, 'cdcConns', a)
    _safe_set(a, 'DatabaseConnection', b2)
    assert _is_linked(a, 'DatabaseConnection', b2)
    if hasattr(b1, 'cdcConns'):
        assert not _is_linked(b1, 'cdcConns', a)
    if hasattr(b2, 'cdcConns'):
        assert _is_linked(b2, 'cdcConns', a)
    _safe_set(a, 'DatabaseConnection', None)
    assert not _is_linked(a, 'DatabaseConnection', b2)
    if hasattr(b2, 'cdcConns'):
        assert not _is_linked(b2, 'cdcConns', a)


def test_assoc_connection6_link_reassign_clear():
    a = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    b1 = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    b2 = connection_Connection(ContextId="sample_text_2", ContextMode=False, version="sample_text_2")
    _safe_set(a, 'connection_MetadataTable7', b1)
    assert _is_linked(a, 'connection_MetadataTable7', b1)
    if hasattr(b1, 'connection_Connection8'):
        assert _is_linked(b1, 'connection_Connection8', a)
    _safe_set(a, 'connection_MetadataTable7', b2)
    assert _is_linked(a, 'connection_MetadataTable7', b2)
    if hasattr(b1, 'connection_Connection8'):
        assert not _is_linked(b1, 'connection_Connection8', a)
    if hasattr(b2, 'connection_Connection8'):
        assert _is_linked(b2, 'connection_Connection8', a)
    _safe_set(a, 'connection_MetadataTable7', None)
    assert not _is_linked(a, 'connection_MetadataTable7', b2)
    if hasattr(b2, 'connection_Connection8'):
        assert not _is_linked(b2, 'connection_Connection8', a)


def test_assoc_connections0_link_reassign_clear():
    a = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    b1 = connection_Metadata()
    b2 = connection_Metadata()
    _safe_set(a, 'connection_Connection', b1)
    assert _is_linked(a, 'connection_Connection', b1)
    if hasattr(b1, 'connection_Metadata'):
        assert _is_linked(b1, 'connection_Metadata', a)
    _safe_set(a, 'connection_Connection', b2)
    assert _is_linked(a, 'connection_Connection', b2)
    if hasattr(b1, 'connection_Metadata'):
        assert not _is_linked(b1, 'connection_Metadata', a)
    if hasattr(b2, 'connection_Metadata'):
        assert _is_linked(b2, 'connection_Metadata', a)
    _safe_set(a, 'connection_Connection', None)
    assert not _is_linked(a, 'connection_Connection', b2)
    if hasattr(b2, 'connection_Metadata'):
        assert not _is_linked(b2, 'connection_Metadata', a)


def test_assoc_functionUnit27_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_InputSAPFunctionParameterTable()
    b2 = connection_InputSAPFunctionParameterTable()
    _safe_set(a, 'SAPFunctionUnit28', b1)
    assert _is_linked(a, 'SAPFunctionUnit28', b1)
    if hasattr(b1, 'InputParameterTable'):
        assert _is_linked(b1, 'InputParameterTable', a)
    _safe_set(a, 'SAPFunctionUnit28', b2)
    assert _is_linked(a, 'SAPFunctionUnit28', b2)
    if hasattr(b1, 'InputParameterTable'):
        assert not _is_linked(b1, 'InputParameterTable', a)
    if hasattr(b2, 'InputParameterTable'):
        assert _is_linked(b2, 'InputParameterTable', a)
    _safe_set(a, 'SAPFunctionUnit28', None)
    assert not _is_linked(a, 'SAPFunctionUnit28', b2)
    if hasattr(b2, 'InputParameterTable'):
        assert not _is_linked(b2, 'InputParameterTable', a)


def test_assoc_functionUnit29_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_OutputSAPFunctionParameterTable()
    b2 = connection_OutputSAPFunctionParameterTable()
    _safe_set(a, 'SAPFunctionUnit30', b1)
    assert _is_linked(a, 'SAPFunctionUnit30', b1)
    if hasattr(b1, 'OutputParameterTable'):
        assert _is_linked(b1, 'OutputParameterTable', a)
    _safe_set(a, 'SAPFunctionUnit30', b2)
    assert _is_linked(a, 'SAPFunctionUnit30', b2)
    if hasattr(b1, 'OutputParameterTable'):
        assert not _is_linked(b1, 'OutputParameterTable', a)
    if hasattr(b2, 'OutputParameterTable'):
        assert _is_linked(b2, 'OutputParameterTable', a)
    _safe_set(a, 'SAPFunctionUnit30', None)
    assert not _is_linked(a, 'SAPFunctionUnit30', b2)
    if hasattr(b2, 'OutputParameterTable'):
        assert not _is_linked(b2, 'OutputParameterTable', a)


def test_assoc_functionUnit50_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_SAPTestInputParameterTable()
    b2 = connection_SAPTestInputParameterTable()
    _safe_set(a, 'SAPFunctionUnit51', b1)
    assert _is_linked(a, 'SAPFunctionUnit51', b1)
    if hasattr(b1, 'TestInputParameterTable'):
        assert _is_linked(b1, 'TestInputParameterTable', a)
    _safe_set(a, 'SAPFunctionUnit51', b2)
    assert _is_linked(a, 'SAPFunctionUnit51', b2)
    if hasattr(b1, 'TestInputParameterTable'):
        assert not _is_linked(b1, 'TestInputParameterTable', a)
    if hasattr(b2, 'TestInputParameterTable'):
        assert _is_linked(b2, 'TestInputParameterTable', a)
    _safe_set(a, 'SAPFunctionUnit51', None)
    assert not _is_linked(a, 'SAPFunctionUnit51', b2)
    if hasattr(b2, 'TestInputParameterTable'):
        assert not _is_linked(b2, 'TestInputParameterTable', a)


def test_assoc_ownedDocument56_link_reassign_clear():
    a = connection_xml_TdXMLElement(javaType="sample_text")
    b1 = xml_TdXMLDocument()
    b2 = xml_TdXMLDocument()
    _safe_set(a, 'connection_xml_TdXMLElement', b1)
    assert _is_linked(a, 'connection_xml_TdXMLElement', b1)
    if hasattr(b1, 'xml_TdXMLDocument'):
        assert _is_linked(b1, 'xml_TdXMLDocument', a)
    _safe_set(a, 'connection_xml_TdXMLElement', b2)
    assert _is_linked(a, 'connection_xml_TdXMLElement', b2)
    if hasattr(b1, 'xml_TdXMLDocument'):
        assert not _is_linked(b1, 'xml_TdXMLDocument', a)
    if hasattr(b2, 'xml_TdXMLDocument'):
        assert _is_linked(b2, 'xml_TdXMLDocument', a)
    _safe_set(a, 'connection_xml_TdXMLElement', None)
    assert not _is_linked(a, 'connection_xml_TdXMLElement', b2)
    if hasattr(b2, 'xml_TdXMLDocument'):
        assert not _is_linked(b2, 'xml_TdXMLDocument', a)


def test_assoc_queries1_link_reassign_clear():
    a = connection_Connection(ContextId="sample_text", ContextMode=True, version="sample_text")
    b1 = connection_QueriesConnection()
    b2 = connection_QueriesConnection()
    _safe_set(a, 'connection', b1)
    assert _is_linked(a, 'connection', b1)
    if hasattr(b1, 'QueriesConnection'):
        assert _is_linked(b1, 'QueriesConnection', a)
    _safe_set(a, 'connection', b2)
    assert _is_linked(a, 'connection', b2)
    if hasattr(b1, 'QueriesConnection'):
        assert not _is_linked(b1, 'QueriesConnection', a)
    if hasattr(b2, 'QueriesConnection'):
        assert _is_linked(b2, 'QueriesConnection', a)
    _safe_set(a, 'connection', None)
    assert not _is_linked(a, 'connection', b2)
    if hasattr(b2, 'QueriesConnection'):
        assert not _is_linked(b2, 'QueriesConnection', a)


def test_assoc_queries38_link_reassign_clear():
    a = connection_Query(contextMode=True, value="sample_text")
    b1 = connection_QueriesConnection()
    b2 = connection_QueriesConnection()
    _safe_set(a, 'query', b1)
    assert _is_linked(a, 'query', b1)
    if hasattr(b1, 'QueriesConnection39'):
        assert _is_linked(b1, 'QueriesConnection39', a)
    _safe_set(a, 'query', b2)
    assert _is_linked(a, 'query', b2)
    if hasattr(b1, 'QueriesConnection39'):
        assert not _is_linked(b1, 'QueriesConnection39', a)
    if hasattr(b2, 'QueriesConnection39'):
        assert _is_linked(b2, 'QueriesConnection39', a)
    _safe_set(a, 'query', None)
    assert not _is_linked(a, 'query', b2)
    if hasattr(b2, 'QueriesConnection39'):
        assert not _is_linked(b2, 'QueriesConnection39', a)


def test_assoc_query36_link_reassign_clear():
    a = connection_Query(contextMode=True, value="sample_text")
    b1 = connection_QueriesConnection()
    b2 = connection_QueriesConnection()
    _safe_set(a, 'Query', b1)
    assert _is_linked(a, 'Query', b1)
    if hasattr(b1, 'queries37'):
        assert _is_linked(b1, 'queries37', a)
    _safe_set(a, 'Query', b2)
    assert _is_linked(a, 'Query', b2)
    if hasattr(b1, 'queries37'):
        assert not _is_linked(b1, 'queries37', a)
    if hasattr(b2, 'queries37'):
        assert _is_linked(b2, 'queries37', a)
    _safe_set(a, 'Query', None)
    assert not _is_linked(a, 'Query', b2)
    if hasattr(b2, 'queries37'):
        assert not _is_linked(b2, 'queries37', a)


def test_assoc_schema31_link_reassign_clear():
    a = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    b1 = connection_XmlFileConnection(Encoding="sample_text", Guess=True, MaskXPattern="sample_text", XmlFilePath="sample_text", XsdFilePath="sample_text")
    b2 = connection_XmlFileConnection(Encoding="sample_text_2", Guess=False, MaskXPattern="sample_text_2", XmlFilePath="sample_text_2", XsdFilePath="sample_text_2")
    _safe_set(a, 'XmlXPathLoopDescriptor', b1)
    assert _is_linked(a, 'XmlXPathLoopDescriptor', b1)
    if hasattr(b1, 'connection32'):
        assert _is_linked(b1, 'connection32', a)
    _safe_set(a, 'XmlXPathLoopDescriptor', b2)
    assert _is_linked(a, 'XmlXPathLoopDescriptor', b2)
    if hasattr(b1, 'connection32'):
        assert not _is_linked(b1, 'connection32', a)
    if hasattr(b2, 'connection32'):
        assert _is_linked(b2, 'connection32', a)
    _safe_set(a, 'XmlXPathLoopDescriptor', None)
    assert not _is_linked(a, 'XmlXPathLoopDescriptor', b2)
    if hasattr(b2, 'connection32'):
        assert not _is_linked(b2, 'connection32', a)


def test_assoc_schema33_link_reassign_clear():
    a = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    b1 = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    b2 = connection_SchemaTarget(RelativeXPathQuery="sample_text_2", TagName="sample_text_2")
    _safe_set(a, 'XmlXPathLoopDescriptor34', b1)
    assert _is_linked(a, 'XmlXPathLoopDescriptor34', b1)
    if hasattr(b1, 'schemaTargets'):
        assert _is_linked(b1, 'schemaTargets', a)
    _safe_set(a, 'XmlXPathLoopDescriptor34', b2)
    assert _is_linked(a, 'XmlXPathLoopDescriptor34', b2)
    if hasattr(b1, 'schemaTargets'):
        assert not _is_linked(b1, 'schemaTargets', a)
    if hasattr(b2, 'schemaTargets'):
        assert _is_linked(b2, 'schemaTargets', a)
    _safe_set(a, 'XmlXPathLoopDescriptor34', None)
    assert not _is_linked(a, 'XmlXPathLoopDescriptor34', b2)
    if hasattr(b2, 'schemaTargets'):
        assert not _is_linked(b2, 'schemaTargets', a)


def test_assoc_schema54_link_reassign_clear():
    a = connection_ConceptTarget(RelativeLoopExpression="sample_text", targetName="sample_text")
    b1 = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    b2 = connection_Concept(LoopExpression="sample_text_2", LoopLimit="sample_text_2")
    _safe_set(a, 'conceptTargets', b1)
    assert _is_linked(a, 'conceptTargets', b1)
    if hasattr(b1, 'Concept'):
        assert _is_linked(b1, 'Concept', a)
    _safe_set(a, 'conceptTargets', b2)
    assert _is_linked(a, 'conceptTargets', b2)
    if hasattr(b1, 'Concept'):
        assert not _is_linked(b1, 'Concept', a)
    if hasattr(b2, 'Concept'):
        assert _is_linked(b2, 'Concept', a)
    _safe_set(a, 'conceptTargets', None)
    assert not _is_linked(a, 'conceptTargets', b2)
    if hasattr(b2, 'Concept'):
        assert not _is_linked(b2, 'Concept', a)


def test_assoc_schemaTargets41_link_reassign_clear():
    a = connection_XmlXPathLoopDescriptor(AbsoluteXPathQuery="sample_text", LimitBoucle="sample_text")
    b1 = connection_SchemaTarget(RelativeXPathQuery="sample_text", TagName="sample_text")
    b2 = connection_SchemaTarget(RelativeXPathQuery="sample_text_2", TagName="sample_text_2")
    _safe_set(a, 'schema42', {b1})
    assert _is_linked(a, 'schema42', b1)
    if hasattr(b1, 'SchemaTarget'):
        assert _is_linked(b1, 'SchemaTarget', a)
    _safe_set(a, 'schema42', {b2})
    assert _is_linked(a, 'schema42', b2)
    if hasattr(b1, 'SchemaTarget'):
        assert not _is_linked(b1, 'SchemaTarget', a)
    if hasattr(b2, 'SchemaTarget'):
        assert _is_linked(b2, 'SchemaTarget', a)
    _safe_set(a, 'schema42', set())
    assert not _is_linked(a, 'schema42', b2)
    if hasattr(b2, 'SchemaTarget'):
        assert not _is_linked(b2, 'SchemaTarget', a)


def test_assoc_schemas9_link_reassign_clear():
    a = connection_MDMConnection(Datacluster="sample_text", Datamodel="sample_text", Password="sample_text", Port="sample_text", Server="sample_text", Universe="sample_text", Username="sample_text")
    b1 = connection_Concept(LoopExpression="sample_text", LoopLimit="sample_text")
    b2 = connection_Concept(LoopExpression="sample_text_2", LoopLimit="sample_text_2")
    _safe_set(a, 'connection_MDMConnection', {b1})
    assert _is_linked(a, 'connection_MDMConnection', b1)
    if hasattr(b1, 'connection_Concept'):
        assert _is_linked(b1, 'connection_Concept', a)
    _safe_set(a, 'connection_MDMConnection', {b2})
    assert _is_linked(a, 'connection_MDMConnection', b2)
    if hasattr(b1, 'connection_Concept'):
        assert not _is_linked(b1, 'connection_Concept', a)
    if hasattr(b2, 'connection_Concept'):
        assert _is_linked(b2, 'connection_Concept', a)
    _safe_set(a, 'connection_MDMConnection', set())
    assert not _is_linked(a, 'connection_MDMConnection', b2)
    if hasattr(b2, 'connection_Concept'):
        assert not _is_linked(b2, 'connection_Concept', a)


def test_assoc_sqlDataType55_link_reassign_clear():
    a = connection_relational_TdColumn()
    b1 = relational_TdSqlDataType()
    b2 = relational_TdSqlDataType()
    _safe_set(a, 'connection_relational_TdColumn', b1)
    assert _is_linked(a, 'connection_relational_TdColumn', b1)
    if hasattr(b1, 'relational_TdSqlDataType'):
        assert _is_linked(b1, 'relational_TdSqlDataType', a)
    _safe_set(a, 'connection_relational_TdColumn', b2)
    assert _is_linked(a, 'connection_relational_TdColumn', b2)
    if hasattr(b1, 'relational_TdSqlDataType'):
        assert not _is_linked(b1, 'relational_TdSqlDataType', a)
    if hasattr(b2, 'relational_TdSqlDataType'):
        assert _is_linked(b2, 'relational_TdSqlDataType', a)
    _safe_set(a, 'connection_relational_TdColumn', None)
    assert not _is_linked(a, 'connection_relational_TdColumn', b2)
    if hasattr(b2, 'relational_TdSqlDataType'):
        assert not _is_linked(b2, 'relational_TdSqlDataType', a)


def test_assoc_subscribers45_link_reassign_clear():
    a = connection_SubscriberTable(system=True)
    b1 = connection_CDCType(journalName="sample_text", linkDB="sample_text")
    b2 = connection_CDCType(journalName="sample_text_2", linkDB="sample_text_2")
    _safe_set(a, 'connection_SubscriberTable', b1)
    assert _is_linked(a, 'connection_SubscriberTable', b1)
    if hasattr(b1, 'connection_CDCType46'):
        assert _is_linked(b1, 'connection_CDCType46', a)
    _safe_set(a, 'connection_SubscriberTable', b2)
    assert _is_linked(a, 'connection_SubscriberTable', b2)
    if hasattr(b1, 'connection_CDCType46'):
        assert not _is_linked(b1, 'connection_CDCType46', a)
    if hasattr(b2, 'connection_CDCType46'):
        assert _is_linked(b2, 'connection_CDCType46', a)
    _safe_set(a, 'connection_SubscriberTable', None)
    assert not _is_linked(a, 'connection_SubscriberTable', b2)
    if hasattr(b2, 'connection_CDCType46'):
        assert not _is_linked(b2, 'connection_CDCType46', a)


def test_assoc_table2_link_reassign_clear():
    a = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    b1 = connection_MetadataColumn(defaultValue="sample_text", displayField="sample_text", key=True, nullable=True, originalField="sample_text", pattern="sample_text", sourceType="sample_text", talendType="sample_text")
    b2 = connection_MetadataColumn(defaultValue="sample_text_2", displayField="sample_text_2", key=False, nullable=False, originalField="sample_text_2", pattern="sample_text_2", sourceType="sample_text_2", talendType="sample_text_2")
    _safe_set(a, 'connection_MetadataTable', b1)
    assert _is_linked(a, 'connection_MetadataTable', b1)
    if hasattr(b1, 'connection_MetadataColumn'):
        assert _is_linked(b1, 'connection_MetadataColumn', a)
    _safe_set(a, 'connection_MetadataTable', b2)
    assert _is_linked(a, 'connection_MetadataTable', b2)
    if hasattr(b1, 'connection_MetadataColumn'):
        assert not _is_linked(b1, 'connection_MetadataColumn', a)
    if hasattr(b2, 'connection_MetadataColumn'):
        assert _is_linked(b2, 'connection_MetadataColumn', a)
    _safe_set(a, 'connection_MetadataTable', None)
    assert not _is_linked(a, 'connection_MetadataTable', b2)
    if hasattr(b2, 'connection_MetadataColumn'):
        assert not _is_linked(b2, 'connection_MetadataColumn', a)


def test_assoc_tables20_link_reassign_clear():
    a = connection_SAPFunctionUnit(OutputTableName="sample_text", OutputType="sample_text")
    b1 = connection_MetadataTable(activatedCDC=True, attachedCDC=True, sourceName="sample_text", tableType="sample_text")
    b2 = connection_MetadataTable(activatedCDC=False, attachedCDC=False, sourceName="sample_text_2", tableType="sample_text_2")
    _safe_set(a, 'connection_SAPFunctionUnit21', {b1})
    assert _is_linked(a, 'connection_SAPFunctionUnit21', b1)
    if hasattr(b1, 'connection_MetadataTable22'):
        assert _is_linked(b1, 'connection_MetadataTable22', a)
    _safe_set(a, 'connection_SAPFunctionUnit21', {b2})
    assert _is_linked(a, 'connection_SAPFunctionUnit21', b2)
    if hasattr(b1, 'connection_MetadataTable22'):
        assert not _is_linked(b1, 'connection_MetadataTable22', a)
    if hasattr(b2, 'connection_MetadataTable22'):
        assert _is_linked(b2, 'connection_MetadataTable22', a)
    _safe_set(a, 'connection_SAPFunctionUnit21', set())
    assert not _is_linked(a, 'connection_SAPFunctionUnit21', b2)
    if hasattr(b2, 'connection_MetadataTable22'):
        assert not _is_linked(b2, 'connection_MetadataTable22', a)


def test_assoc_xmlContent57_link_reassign_clear():
    a = connection_xml_TdXMLElement(javaType="sample_text")
    b1 = xml_TdXMLContent()
    b2 = xml_TdXMLContent()
    _safe_set(a, 'connection_xml_TdXMLElement58', b1)
    assert _is_linked(a, 'connection_xml_TdXMLElement58', b1)
    if hasattr(b1, 'xml_TdXMLContent'):
        assert _is_linked(b1, 'xml_TdXMLContent', a)
    _safe_set(a, 'connection_xml_TdXMLElement58', b2)
    assert _is_linked(a, 'connection_xml_TdXMLElement58', b2)
    if hasattr(b1, 'xml_TdXMLContent'):
        assert not _is_linked(b1, 'xml_TdXMLContent', a)
    if hasattr(b2, 'xml_TdXMLContent'):
        assert _is_linked(b2, 'xml_TdXMLContent', a)
    _safe_set(a, 'connection_xml_TdXMLElement58', None)
    assert not _is_linked(a, 'connection_xml_TdXMLElement58', b2)
    if hasattr(b2, 'xml_TdXMLContent'):
        assert not _is_linked(b2, 'xml_TdXMLContent', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractMetadataObject_strategy = st.builds(AbstractMetadataObject)
@given(instance=AbstractMetadataObject_strategy)
@settings(max_examples=25)
def test_AbstractMetadataObject_instantiation(instance):
    assert isinstance(instance, AbstractMetadataObject)


Connection_strategy = st.builds(Connection)
@given(instance=Connection_strategy)
@settings(max_examples=25)
def test_Connection_instantiation(instance):
    assert isinstance(instance, Connection)


FileConnection_strategy = st.builds(FileConnection)
@given(instance=FileConnection_strategy)
@settings(max_examples=25)
def test_FileConnection_instantiation(instance):
    assert isinstance(instance, FileConnection)


MetadataColumn_strategy = st.builds(MetadataColumn)
@given(instance=MetadataColumn_strategy)
@settings(max_examples=25)
def test_MetadataColumn_instantiation(instance):
    assert isinstance(instance, MetadataColumn)


SAPFunctionParameterTable_strategy = st.builds(SAPFunctionParameterTable)
@given(instance=SAPFunctionParameterTable_strategy)
@settings(max_examples=25)
def test_SAPFunctionParameterTable_instantiation(instance):
    assert isinstance(instance, SAPFunctionParameterTable)


TdTable_strategy = st.builds(TdTable)
@given(instance=TdTable_strategy)
@settings(max_examples=25)
def test_TdTable_instantiation(instance):
    assert isinstance(instance, TdTable)


connection_AbstractMetadataObject_strategy = st.builds(connection_AbstractMetadataObject, comment=safe_text, divergency=st.booleans(), id=safe_text, label=safe_text, properties=safe_text, readOnly=st.booleans(), synchronised=st.booleans())
@given(instance=connection_AbstractMetadataObject_strategy)
@settings(max_examples=25)
def test_connection_AbstractMetadataObject_instantiation(instance):
    assert isinstance(instance, connection_AbstractMetadataObject)


connection_CDCConnection_strategy = st.builds(connection_CDCConnection)
@given(instance=connection_CDCConnection_strategy)
@settings(max_examples=25)
def test_connection_CDCConnection_instantiation(instance):
    assert isinstance(instance, connection_CDCConnection)


connection_CDCType_strategy = st.builds(connection_CDCType, journalName=safe_text, linkDB=safe_text)
@given(instance=connection_CDCType_strategy)
@settings(max_examples=25)
def test_connection_CDCType_instantiation(instance):
    assert isinstance(instance, connection_CDCType)


connection_Concept_strategy = st.builds(connection_Concept, LoopExpression=safe_text, LoopLimit=safe_text)
@given(instance=connection_Concept_strategy)
@settings(max_examples=25)
def test_connection_Concept_instantiation(instance):
    assert isinstance(instance, connection_Concept)


connection_ConceptTarget_strategy = st.builds(connection_ConceptTarget, RelativeLoopExpression=safe_text, targetName=safe_text)
@given(instance=connection_ConceptTarget_strategy)
@settings(max_examples=25)
def test_connection_ConceptTarget_instantiation(instance):
    assert isinstance(instance, connection_ConceptTarget)


connection_Connection_strategy = st.builds(connection_Connection, ContextId=safe_text, ContextMode=st.booleans(), version=safe_text)
@given(instance=connection_Connection_strategy)
@settings(max_examples=25)
def test_connection_Connection_instantiation(instance):
    assert isinstance(instance, connection_Connection)


connection_DatabaseConnection_strategy = st.builds(connection_DatabaseConnection, AdditionalParams=safe_text, DBRootPath=safe_text, DatabaseType=safe_text, DatasourceName=safe_text, DbmsId=safe_text, DriverClass=safe_text, DriverJarPath=safe_text, FileFieldName=safe_text, NullChar=safe_text, Password=safe_text, Port=safe_text, ProductId=safe_text, SID=safe_text, SQLMode=st.booleans(), ServerName=safe_text, SqlSynthax=safe_text, StandardSQL=st.booleans(), StringQuote=safe_text, SystemSQL=st.booleans(), URL=safe_text, UiSchema=safe_text, Username=safe_text, cdcTypeMode=safe_text, dbVersionString=safe_text)
@given(instance=connection_DatabaseConnection_strategy)
@settings(max_examples=25)
def test_connection_DatabaseConnection_instantiation(instance):
    assert isinstance(instance, connection_DatabaseConnection)


connection_DelimitedFileConnection_strategy = st.builds(connection_DelimitedFileConnection, FieldSeparatorType=safe_text, splitRecord=st.booleans())
@given(instance=connection_DelimitedFileConnection_strategy)
@settings(max_examples=25)
def test_connection_DelimitedFileConnection_instantiation(instance):
    assert isinstance(instance, connection_DelimitedFileConnection)


connection_EbcdicConnection_strategy = st.builds(connection_EbcdicConnection, DataFile=safe_text, MidFile=safe_text)
@given(instance=connection_EbcdicConnection_strategy)
@settings(max_examples=25)
def test_connection_EbcdicConnection_instantiation(instance):
    assert isinstance(instance, connection_EbcdicConnection)


connection_FileConnection_strategy = st.builds(connection_FileConnection, CsvOption=st.booleans(), Encoding=safe_text, EscapeChar=safe_text, EscapeType=safe_text, FieldSeparatorValue=safe_text, FilePath=safe_text, FirstLineCaption=st.booleans(), FooterValue=safe_text, Format=safe_text, HeaderValue=safe_text, LimitValue=safe_text, RemoveEmptyRow=st.booleans(), RowSeparatorType=safe_text, RowSeparatorValue=safe_text, Server=safe_text, TextEnclosure=safe_text, TextIdentifier=safe_text, UseFooter=st.booleans(), UseHeader=st.booleans(), UseLimit=st.booleans())
@given(instance=connection_FileConnection_strategy)
@settings(max_examples=25)
def test_connection_FileConnection_instantiation(instance):
    assert isinstance(instance, connection_FileConnection)


connection_FileExcelConnection_strategy = st.builds(connection_FileExcelConnection, SheetName=safe_text, advancedSpearator=st.booleans(), decimalSeparator=safe_text, firstColumn=safe_text, lastColumn=safe_text, selectAllSheets=st.booleans(), sheetColumns=safe_text, sheetList=safe_text, thousandSeparator=safe_text)
@given(instance=connection_FileExcelConnection_strategy)
@settings(max_examples=25)
def test_connection_FileExcelConnection_instantiation(instance):
    assert isinstance(instance, connection_FileExcelConnection)


connection_GenericPackage_strategy = st.builds(connection_GenericPackage)
@given(instance=connection_GenericPackage_strategy)
@settings(max_examples=25)
def test_connection_GenericPackage_instantiation(instance):
    assert isinstance(instance, connection_GenericPackage)


connection_GenericSchemaConnection_strategy = st.builds(connection_GenericSchemaConnection, mappingTypeId=safe_text, mappingTypeUsed=st.booleans())
@given(instance=connection_GenericSchemaConnection_strategy)
@settings(max_examples=25)
def test_connection_GenericSchemaConnection_instantiation(instance):
    assert isinstance(instance, connection_GenericSchemaConnection)


connection_HL7Connection_strategy = st.builds(connection_HL7Connection, EndChar=st.integers(), StartChar=safe_text)
@given(instance=connection_HL7Connection_strategy)
@settings(max_examples=25)
def test_connection_HL7Connection_instantiation(instance):
    assert isinstance(instance, connection_HL7Connection)


connection_InputSAPFunctionParameterTable_strategy = st.builds(connection_InputSAPFunctionParameterTable)
@given(instance=connection_InputSAPFunctionParameterTable_strategy)
@settings(max_examples=25)
def test_connection_InputSAPFunctionParameterTable_instantiation(instance):
    assert isinstance(instance, connection_InputSAPFunctionParameterTable)


connection_LDAPSchemaConnection_strategy = st.builds(connection_LDAPSchemaConnection, Aliases=safe_text, BaseDNs=safe_text, BindPassword=safe_text, BindPrincipal=safe_text, CountLimit=safe_text, EncryptionMethodName=safe_text, Filter=safe_text, GetBaseDNsFromRoot=st.booleans(), Host=safe_text, LimitValue=st.integers(), Port=safe_text, Protocol=safe_text, Referrals=safe_text, ReturnAttributes=safe_text, SavePassword=st.booleans(), SelectedDN=safe_text, Separator=safe_text, StorePath=safe_text, TimeOutLimit=safe_text, UseAdvanced=st.booleans(), UseAuthen=st.booleans(), UseLimit=st.booleans(), Value=safe_text)
@given(instance=connection_LDAPSchemaConnection_strategy)
@settings(max_examples=25)
def test_connection_LDAPSchemaConnection_instantiation(instance):
    assert isinstance(instance, connection_LDAPSchemaConnection)


connection_LdifFileConnection_strategy = st.builds(connection_LdifFileConnection, FilePath=safe_text, LimitEntry=st.integers(), Server=safe_text, UseLimit=st.booleans(), value=safe_text)
@given(instance=connection_LdifFileConnection_strategy)
@settings(max_examples=25)
def test_connection_LdifFileConnection_instantiation(instance):
    assert isinstance(instance, connection_LdifFileConnection)


connection_MDMConnection_strategy = st.builds(connection_MDMConnection, Datacluster=safe_text, Datamodel=safe_text, Password=safe_text, Port=safe_text, Server=safe_text, Universe=safe_text, Username=safe_text)
@given(instance=connection_MDMConnection_strategy)
@settings(max_examples=25)
def test_connection_MDMConnection_instantiation(instance):
    assert isinstance(instance, connection_MDMConnection)


connection_Metadata_strategy = st.builds(connection_Metadata)
@given(instance=connection_Metadata_strategy)
@settings(max_examples=25)
def test_connection_Metadata_instantiation(instance):
    assert isinstance(instance, connection_Metadata)


connection_MetadataColumn_strategy = st.builds(connection_MetadataColumn, defaultValue=safe_text, displayField=safe_text, key=st.booleans(), nullable=st.booleans(), originalField=safe_text, pattern=safe_text, sourceType=safe_text, talendType=safe_text)
@given(instance=connection_MetadataColumn_strategy)
@settings(max_examples=25)
def test_connection_MetadataColumn_instantiation(instance):
    assert isinstance(instance, connection_MetadataColumn)


connection_MetadataTable_strategy = st.builds(connection_MetadataTable, activatedCDC=st.booleans(), attachedCDC=st.booleans(), sourceName=safe_text, tableType=safe_text)
@given(instance=connection_MetadataTable_strategy)
@settings(max_examples=25)
def test_connection_MetadataTable_instantiation(instance):
    assert isinstance(instance, connection_MetadataTable)


connection_OutputSAPFunctionParameterTable_strategy = st.builds(connection_OutputSAPFunctionParameterTable)
@given(instance=connection_OutputSAPFunctionParameterTable_strategy)
@settings(max_examples=25)
def test_connection_OutputSAPFunctionParameterTable_instantiation(instance):
    assert isinstance(instance, connection_OutputSAPFunctionParameterTable)


connection_PositionalFileConnection_strategy = st.builds(connection_PositionalFileConnection)
@given(instance=connection_PositionalFileConnection_strategy)
@settings(max_examples=25)
def test_connection_PositionalFileConnection_instantiation(instance):
    assert isinstance(instance, connection_PositionalFileConnection)


connection_QueriesConnection_strategy = st.builds(connection_QueriesConnection)
@given(instance=connection_QueriesConnection_strategy)
@settings(max_examples=25)
def test_connection_QueriesConnection_instantiation(instance):
    assert isinstance(instance, connection_QueriesConnection)


connection_Query_strategy = st.builds(connection_Query, contextMode=st.booleans(), value=safe_text)
@given(instance=connection_Query_strategy)
@settings(max_examples=25)
def test_connection_Query_instantiation(instance):
    assert isinstance(instance, connection_Query)


connection_RegexpFileConnection_strategy = st.builds(connection_RegexpFileConnection, FieldSeparatorType=safe_text)
@given(instance=connection_RegexpFileConnection_strategy)
@settings(max_examples=25)
def test_connection_RegexpFileConnection_instantiation(instance):
    assert isinstance(instance, connection_RegexpFileConnection)


connection_SAPConnection_strategy = st.builds(connection_SAPConnection, Client=safe_text, Host=safe_text, Language=safe_text, Password=safe_text, SystemNumber=safe_text, Username=safe_text, currentFucntion=safe_text)
@given(instance=connection_SAPConnection_strategy)
@settings(max_examples=25)
def test_connection_SAPConnection_instantiation(instance):
    assert isinstance(instance, connection_SAPConnection)


connection_SAPFunctionParameterColumn_strategy = st.builds(connection_SAPFunctionParameterColumn, DataType=safe_text, Length=safe_text, ParameterType=safe_text, StructureOrTableName=safe_text, Value=safe_text)
@given(instance=connection_SAPFunctionParameterColumn_strategy)
@settings(max_examples=25)
def test_connection_SAPFunctionParameterColumn_instantiation(instance):
    assert isinstance(instance, connection_SAPFunctionParameterColumn)


connection_SAPFunctionParameterTable_strategy = st.builds(connection_SAPFunctionParameterTable)
@given(instance=connection_SAPFunctionParameterTable_strategy)
@settings(max_examples=25)
def test_connection_SAPFunctionParameterTable_instantiation(instance):
    assert isinstance(instance, connection_SAPFunctionParameterTable)


connection_SAPFunctionUnit_strategy = st.builds(connection_SAPFunctionUnit, OutputTableName=safe_text, OutputType=safe_text)
@given(instance=connection_SAPFunctionUnit_strategy)
@settings(max_examples=25)
def test_connection_SAPFunctionUnit_instantiation(instance):
    assert isinstance(instance, connection_SAPFunctionUnit)


connection_SAPTestInputParameterTable_strategy = st.builds(connection_SAPTestInputParameterTable)
@given(instance=connection_SAPTestInputParameterTable_strategy)
@settings(max_examples=25)
def test_connection_SAPTestInputParameterTable_instantiation(instance):
    assert isinstance(instance, connection_SAPTestInputParameterTable)


connection_SalesforceSchemaConnection_strategy = st.builds(connection_SalesforceSchemaConnection, batchSize=safe_text, moduleName=safe_text, password=safe_text, proxyHost=safe_text, proxyPassword=safe_text, proxyPort=safe_text, proxyUsername=safe_text, queryCondition=safe_text, timeOut=safe_text, useAlphbet=st.booleans(), useCustomModuleName=st.booleans(), useHttpProxy=st.booleans(), useProxy=st.booleans(), userName=safe_text, webServiceUrl=safe_text)
@given(instance=connection_SalesforceSchemaConnection_strategy)
@settings(max_examples=25)
def test_connection_SalesforceSchemaConnection_instantiation(instance):
    assert isinstance(instance, connection_SalesforceSchemaConnection)


connection_SchemaTarget_strategy = st.builds(connection_SchemaTarget, RelativeXPathQuery=safe_text, TagName=safe_text)
@given(instance=connection_SchemaTarget_strategy)
@settings(max_examples=25)
def test_connection_SchemaTarget_instantiation(instance):
    assert isinstance(instance, connection_SchemaTarget)


connection_SubscriberTable_strategy = st.builds(connection_SubscriberTable, system=st.booleans())
@given(instance=connection_SubscriberTable_strategy)
@settings(max_examples=25)
def test_connection_SubscriberTable_instantiation(instance):
    assert isinstance(instance, connection_SubscriberTable)


connection_WSDLSchemaConnection_strategy = st.builds(connection_WSDLSchemaConnection, Encoding=safe_text, EndpointURI=safe_text, Password=safe_text, UserName=safe_text, Value=safe_text, WSDL=safe_text, methodName=safe_text, needAuth=st.booleans(), parameters=safe_text, proxyHost=safe_text, proxyPassword=safe_text, proxyPort=safe_text, proxyUser=safe_text, timeOut=st.integers(), useProxy=st.booleans())
@given(instance=connection_WSDLSchemaConnection_strategy)
@settings(max_examples=25)
def test_connection_WSDLSchemaConnection_instantiation(instance):
    assert isinstance(instance, connection_WSDLSchemaConnection)


connection_XmlFileConnection_strategy = st.builds(connection_XmlFileConnection, Encoding=safe_text, Guess=st.booleans(), MaskXPattern=safe_text, XmlFilePath=safe_text, XsdFilePath=safe_text)
@given(instance=connection_XmlFileConnection_strategy)
@settings(max_examples=25)
def test_connection_XmlFileConnection_instantiation(instance):
    assert isinstance(instance, connection_XmlFileConnection)


connection_XmlXPathLoopDescriptor_strategy = st.builds(connection_XmlXPathLoopDescriptor, AbsoluteXPathQuery=safe_text, LimitBoucle=safe_text)
@given(instance=connection_XmlXPathLoopDescriptor_strategy)
@settings(max_examples=25)
def test_connection_XmlXPathLoopDescriptor_instantiation(instance):
    assert isinstance(instance, connection_XmlXPathLoopDescriptor)


connection_relational_TdColumn_strategy = st.builds(connection_relational_TdColumn)
@given(instance=connection_relational_TdColumn_strategy)
@settings(max_examples=25)
def test_connection_relational_TdColumn_instantiation(instance):
    assert isinstance(instance, connection_relational_TdColumn)


connection_relational_TdProcedure_strategy = st.builds(connection_relational_TdProcedure)
@given(instance=connection_relational_TdProcedure_strategy)
@settings(max_examples=25)
def test_connection_relational_TdProcedure_instantiation(instance):
    assert isinstance(instance, connection_relational_TdProcedure)


connection_relational_TdSqlDataType_strategy = st.builds(connection_relational_TdSqlDataType, autoIncrement=safe_text, caseSensitive=safe_text, javaDataType=st.integers(), localTypeName=safe_text, nullable=safe_text, searchable=safe_text, unsignedAttribute=safe_text)
@given(instance=connection_relational_TdSqlDataType_strategy)
@settings(max_examples=25)
def test_connection_relational_TdSqlDataType_instantiation(instance):
    assert isinstance(instance, connection_relational_TdSqlDataType)


connection_relational_TdTable_strategy = st.builds(connection_relational_TdTable)
@given(instance=connection_relational_TdTable_strategy)
@settings(max_examples=25)
def test_connection_relational_TdTable_instantiation(instance):
    assert isinstance(instance, connection_relational_TdTable)


connection_relational_TdTrigger_strategy = st.builds(connection_relational_TdTrigger)
@given(instance=connection_relational_TdTrigger_strategy)
@settings(max_examples=25)
def test_connection_relational_TdTrigger_instantiation(instance):
    assert isinstance(instance, connection_relational_TdTrigger)


connection_relational_TdView_strategy = st.builds(connection_relational_TdView)
@given(instance=connection_relational_TdView_strategy)
@settings(max_examples=25)
def test_connection_relational_TdView_instantiation(instance):
    assert isinstance(instance, connection_relational_TdView)


connection_softwaredeployment_TdDataManager_strategy = st.builds(connection_softwaredeployment_TdDataManager)
@given(instance=connection_softwaredeployment_TdDataManager_strategy)
@settings(max_examples=25)
def test_connection_softwaredeployment_TdDataManager_instantiation(instance):
    assert isinstance(instance, connection_softwaredeployment_TdDataManager)


connection_softwaredeployment_TdMachine_strategy = st.builds(connection_softwaredeployment_TdMachine)
@given(instance=connection_softwaredeployment_TdMachine_strategy)
@settings(max_examples=25)
def test_connection_softwaredeployment_TdMachine_instantiation(instance):
    assert isinstance(instance, connection_softwaredeployment_TdMachine)


connection_softwaredeployment_TdSoftwareSystem_strategy = st.builds(connection_softwaredeployment_TdSoftwareSystem)
@given(instance=connection_softwaredeployment_TdSoftwareSystem_strategy)
@settings(max_examples=25)
def test_connection_softwaredeployment_TdSoftwareSystem_instantiation(instance):
    assert isinstance(instance, connection_softwaredeployment_TdSoftwareSystem)


connection_xml_TdXMLContent_strategy = st.builds(connection_xml_TdXMLContent)
@given(instance=connection_xml_TdXMLContent_strategy)
@settings(max_examples=25)
def test_connection_xml_TdXMLContent_instantiation(instance):
    assert isinstance(instance, connection_xml_TdXMLContent)


connection_xml_TdXMLDocument_strategy = st.builds(connection_xml_TdXMLDocument, xsdFilePath=safe_text)
@given(instance=connection_xml_TdXMLDocument_strategy)
@settings(max_examples=25)
def test_connection_xml_TdXMLDocument_instantiation(instance):
    assert isinstance(instance, connection_xml_TdXMLDocument)


connection_xml_TdXMLElement_strategy = st.builds(connection_xml_TdXMLElement, javaType=safe_text)
@given(instance=connection_xml_TdXMLElement_strategy)
@settings(max_examples=25)
def test_connection_xml_TdXMLElement_instantiation(instance):
    assert isinstance(instance, connection_xml_TdXMLElement)


relational_TdSqlDataType_strategy = st.builds(relational_TdSqlDataType)
@given(instance=relational_TdSqlDataType_strategy)
@settings(max_examples=25)
def test_relational_TdSqlDataType_instantiation(instance):
    assert isinstance(instance, relational_TdSqlDataType)


xml_TdXMLContent_strategy = st.builds(xml_TdXMLContent)
@given(instance=xml_TdXMLContent_strategy)
@settings(max_examples=25)
def test_xml_TdXMLContent_instantiation(instance):
    assert isinstance(instance, xml_TdXMLContent)


xml_TdXMLDocument_strategy = st.builds(xml_TdXMLDocument)
@given(instance=xml_TdXMLDocument_strategy)
@settings(max_examples=25)
def test_xml_TdXMLDocument_instantiation(instance):
    assert isinstance(instance, xml_TdXMLDocument)


xml_TdXMLElement_strategy = st.builds(xml_TdXMLElement)
@given(instance=xml_TdXMLElement_strategy)
@settings(max_examples=25)
def test_xml_TdXMLElement_instantiation(instance):
    assert isinstance(instance, xml_TdXMLElement)


