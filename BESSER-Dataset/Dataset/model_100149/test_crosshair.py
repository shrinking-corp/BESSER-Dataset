from python_code import connection_AbstractMetadataObject

def test_connection_AbstractMetadataObject___init__():
    assert connection_AbstractMetadataObject.__init__(connection_AbstractMetadataObject(False, '', '', '', '', False, False), False, '\x00', '', '', '', False, False) == None


from python_code import connection_BRMSConnection

def test_connection_BRMSConnection___init__():
    assert connection_BRMSConnection.__init__(connection_BRMSConnection('', '', '', '', '', '', connection_BRMSConnection110=set(), connection_BRMSConnection=set(), connection_BRMSConnection107=set()), '', '', '', '', '\x00', '', connection_BRMSConnection110=set(), connection_BRMSConnection=set(), connection_BRMSConnection107=set()) == None


from python_code import connection_CDCConnection
from python_code import connection_CDCType

def test_connection_CDCType___init__():
    assert connection_CDCType.__init__(connection_CDCType('\x00\x00', '', connection_CDCType=connection_CDCConnection(), connection_CDCType85=set(), connection_CDCType87=connection_CDCConnection()), '', '', connection_CDCType=connection_CDCConnection(), connection_CDCType85=set(), connection_CDCType87=connection_CDCConnection()) == None


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
    assert connection_EbcdicConnection.__init__(connection_EbcdicConnection('', '', '', '', ''), '', '', '', '', '') == None


from python_code import connection_FTPConnection

def test_connection_FTPConnection___init__():
    assert connection_FTPConnection.__init__(connection_FTPConnection('', '', '', '', '', '', False, False, '', '', '', '', '', True, '\x00', '', '', '', ''), '', '', '', '', '', '', False, False, '', '', '', '', '', True, '', '', '', '', '') == None


from python_code import connection_FileConnection

def test_connection_FileConnection___init__():
    assert connection_FileConnection.__init__(connection_FileConnection(True, False, '', '', '', False, '', '', '', '', '', '', '\x00', '', False, '', False, '', True, ''), False, False, '', '', '', False, '', '', '', '', '', '', '', '', True, '', False, '', False, '') == None


from python_code import connection_FileExcelConnection

def test_connection_FileExcelConnection___init__():
    assert connection_FileExcelConnection.__init__(connection_FileExcelConnection('', '', '\x00', '', '', '', False, False, '', ''), '', '', '\x00', '', '', '', True, False, '', '') == None


from python_code import connection_GenericSchemaConnection

def test_connection_GenericSchemaConnection___init__():
    assert connection_GenericSchemaConnection.__init__(connection_GenericSchemaConnection(False, '\x00'), False, '\x00') == None


from python_code import connection_HL7Connection

def test_connection_HL7Connection___init__():
    assert connection_HL7Connection.__init__(connection_HL7Connection('', '', '', connection_HL7Connection=set()), '', '', '', connection_HL7Connection=set()) == None


from python_code import connection_HeaderFooterConnection

def test_connection_HeaderFooterConnection___init__():
    assert connection_HeaderFooterConnection.__init__(connection_HeaderFooterConnection(False, '\x00', '', ''), False, '', '', '') == None


from python_code import connection_LDAPSchemaConnection

def test_connection_LDAPSchemaConnection___init__():
    assert connection_LDAPSchemaConnection.__init__(connection_LDAPSchemaConnection('', '', '', '', '', True, '\x00', False, False, '', '', 0, '', '', False, '', '', '', '', '', True, '', ''), '', '', '', '', '', True, '', False, False, '', '', 0, '', '\x00', True, '', '', '', '', '', True, '', '') == None


from python_code import connection_LdifFileConnection

def test_connection_LdifFileConnection___init__():
    assert connection_LdifFileConnection.__init__(connection_LdifFileConnection('', '', 0, False, ''), '', '', 0, False, '') == None


from python_code import connection_MDMConnection

def test_connection_MDMConnection___init__():
    assert connection_MDMConnection.__init__(connection_MDMConnection('', '', '', '', '', '', '', '', '', '', connection_MDMConnection=set()), '\x00', '', '', '', '', '', '', '', '', '', connection_MDMConnection=set()) == None

def test_connection_MDMConnection_getConnectionString():
    assert connection_MDMConnection.getConnectionString(connection_MDMConnection('', '', '', '', '', '', '', '', '', '', connection_MDMConnection=set())) == None


from python_code import connection_QueriesConnection
from python_code import connection_Query

def test_connection_Query___init__():
    assert connection_Query.__init__(connection_Query('', False, Query=connection_QueriesConnection(), query=connection_QueriesConnection()), '', False, Query=connection_QueriesConnection(), query=connection_QueriesConnection()) == None


from python_code import connection_RegexpFileConnection

def test_connection_RegexpFileConnection___init__():
    assert connection_RegexpFileConnection.__init__(connection_RegexpFileConnection(''), '') == None


from python_code import connection_SAPBWTableField

def test_connection_SAPBWTableField___init__():
    assert connection_SAPBWTableField.__init__(connection_SAPBWTableField(''), '') == None


from python_code import connection_SAPFunctionParameterColumn
from python_code import connection_SAPFunctionParameterTable

def test_connection_SAPFunctionParameterColumn___init__():
    assert connection_SAPFunctionParameterColumn.__init__(connection_SAPFunctionParameterColumn('', '', '', '', '', columns=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()), '', '', '', '', '', columns=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()) == None

def test_connection_SAPFunctionParameterColumn_setDescription():
    assert connection_SAPFunctionParameterColumn.setDescription(connection_SAPFunctionParameterColumn('\x00', '\x00\x00', '', '', '', columns=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()), '') == None


from python_code import connection_SAPTable

def test_connection_SAPTable___init__():
    assert connection_SAPTable.__init__(connection_SAPTable(''), '') == None


from python_code import connection_SAPTableField

def test_connection_SAPTableField___init__():
    assert connection_SAPTableField.__init__(connection_SAPTableField('', '\x00'), '\x00\x00', '') == None


from python_code import connection_ValidationRulesConnection

def test_connection_ValidationRulesConnection___init__():
    assert connection_ValidationRulesConnection.__init__(connection_ValidationRulesConnection(False, False, False, False, '', '', '', '', '', '', '', '', False, False, connection_ValidationRulesConnection=set(), connection_ValidationRulesConnection114=set()), False, True, False, False, '', '', '', '', '', '', '', '', False, False, connection_ValidationRulesConnection=set(), connection_ValidationRulesConnection114=set()) == None

