from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLStyles_BooleanValue
from python_code import WordprocessingMLStyles_CustomDocumentProperty

def test_WordprocessingMLStyles_BooleanValue___init__():
    assert WordprocessingMLStyles_BooleanValue.__init__(WordprocessingMLStyles_BooleanValue(StringType(), ValueType=WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType())), StringType(), ValueType=WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType())) == None


from python_code import WordprocessingMLStyles_BreakElt
from python_code import WordprocessingMLStyles_RunElt

def test_WordprocessingMLStyles_BreakElt___init__():
    assert WordprocessingMLStyles_BreakElt.__init__(WordprocessingMLStyles_BreakElt('', RunContentElt=WordprocessingMLStyles_RunElt()), '', RunContentElt=WordprocessingMLStyles_RunElt()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLStyles_CustomDocumentProperty

def test_WordprocessingMLStyles_CustomDocumentProperty___init__():
    assert WordprocessingMLStyles_CustomDocumentProperty.__init__(WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType()), StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType()) == None


from python_code import StringType
from python_code import WordprocessingMLStyles_DateTimeType

def test_WordprocessingMLStyles_DateTimeType___init__():
    assert WordprocessingMLStyles_DateTimeType.__init__(WordprocessingMLStyles_DateTimeType(StringType(), StringType(), StringType(), StringType(), StringType(), StringType()), StringType(), StringType(), StringType(), StringType(), StringType(), StringType()) == None


from python_code import DateTimeType
from python_code import StringType
from python_code import VersionType
from python_code import WordDocument
from python_code import WordprocessingMLStyles_DelInstrText
from python_code import WordprocessingMLStyles_DelText
from python_code import WordprocessingMLStyles_DocumentPropertiesCollection
from python_code import WordprocessingMLStyles_StringProperty
from python_code import WordprocessingMLStyles_Text

def test_WordprocessingMLStyles_DocumentPropertiesCollection___init__():
    assert WordprocessingMLStyles_DocumentPropertiesCollection.__init__(WordprocessingMLStyles_DocumentPropertiesCollection(StringType(), WordprocessingMLStyles_DelText(), WordprocessingMLStyles_Text(), StringType(), StringType(), WordprocessingMLStyles_DelInstrText(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), wd_docProperties=WordDocument(), WordprocessingMLStyles_DocumentPropertiesCollection4=DateTimeType(), WordprocessingMLStyles_DocumentPropertiesCollection7=DateTimeType(), WordprocessingMLStyles_DocumentPropertiesCollection10=DateTimeType(), WordprocessingMLStyles_DocumentPropertiesCollection=VersionType()), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), StringType(), WordprocessingMLStyles_StringProperty(), StringType(), wd_docProperties=WordDocument(), WordprocessingMLStyles_DocumentPropertiesCollection4=DateTimeType(), WordprocessingMLStyles_DocumentPropertiesCollection7=DateTimeType(), WordprocessingMLStyles_DocumentPropertiesCollection10=DateTimeType(), WordprocessingMLStyles_DocumentPropertiesCollection=VersionType()) == None


from python_code import StringType
from python_code import WordprocessingMLStyles_FldCharElt

def test_WordprocessingMLStyles_FldCharElt___init__():
    assert WordprocessingMLStyles_FldCharElt.__init__(WordprocessingMLStyles_FldCharElt('', '\x00', WordprocessingMLStyles_FldCharElt=StringType()), '', '', WordprocessingMLStyles_FldCharElt=StringType()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLStyles_CustomDocumentProperty
from python_code import WordprocessingMLStyles_FloatValue

def test_WordprocessingMLStyles_FloatValue___init__():
    assert WordprocessingMLStyles_FloatValue.__init__(WordprocessingMLStyles_FloatValue(StringType(), ValueType=WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType())), StringType(), ValueType=WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType())) == None


from python_code import FontsListElt
from python_code import RunPrElt
from python_code import StringType
from python_code import WordprocessingMLStyles_FontsElt

def test_WordprocessingMLStyles_FontsElt___init__():
    assert WordprocessingMLStyles_FontsElt.__init__(WordprocessingMLStyles_FontsElt('', defaultFonts=FontsListElt(), rFonts=RunPrElt(), WordprocessingMLStyles_FontsElt=StringType(), WordprocessingMLStyles_FontsElt126=StringType(), WordprocessingMLStyles_FontsElt129=StringType(), WordprocessingMLStyles_FontsElt132=StringType()), '', defaultFonts=FontsListElt(), rFonts=RunPrElt(), WordprocessingMLStyles_FontsElt=StringType(), WordprocessingMLStyles_FontsElt126=StringType(), WordprocessingMLStyles_FontsElt129=StringType(), WordprocessingMLStyles_FontsElt132=StringType()) == None


from python_code import RunPrElt
from python_code import WordprocessingMLStyles_LangElt

def test_WordprocessingMLStyles_LangElt___init__():
    assert WordprocessingMLStyles_LangElt.__init__(WordprocessingMLStyles_LangElt('', '\x00', language=RunPrElt()), '\x00\x00', '', language=RunPrElt()) == None


from python_code import WordprocessingMLStyles_NoteElt

def test_WordprocessingMLStyles_NoteElt___init__():
    assert WordprocessingMLStyles_NoteElt.__init__(WordprocessingMLStyles_NoteElt('\x00\x00', '', ble_note=set()), '', '', ble_note=set()) == None


from python_code import ParaElt
from python_code import StringProperty
from python_code import StyleElt
from python_code import WordprocessingMLStyles_ParaPrElt

def test_WordprocessingMLStyles_ParaPrElt___init__():
    assert WordprocessingMLStyles_ParaPrElt.__init__(WordprocessingMLStyles_ParaPrElt('', '', '', '', '', '', '\x00', '', pPr=ParaElt(), se_pPr=StyleElt(), WordprocessingMLStyles_ParaPrElt=StringProperty()), '', '', '', '', '', '', '', '', pPr=ParaElt(), se_pPr=StyleElt(), WordprocessingMLStyles_ParaPrElt=StringProperty()) == None


from python_code import FontsElt
from python_code import LangElt
from python_code import RunElt
from python_code import StringProperty
from python_code import StyleElt
from python_code import UnderlineProperty
from python_code import WordprocessingMLStyles_RunPrElt

def test_WordprocessingMLStyles_RunPrElt___init__():
    assert WordprocessingMLStyles_RunPrElt.__init__(WordprocessingMLStyles_RunPrElt('', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', rPr=RunElt(), se_rPr=StyleElt(), WordprocessingMLStyles_RunPrElt=StringProperty(), fse_runPrElt=FontsElt(), WordprocessingMLStyles_RunPrElt62=UnderlineProperty(), le_runPrElt=LangElt()), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', rPr=RunElt(), se_rPr=StyleElt(), WordprocessingMLStyles_RunPrElt=StringProperty(), fse_runPrElt=FontsElt(), WordprocessingMLStyles_RunPrElt62=UnderlineProperty(), le_runPrElt=LangElt()) == None


from python_code import SmartTagsCollection
from python_code import StringType
from python_code import WordprocessingMLStyles_SmartTagType

def test_WordprocessingMLStyles_SmartTagType___init__():
    assert WordprocessingMLStyles_SmartTagType.__init__(WordprocessingMLStyles_SmartTagType(StringType(), StringType(), StringType(), smartTagTypes=SmartTagsCollection()), StringType(), StringType(), StringType(), smartTagTypes=SmartTagsCollection()) == None


from python_code import WordprocessingMLStyles_StringType

def test_WordprocessingMLStyles_StringType___init__():
    assert WordprocessingMLStyles_StringType.__init__(WordprocessingMLStyles_StringType(''), '') == None


from python_code import CustomDocumentPropertiesCollection
from python_code import StringType
from python_code import ValueType
from python_code import WordprocessingMLStyles_CustomDocumentProperty
from python_code import WordprocessingMLStyles_StringValue

def test_WordprocessingMLStyles_StringValue___init__():
    assert WordprocessingMLStyles_StringValue.__init__(WordprocessingMLStyles_StringValue(StringType(), ValueType=WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType())), StringType(), ValueType=WordprocessingMLStyles_CustomDocumentProperty(StringType(), customDocumentProperties=CustomDocumentPropertiesCollection(), WordprocessingMLStyles_CustomDocumentProperty=ValueType())) == None


from python_code import ParaPrElt
from python_code import RunPrElt
from python_code import StringProperty
from python_code import StringType
from python_code import StylesElt
from python_code import TableCellPrElt
from python_code import TablePrElt
from python_code import TableRowPrElt
from python_code import WordprocessingMLStyles_StyleElt

def test_WordprocessingMLStyles_StyleElt___init__():
    assert WordprocessingMLStyles_StyleElt.__init__(WordprocessingMLStyles_StyleElt('', '', '', '', '', '', '', '', '', '\x00', styles147=StylesElt(), WordprocessingMLStyles_StyleElt=StringType(), WordprocessingMLStyles_StyleElt152=StringProperty(), WordprocessingMLStyles_StyleElt155=StringProperty(), WordprocessingMLStyles_StyleElt158=StringProperty(), rpe_styleElt=RunPrElt(), WordprocessingMLStyles_StyleElt161=StringProperty(), WordprocessingMLStyles_StyleElt164=StringProperty(), WordprocessingMLStyles_StyleElt167=StringType(), ppe_styleElt=ParaPrElt(), tpe_styleElt=TablePrElt(), trpe_styleElt=TableRowPrElt(), tcpe_styleElt=TableCellPrElt()), '', '', '', '', '', '', '', '', '', '', styles147=StylesElt(), WordprocessingMLStyles_StyleElt=StringType(), WordprocessingMLStyles_StyleElt152=StringProperty(), WordprocessingMLStyles_StyleElt155=StringProperty(), WordprocessingMLStyles_StyleElt158=StringProperty(), rpe_styleElt=RunPrElt(), WordprocessingMLStyles_StyleElt161=StringProperty(), WordprocessingMLStyles_StyleElt164=StringProperty(), WordprocessingMLStyles_StyleElt167=StringType(), ppe_styleElt=ParaPrElt(), tpe_styleElt=TablePrElt(), trpe_styleElt=TableRowPrElt(), tcpe_styleElt=TableCellPrElt()) == None


from python_code import WordDocument
from python_code import WordprocessingMLStyles_StylesElt

def test_WordprocessingMLStyles_StylesElt___init__():
    assert WordprocessingMLStyles_StylesElt.__init__(WordprocessingMLStyles_StylesElt('', styles=WordDocument(), se_stylesElt=set()), '', styles=WordDocument(), se_stylesElt=set()) == None


from python_code import WordprocessingMLStyles_UnderlineProperty

def test_WordprocessingMLStyles_UnderlineProperty___init__():
    assert WordprocessingMLStyles_UnderlineProperty.__init__(WordprocessingMLStyles_UnderlineProperty('', '\x00'), '\x00\x00', '') == None


from python_code import StringType
from python_code import WordprocessingMLStyles_VersionType

def test_WordprocessingMLStyles_VersionType___init__():
    assert WordprocessingMLStyles_VersionType.__init__(WordprocessingMLStyles_VersionType(StringType(), StringType()), StringType(), StringType()) == None

