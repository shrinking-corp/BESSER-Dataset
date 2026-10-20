from python_code import cwm_relational_TdCatalog

def test_cwm_relational_TdCatalog___init__():
    assert cwm_relational_TdCatalog.__init__(cwm_relational_TdCatalog()) == None

def test_cwm_relational_TdCatalog_addSchema():
    assert cwm_relational_TdCatalog.addSchema(cwm_relational_TdCatalog(), '') == None


from python_code import TdSqlDataType
from python_code import cwm_relational_TdColumn

def test_cwm_relational_TdColumn___init__():
    assert cwm_relational_TdColumn.__init__(cwm_relational_TdColumn(0, cwm_relational_TdColumn=TdSqlDataType()), 0, cwm_relational_TdColumn=TdSqlDataType()) == None

def test_cwm_relational_TdColumn_setContentType():
    assert cwm_relational_TdColumn.setContentType(cwm_relational_TdColumn(0, cwm_relational_TdColumn=TdSqlDataType()), 0) == None

def test_cwm_relational_TdColumn_getContentType():
    assert cwm_relational_TdColumn.getContentType(cwm_relational_TdColumn(0, cwm_relational_TdColumn=TdSqlDataType())) == None


from python_code import cwm_relational_TdSqlDataType

def test_cwm_relational_TdSqlDataType___init__():
    assert cwm_relational_TdSqlDataType.__init__(cwm_relational_TdSqlDataType(0, '', '', '', '', '', ''), 0, '\x00', '', '', '', '', '') == None


from python_code import cwm_softwaredeployment_TdProviderConnection

def test_cwm_softwaredeployment_TdProviderConnection___init__():
    assert cwm_softwaredeployment_TdProviderConnection.__init__(cwm_softwaredeployment_TdProviderConnection('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import cwm_xml_TdXMLDocument

def test_cwm_xml_TdXMLDocument___init__():
    assert cwm_xml_TdXMLDocument.__init__(cwm_xml_TdXMLDocument(''), '') == None


from python_code import TdXMLContent
from python_code import TdXMLDocument
from python_code import cwm_xml_TdXMLElement
from python_code import xml_cwm_EObject

def test_cwm_xml_TdXMLElement___init__():
    assert cwm_xml_TdXMLElement.__init__(cwm_xml_TdXMLElement('', cwm_xml_TdXMLElement=xml_cwm_EObject(), cwm_xml_TdXMLElement3=TdXMLDocument(), cwm_xml_TdXMLElement5=TdXMLContent()), '', cwm_xml_TdXMLElement=xml_cwm_EObject(), cwm_xml_TdXMLElement3=TdXMLDocument(), cwm_xml_TdXMLElement5=TdXMLContent()) == None

def test_cwm_xml_TdXMLElement_setContentType():
    assert cwm_xml_TdXMLElement.setContentType(cwm_xml_TdXMLElement('', cwm_xml_TdXMLElement=xml_cwm_EObject(), cwm_xml_TdXMLElement3=TdXMLDocument(), cwm_xml_TdXMLElement5=TdXMLContent()), 0) == None

def test_cwm_xml_TdXMLElement_getContentType():
    assert cwm_xml_TdXMLElement.getContentType(cwm_xml_TdXMLElement('', cwm_xml_TdXMLElement=xml_cwm_EObject(), cwm_xml_TdXMLElement3=TdXMLDocument(), cwm_xml_TdXMLElement5=TdXMLContent())) == None

