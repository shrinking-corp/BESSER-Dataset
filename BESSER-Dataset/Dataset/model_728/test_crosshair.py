from python_code import AttributeDefinitionComplex
from python_code import rif12_ExchangeFile_AttributeDefinitionComplex
from python_code import rif12_ExchangeFile_AttributeValueFileReference

def test_rif12_ExchangeFile_AttributeValueFileReference___init__():
    assert rif12_ExchangeFile_AttributeValueFileReference.__init__(rif12_ExchangeFile_AttributeValueFileReference('', rif12_ExchangeFile_AttributeValueFileReference=AttributeDefinitionComplex(), AttributeValueComplex=rif12_ExchangeFile_AttributeDefinitionComplex()), '', rif12_ExchangeFile_AttributeValueFileReference=AttributeDefinitionComplex(), AttributeValueComplex=rif12_ExchangeFile_AttributeDefinitionComplex()) == None


from python_code import rif12_ExchangeFile_AttributeDefinitionComplex
from python_code import rif12_ExchangeFile_DatatypeDefinitionBinaryFile

def test_rif12_ExchangeFile_DatatypeDefinitionBinaryFile___init__():
    assert rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__init__(rif12_ExchangeFile_DatatypeDefinitionBinaryFile('\x00\x00', '', '', '', DatatypeDefinitionComplex=rif12_ExchangeFile_AttributeDefinitionComplex()), '', '', '', '', DatatypeDefinitionComplex=rif12_ExchangeFile_AttributeDefinitionComplex()) == None


from python_code import rif12_ExchangeFile_AttributeDefinitionSimple
from python_code import rif12_ExchangeFile_DatatypeDefinitionDate

def test_rif12_ExchangeFile_DatatypeDefinitionDate___init__():
    assert rif12_ExchangeFile_DatatypeDefinitionDate.__init__(rif12_ExchangeFile_DatatypeDefinitionDate('', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()), '', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()) == None


from python_code import rif12_ExchangeFile_AttributeDefinitionSimple
from python_code import rif12_ExchangeFile_DatatypeDefinitionInteger

def test_rif12_ExchangeFile_DatatypeDefinitionInteger___init__():
    assert rif12_ExchangeFile_DatatypeDefinitionInteger.__init__(rif12_ExchangeFile_DatatypeDefinitionInteger('', '\x00', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()), '\x00\x00', '', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()) == None


from python_code import rif12_ExchangeFile_AttributeDefinitionSimple
from python_code import rif12_ExchangeFile_DatatypeDefinitionReal

def test_rif12_ExchangeFile_DatatypeDefinitionReal___init__():
    assert rif12_ExchangeFile_DatatypeDefinitionReal.__init__(rif12_ExchangeFile_DatatypeDefinitionReal('', '', '\x00\x00', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()), '', '', '', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()) == None


from python_code import rif12_ExchangeFile_AttributeDefinitionSimple
from python_code import rif12_ExchangeFile_DatatypeDefinitionString

def test_rif12_ExchangeFile_DatatypeDefinitionString___init__():
    assert rif12_ExchangeFile_DatatypeDefinitionString.__init__(rif12_ExchangeFile_DatatypeDefinitionString('', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()), '', DatatypeDefinitionSimple=rif12_ExchangeFile_AttributeDefinitionSimple()) == None


from python_code import rif12_ExchangeFile_AttributeDefinitionComplex
from python_code import rif12_ExchangeFile_DatatypeDefinitionXmlData

def test_rif12_ExchangeFile_DatatypeDefinitionXmlData___init__():
    assert rif12_ExchangeFile_DatatypeDefinitionXmlData.__init__(rif12_ExchangeFile_DatatypeDefinitionXmlData('', '\x00', DatatypeDefinitionComplex=rif12_ExchangeFile_AttributeDefinitionComplex()), '\x00\x00', '', DatatypeDefinitionComplex=rif12_ExchangeFile_AttributeDefinitionComplex()) == None


from python_code import rif12_ExchangeFile_EmbeddedValue

def test_rif12_ExchangeFile_EmbeddedValue___init__():
    assert rif12_ExchangeFile_EmbeddedValue.__init__(rif12_ExchangeFile_EmbeddedValue('', '\x00'), '\x00\x00', '') == None


from python_code import rif12_ExchangeFile_Identifiable

def test_rif12_ExchangeFile_Identifiable___init__():
    assert rif12_ExchangeFile_Identifiable.__init__(rif12_ExchangeFile_Identifiable('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import rif12_ExchangeFile_RIFHeader

def test_rif12_ExchangeFile_RIFHeader___init__():
    assert rif12_ExchangeFile_RIFHeader.__init__(rif12_ExchangeFile_RIFHeader('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

