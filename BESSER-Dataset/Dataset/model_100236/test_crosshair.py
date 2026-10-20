from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLTableElts_BooleanValue
from python_code import WordprocessingMLTableElts_CustomDocumentProperty

def test_WordprocessingMLTableElts_BooleanValue___init__():
    assert WordprocessingMLTableElts_BooleanValue.__init__(WordprocessingMLTableElts_BooleanValue('\x00', ValueType=WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType())), '', ValueType=WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType())) == None


from python_code import WordprocessingMLTableElts_BreakElt
from python_code import WordprocessingMLTableElts_RunElt

def test_WordprocessingMLTableElts_BreakElt___init__():
    assert WordprocessingMLTableElts_BreakElt.__init__(WordprocessingMLTableElts_BreakElt('', RunContentElt=WordprocessingMLTableElts_RunElt()), '', RunContentElt=WordprocessingMLTableElts_RunElt()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLTableElts_CustomDocumentProperty

def test_WordprocessingMLTableElts_CustomDocumentProperty___init__():
    assert WordprocessingMLTableElts_CustomDocumentProperty.__init__(WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType()), StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType()) == None


from python_code import WordprocessingMLTableElts_DateTimeType

def test_WordprocessingMLTableElts_DateTimeType___init__():
    assert WordprocessingMLTableElts_DateTimeType.__init__(WordprocessingMLTableElts_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import DateTimeType
from python_code import VersionType
from python_code import WordDocument
from python_code import WordprocessingMLTableElts_DocumentPropertiesCollection

def test_WordprocessingMLTableElts_DocumentPropertiesCollection___init__():
    assert WordprocessingMLTableElts_DocumentPropertiesCollection.__init__(WordprocessingMLTableElts_DocumentPropertiesCollection('', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', wd_docProperties=WordDocument(), WordprocessingMLTableElts_DocumentPropertiesCollection=VersionType(), WordprocessingMLTableElts_DocumentPropertiesCollection4=DateTimeType(), WordprocessingMLTableElts_DocumentPropertiesCollection7=DateTimeType(), WordprocessingMLTableElts_DocumentPropertiesCollection10=DateTimeType()), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', wd_docProperties=WordDocument(), WordprocessingMLTableElts_DocumentPropertiesCollection=VersionType(), WordprocessingMLTableElts_DocumentPropertiesCollection4=DateTimeType(), WordprocessingMLTableElts_DocumentPropertiesCollection7=DateTimeType(), WordprocessingMLTableElts_DocumentPropertiesCollection10=DateTimeType()) == None


from python_code import StringType
from python_code import WordprocessingMLTableElts_FldCharElt

def test_WordprocessingMLTableElts_FldCharElt___init__():
    assert WordprocessingMLTableElts_FldCharElt.__init__(WordprocessingMLTableElts_FldCharElt('', '\x00', WordprocessingMLTableElts_FldCharElt=StringType()), '', '', WordprocessingMLTableElts_FldCharElt=StringType()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLTableElts_CustomDocumentProperty
from python_code import WordprocessingMLTableElts_FloatValue

def test_WordprocessingMLTableElts_FloatValue___init__():
    assert WordprocessingMLTableElts_FloatValue.__init__(WordprocessingMLTableElts_FloatValue('', ValueType=WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType())), '', ValueType=WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType())) == None


from python_code import WordprocessingMLTableElts_NoteElt

def test_WordprocessingMLTableElts_NoteElt___init__():
    assert WordprocessingMLTableElts_NoteElt.__init__(WordprocessingMLTableElts_NoteElt('\x00\x00', '', ble_note=set()), '', '', ble_note=set()) == None


from python_code import SmartTagsCollection
from python_code import StringType
from python_code import WordprocessingMLTableElts_SmartTagType

def test_WordprocessingMLTableElts_SmartTagType___init__():
    assert WordprocessingMLTableElts_SmartTagType.__init__(WordprocessingMLTableElts_SmartTagType(StringType(), StringType(), StringType(), smartTagTypes=SmartTagsCollection()), StringType(), StringType(), StringType(), smartTagTypes=SmartTagsCollection()) == None


from python_code import WordprocessingMLTableElts_StringType

def test_WordprocessingMLTableElts_StringType___init__():
    assert WordprocessingMLTableElts_StringType.__init__(WordprocessingMLTableElts_StringType(''), '') == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLTableElts_CustomDocumentProperty
from python_code import WordprocessingMLTableElts_StringValue

def test_WordprocessingMLTableElts_StringValue___init__():
    assert WordprocessingMLTableElts_StringValue.__init__(WordprocessingMLTableElts_StringValue('', ValueType=WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType())), '', ValueType=WordprocessingMLTableElts_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLTableElts_CustomDocumentProperty=ValueType())) == None


from python_code import WordprocessingMLTableElts_VersionType

def test_WordprocessingMLTableElts_VersionType___init__():
    assert WordprocessingMLTableElts_VersionType.__init__(WordprocessingMLTableElts_VersionType('', '\x00'), '\x00\x00', '') == None

