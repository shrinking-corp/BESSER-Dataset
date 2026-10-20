from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLBasicDef_BooleanValue
from python_code import WordprocessingMLBasicDef_CustomDocumentProperty

def test_WordprocessingMLBasicDef_BooleanValue___init__():
    assert WordprocessingMLBasicDef_BooleanValue.__init__(WordprocessingMLBasicDef_BooleanValue(StringType(), ValueType=WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType())), StringType(), ValueType=WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType())) == None


from python_code import WordprocessingMLBasicDef_BreakElt
from python_code import WordprocessingMLBasicDef_RunElt

def test_WordprocessingMLBasicDef_BreakElt___init__():
    assert WordprocessingMLBasicDef_BreakElt.__init__(WordprocessingMLBasicDef_BreakElt('', RunContentElt=WordprocessingMLBasicDef_RunElt()), '', RunContentElt=WordprocessingMLBasicDef_RunElt()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLBasicDef_CustomDocumentProperty

def test_WordprocessingMLBasicDef_CustomDocumentProperty___init__():
    assert WordprocessingMLBasicDef_CustomDocumentProperty.__init__(WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType()), StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType()) == None


from python_code import StringType
from python_code import WordprocessingMLBasicDef_DateTimeType

def test_WordprocessingMLBasicDef_DateTimeType___init__():
    assert WordprocessingMLBasicDef_DateTimeType.__init__(WordprocessingMLBasicDef_DateTimeType(StringType(), StringType(), StringType(), StringType(), StringType(), StringType()), StringType(), StringType(), StringType(), StringType(), StringType(), StringType()) == None


from python_code import DateTimeType
from python_code import StringType
from python_code import VersionType
from python_code import WordDocument
from python_code import WordprocessingMLBasicDef_DelInstrText
from python_code import WordprocessingMLBasicDef_DelText
from python_code import WordprocessingMLBasicDef_DocumentPropertiesCollection
from python_code import WordprocessingMLBasicDef_StringProperty
from python_code import WordprocessingMLBasicDef_Text

def test_WordprocessingMLBasicDef_DocumentPropertiesCollection___init__():
    assert WordprocessingMLBasicDef_DocumentPropertiesCollection.__init__(WordprocessingMLBasicDef_DocumentPropertiesCollection(StringType(), WordprocessingMLBasicDef_StringProperty(), WordprocessingMLBasicDef_Text(), StringType(), StringType(), WordprocessingMLBasicDef_DelInstrText(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), wd_docProperties=WordDocument(), WordprocessingMLBasicDef_DocumentPropertiesCollection=VersionType(), WordprocessingMLBasicDef_DocumentPropertiesCollection4=DateTimeType(), WordprocessingMLBasicDef_DocumentPropertiesCollection7=DateTimeType(), WordprocessingMLBasicDef_DocumentPropertiesCollection10=DateTimeType()), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), WordprocessingMLBasicDef_DelText(), StringType(), wd_docProperties=WordDocument(), WordprocessingMLBasicDef_DocumentPropertiesCollection=VersionType(), WordprocessingMLBasicDef_DocumentPropertiesCollection4=DateTimeType(), WordprocessingMLBasicDef_DocumentPropertiesCollection7=DateTimeType(), WordprocessingMLBasicDef_DocumentPropertiesCollection10=DateTimeType()) == None


from python_code import StringType
from python_code import WordprocessingMLBasicDef_FldCharElt

def test_WordprocessingMLBasicDef_FldCharElt___init__():
    assert WordprocessingMLBasicDef_FldCharElt.__init__(WordprocessingMLBasicDef_FldCharElt(StringType(), StringType(), WordprocessingMLBasicDef_FldCharElt=StringType()), StringType(), StringType(), WordprocessingMLBasicDef_FldCharElt=StringType()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLBasicDef_CustomDocumentProperty
from python_code import WordprocessingMLBasicDef_FloatValue

def test_WordprocessingMLBasicDef_FloatValue___init__():
    assert WordprocessingMLBasicDef_FloatValue.__init__(WordprocessingMLBasicDef_FloatValue(StringType(), ValueType=WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType())), StringType(), ValueType=WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType())) == None


from python_code import WordprocessingMLBasicDef_NoteElt

def test_WordprocessingMLBasicDef_NoteElt___init__():
    assert WordprocessingMLBasicDef_NoteElt.__init__(WordprocessingMLBasicDef_NoteElt('\x00\x00', '', ble_note=set()), '', '', ble_note=set()) == None


from python_code import SmartTagsCollection
from python_code import StringType
from python_code import WordprocessingMLBasicDef_SmartTagType

def test_WordprocessingMLBasicDef_SmartTagType___init__():
    assert WordprocessingMLBasicDef_SmartTagType.__init__(WordprocessingMLBasicDef_SmartTagType(StringType(), StringType(), StringType(), smartTagTypes=SmartTagsCollection()), StringType(), StringType(), StringType(), smartTagTypes=SmartTagsCollection()) == None


from python_code import WordprocessingMLBasicDef_StringType

def test_WordprocessingMLBasicDef_StringType___init__():
    assert WordprocessingMLBasicDef_StringType.__init__(WordprocessingMLBasicDef_StringType(''), '') == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLBasicDef_CustomDocumentProperty
from python_code import WordprocessingMLBasicDef_StringValue

def test_WordprocessingMLBasicDef_StringValue___init__():
    assert WordprocessingMLBasicDef_StringValue.__init__(WordprocessingMLBasicDef_StringValue(StringType(), ValueType=WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType())), StringType(), ValueType=WordprocessingMLBasicDef_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLBasicDef_CustomDocumentProperty=ValueType())) == None


from python_code import StringType
from python_code import WordprocessingMLBasicDef_VersionType

def test_WordprocessingMLBasicDef_VersionType___init__():
    assert WordprocessingMLBasicDef_VersionType.__init__(WordprocessingMLBasicDef_VersionType(StringType(), StringType()), StringType(), StringType()) == None

