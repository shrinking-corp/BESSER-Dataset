from python_code import connection_AbstractMetadataObject

def test_connection_AbstractMetadataObject___init__():
    assert connection_AbstractMetadataObject.__init__(connection_AbstractMetadataObject('', '', False, False, False, '', ''), '', '\x00', False, False, False, '', '') == None


from python_code import connection_CDCConnection
from python_code import connection_CDCType

def test_connection_CDCType___init__():
    assert connection_CDCType.__init__(connection_CDCType('\x00\x00', '', connection_CDCType=connection_CDCConnection(), connection_CDCType46=set(), connection_CDCType48=connection_CDCConnection()), '', '', connection_CDCType=connection_CDCConnection(), connection_CDCType46=set(), connection_CDCType48=connection_CDCConnection()) == None


from python_code import connection_CDCConnection
from python_code import connection_DatabaseConnection

def test_connection_DatabaseConnection___init__():
    assert connection_DatabaseConnection.__init__(connection_DatabaseConnection('', '', '', '', '\x00', '', '', '', '', '', True, False, '', '', '', '', '', '', '', '', '', '', '', True, DatabaseConnection=connection_CDCConnection(), connection10=connection_CDCConnection()), '', '', '', '', '', '', '', '', '', '', False, True, '', '', '', '', '', '', '', '', '', '', '', True, DatabaseConnection=connection_CDCConnection(), connection10=connection_CDCConnection()) == None


from python_code import connection_DelimitedFileConnection

def test_connection_DelimitedFileConnection___init__():
    assert connection_DelimitedFileConnection.__init__(connection_DelimitedFileConnection('', False), '', False) == None


from python_code import connection_EbcdicConnection

def test_connection_EbcdicConnection___init__():
    assert connection_EbcdicConnection.__init__(connection_EbcdicConnection('', '\x00'), '\x00\x00', '') == None


from python_code import connection_FileConnection

def test_connection_FileConnection___init__():
    assert connection_FileConnection.__init__(connection_FileConnection('', '', '', True, '', False, '', True, '', False, False, '', '\x00', '', '', '', '', '', '', False), '', '', '', False, '', False, '', False, '', False, True, '', '', '', '', '', '', '', '', False) == None


from python_code import connection_FileExcelConnection

def test_connection_FileExcelConnection___init__():
    assert connection_FileExcelConnection.__init__(connection_FileExcelConnection('', '', '', '', '\x00', '', '', False, False), '', '', '', '', '', '\x00', '', False, False) == None


from python_code import connection_GenericSchemaConnection

def test_connection_GenericSchemaConnection___init__():
    assert connection_GenericSchemaConnection.__init__(connection_GenericSchemaConnection(False, '\x00'), False, '\x00') == None


from python_code import connection_HL7Connection

def test_connection_HL7Connection___init__():
    assert connection_HL7Connection.__init__(connection_HL7Connection('', '\x00'), '\x00\x00', '') == None


from python_code import connection_LDAPSchemaConnection

def test_connection_LDAPSchemaConnection___init__():
    assert connection_LDAPSchemaConnection.__init__(connection_LDAPSchemaConnection('', '', '', 0, '', '', False, '', '', '', '', '', False, '', '', '', '', '', True, '', False, False, ''), '', '', '', 0, '', '', False, '', '', '', '', '', False, '', '', '\x00', '', '', False, '', True, False, '') == None


from python_code import connection_LdifFileConnection

def test_connection_LdifFileConnection___init__():
    assert connection_LdifFileConnection.__init__(connection_LdifFileConnection(False, '', '', '', 0), True, '', '', '', 0) == None


from python_code import connection_MDMConnection

def test_connection_MDMConnection___init__():
    assert connection_MDMConnection.__init__(connection_MDMConnection('', '', '', '', '\x00', '', '', connection_MDMConnection=set()), '', '', '', '', '', '', '', connection_MDMConnection=set()) == None


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
    assert connection_SAPFunctionParameterColumn.__init__(connection_SAPFunctionParameterColumn('', '', '', '', '', '', '', columns24=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()), '', '\x00', '', '', '', '', '', columns24=connection_SAPFunctionParameterTable(), SAPFunctionParameterColumn=connection_SAPFunctionParameterTable()) == None


from python_code import connection_SalesforceSchemaConnection

def test_connection_SalesforceSchemaConnection___init__():
    assert connection_SalesforceSchemaConnection.__init__(connection_SalesforceSchemaConnection('', '', '', '', '\x00', False, False, '', '', '', '', '', False, False, ''), '', '', '', '', '', False, False, '', '', '', '', '', False, True, '') == None


from python_code import connection_WSDLSchemaConnection

def test_connection_WSDLSchemaConnection___init__():
    assert connection_WSDLSchemaConnection.__init__(connection_WSDLSchemaConnection('', '', '', '', 0, '', False, '', '', '', '', False, '', '', ''), '', '', '', '', 0, '', True, '\x00', '', '', '', False, '', '', '') == None

