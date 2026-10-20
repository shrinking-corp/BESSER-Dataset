from python_code import connection_AbstractMetadataObject

def test_connection_AbstractMetadataObject___init__():
    assert connection_AbstractMetadataObject.__init__(connection_AbstractMetadataObject('', '', '', '', False, False, False), '', '\x00', '', '', False, False, False) == None


from python_code import connection_BRMSConnection

def test_connection_BRMSConnection___init__():
    assert connection_BRMSConnection.__init__(connection_BRMSConnection('', '', '', '', '', '', connection_BRMSConnection=set(), connection_BRMSConnection85=set(), connection_BRMSConnection88=set()), '', '', '', '', '\x00', '', connection_BRMSConnection=set(), connection_BRMSConnection85=set(), connection_BRMSConnection88=set()) == None


from python_code import connection_CDCConnection
from python_code import connection_CDCType

def test_connection_CDCType___init__():
    assert connection_CDCType.__init__(connection_CDCType('\x00\x00', '', connection_CDCType=connection_CDCConnection(), connection_CDCType63=set(), connection_CDCType65=connection_CDCConnection()), '', '', connection_CDCType=connection_CDCConnection(), connection_CDCType63=set(), connection_CDCType65=connection_CDCConnection()) == None


from python_code import connection_CDCConnection
from python_code import connection_DatabaseConnection

def test_connection_DatabaseConnection___init__():
    assert connection_DatabaseConnection.__init__(connection_DatabaseConnection('', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', False, False, '', True, '', connection11=connection_CDCConnection(), DatabaseConnection=connection_CDCConnection()), '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', '', False, False, '', False, '', connection11=connection_CDCConnection(), DatabaseConnection=connection_CDCConnection()) == None


from python_code import connection_DelimitedFileConnection

def test_connection_DelimitedFileConnection___init__():
    assert connection_DelimitedFileConnection.__init__(connection_DelimitedFileConnection('', False), '', False) == None


from python_code import connection_EDIFACTColumn

def test_connection_EDIFACTColumn___init__():
    assert connection_EDIFACTColumn.__init__(connection_EDIFACTColumn('', '\x00'), '\x00\x00', '') == None


from python_code import connection_EDIFACTConnection

def test_connection_EDIFACTConnection___init__():
    assert connection_EDIFACTConnection.__init__(connection_EDIFACTConnection('', '', '\x00\x00'), '', '', '') == None


from python_code import connection_EbcdicConnection

def test_connection_EbcdicConnection___init__():
    assert connection_EbcdicConnection.__init__(connection_EbcdicConnection('', '\x00'), '\x00\x00', '') == None


from python_code import connection_FTPConnection

def test_connection_FTPConnection___init__():
    assert connection_FTPConnection.__init__(connection_FTPConnection('\x00', '', '', '', '', '', False, True, '', '', '', True, '', '', '', '', '\x00'), '', '', '', '', '', '', False, False, '', '', '', False, '', '', '', '', '') == None


from python_code import connection_FileConnection

def test_connection_FileConnection___init__():
    assert connection_FileConnection.__init__(connection_FileConnection('', '', '', '', '', '', '', '', False, '', False, '', False, '', False, False, '', '', '', False), '', '', '', '', '', '', '', '', True, '', False, '', True, '', False, False, '', '', '', False) == None


from python_code import connection_FileExcelConnection

def test_connection_FileExcelConnection___init__():
    assert connection_FileExcelConnection.__init__(connection_FileExcelConnection('', '', '', '', '\x00', '', '', False, False), '', '', '', '', '', '\x00', '', False, False) == None


from python_code import connection_GenericSchemaConnection

def test_connection_GenericSchemaConnection___init__():
    assert connection_GenericSchemaConnection.__init__(connection_GenericSchemaConnection(False, '\x00'), False, '\x00') == None


from python_code import connection_HL7Connection

def test_connection_HL7Connection___init__():
    assert connection_HL7Connection.__init__(connection_HL7Connection('', '', '', connection_HL7Connection=set()), '', '', '', connection_HL7Connection=set()) == None


from python_code import connection_HeaderFooterConnection

def test_connection_HeaderFooterConnection___init__():
    assert connection_HeaderFooterConnection.__init__(connection_HeaderFooterConnection('\x00\x00', False, '', ''), '', False, '', '') == None


from python_code import connection_LDAPSchemaConnection

def test_connection_LDAPSchemaConnection___init__():
    assert connection_LDAPSchemaConnection.__init__(connection_LDAPSchemaConnection('', '', '', '', '', True, '\x00', False, False, '', '', 0, '', '', False, '', '', '', '', '', True, '', ''), '', '', '', '', '', True, '', False, False, '', '', 0, '', '\x00', True, '', '', '', '', '', True, '', '') == None


from python_code import connection_LdifFileConnection

def test_connection_LdifFileConnection___init__():
    assert connection_LdifFileConnection.__init__(connection_LdifFileConnection('', '', 0, False, ''), '', '', 0, False, '') == None


from python_code import connection_MDMConnection

def test_connection_MDMConnection___init__():
    assert connection_MDMConnection.__init__(connection_MDMConnection('\x00', '', '', '', '', '', '', '', '', connection_MDMConnection=set()), '', '\x00', '', '', '', '', '', '', '', connection_MDMConnection=set()) == None

def test_connection_MDMConnection_getConnectionString():
    assert connection_MDMConnection.getConnectionString(connection_MDMConnection('', '', '', '', '', '', '', '', '', connection_MDMConnection=set())) == None


from python_code import connection_QueriesConnection
from python_code import connection_Query

def test_connection_Query___init__():
    assert connection_Query.__init__(connection_Query('', False, Query=connection_QueriesConnection(), query=connection_QueriesConnection()), '', False, Query=connection_QueriesConnection(), query=connection_QueriesConnection()) == None


from python_code import connection_RegexpFileConnection

def test_connection_RegexpFileConnection___init__():
    assert connection_RegexpFileConnection.__init__(connection_RegexpFileConnection(''), '') == None


from python_code import connection_SAPFunctionParameterColumn
from python_code import connection_SAPFunctionParameterTable

def test_connection_SAPFunctionParameterColumn___init__():
    assert connection_SAPFunctionParameterColumn.__init__(connection_SAPFunctionParameterColumn('', '', '', '', '', columns=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()), '', '', '', '', '', columns=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()) == None

def test_connection_SAPFunctionParameterColumn_setDescription():
    assert connection_SAPFunctionParameterColumn.setDescription(connection_SAPFunctionParameterColumn('\x00', '\x00\x00', '', '', '', columns=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()), '') == None


from python_code import connection_ValidationRulesConnection

def test_connection_ValidationRulesConnection___init__():
    assert connection_ValidationRulesConnection.__init__(connection_ValidationRulesConnection(False, False, False, False, '', '', '', '', '', '', '', '', False, False, connection_ValidationRulesConnection=set(), connection_ValidationRulesConnection92=set()), False, True, False, False, '', '', '', '', '', '', '', '', False, False, connection_ValidationRulesConnection=set(), connection_ValidationRulesConnection92=set()) == None


from python_code import connection_relational_TdColumn
from python_code import relational_TdSqlDataType

def test_connection_relational_TdColumn___init__():
    assert connection_relational_TdColumn.__init__(connection_relational_TdColumn(connection_relational_TdColumn=relational_TdSqlDataType()), connection_relational_TdColumn=relational_TdSqlDataType()) == None

def test_connection_relational_TdColumn_getContentType():
    assert connection_relational_TdColumn.getContentType(connection_relational_TdColumn(connection_relational_TdColumn=relational_TdSqlDataType())) == None

def test_connection_relational_TdColumn_getJavaType():
    assert connection_relational_TdColumn.getJavaType(connection_relational_TdColumn(connection_relational_TdColumn=relational_TdSqlDataType())) == None

def test_connection_relational_TdColumn_setContentType():
    assert connection_relational_TdColumn.setContentType(connection_relational_TdColumn(connection_relational_TdColumn=relational_TdSqlDataType()), '') == None


from python_code import connection_relational_TdExpression

def test_connection_relational_TdExpression___init__():
    assert connection_relational_TdExpression.__init__(connection_relational_TdExpression('', '', '\x00\x00'), '', '', '') == None


from python_code import connection_relational_TdSqlDataType

def test_connection_relational_TdSqlDataType___init__():
    assert connection_relational_TdSqlDataType.__init__(connection_relational_TdSqlDataType(0, '', '', '', '', '', ''), 0, '\x00', '', '', '', '', '') == None


from python_code import connection_xml_TdXmlElementType
from python_code import xml_TdXmlContent
from python_code import xml_TdXmlSchema
from python_code import xml_connection_EObject

def test_connection_xml_TdXmlElementType___init__():
    assert connection_xml_TdXmlElementType.__init__(connection_xml_TdXmlElementType('', connection_xml_TdXmlElementType=xml_connection_EObject(), connection_xml_TdXmlElementType102=xml_TdXmlSchema(), connection_xml_TdXmlElementType104=xml_TdXmlContent()), '', connection_xml_TdXmlElementType=xml_connection_EObject(), connection_xml_TdXmlElementType102=xml_TdXmlSchema(), connection_xml_TdXmlElementType104=xml_TdXmlContent()) == None

def test_connection_xml_TdXmlElementType_setContentType():
    assert connection_xml_TdXmlElementType.setContentType(connection_xml_TdXmlElementType('', connection_xml_TdXmlElementType=xml_connection_EObject(), connection_xml_TdXmlElementType102=xml_TdXmlSchema(), connection_xml_TdXmlElementType104=xml_TdXmlContent()), 0) == None

def test_connection_xml_TdXmlElementType_getContentType():
    assert connection_xml_TdXmlElementType.getContentType(connection_xml_TdXmlElementType('', connection_xml_TdXmlElementType=xml_connection_EObject(), connection_xml_TdXmlElementType102=xml_TdXmlSchema(), connection_xml_TdXmlElementType104=xml_TdXmlContent())) == None


from python_code import connection_xml_TdXmlSchema

def test_connection_xml_TdXmlSchema___init__():
    assert connection_xml_TdXmlSchema.__init__(connection_xml_TdXmlSchema(''), '') == None

