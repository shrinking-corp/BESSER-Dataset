from python_code import WordprocessingMLBasicDef_BreakElt
from python_code import WordprocessingMLBasicDef_RunElt

def test_WordprocessingMLBasicDef_BreakElt___init__():
    assert WordprocessingMLBasicDef_BreakElt.__init__(WordprocessingMLBasicDef_BreakElt('', RunContentElt=WordprocessingMLBasicDef_RunElt()), '', RunContentElt=WordprocessingMLBasicDef_RunElt()) == None


from python_code import StringType
from python_code import WordprocessingMLBasicDef_FldCharElt

def test_WordprocessingMLBasicDef_FldCharElt___init__():
    assert WordprocessingMLBasicDef_FldCharElt.__init__(WordprocessingMLBasicDef_FldCharElt(StringType(), StringType(), WordprocessingMLBasicDef_FldCharElt=StringType()), StringType(), StringType(), WordprocessingMLBasicDef_FldCharElt=StringType()) == None


from python_code import StringType
from python_code import WordprocessingMLBasicDef_NoteElt

def test_WordprocessingMLBasicDef_NoteElt___init__():
    assert WordprocessingMLBasicDef_NoteElt.__init__(WordprocessingMLBasicDef_NoteElt(StringType(), StringType(), ble_note=set()), StringType(), StringType(), ble_note=set()) == None


from python_code import WordprocessingMLBasicDef_StringType

def test_WordprocessingMLBasicDef_StringType___init__():
    assert WordprocessingMLBasicDef_StringType.__init__(WordprocessingMLBasicDef_StringType(''), '') == None

