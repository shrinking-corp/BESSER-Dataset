from python_code import docbook_ImageData
from python_code import docbook_ImageObject

def test_docbook_ImageData___init__():
    assert docbook_ImageData.__init__(docbook_ImageData('', '', '\x00\x00', ImageData=docbook_ImageObject(), content52=docbook_ImageObject()), '', '', '', ImageData=docbook_ImageObject(), content52=docbook_ImageObject()) == None


from python_code import docbook_SimpleText

def test_docbook_SimpleText___init__():
    assert docbook_SimpleText.__init__(docbook_SimpleText(''), '') == None


from python_code import docbook_XMLElement

def test_docbook_XMLElement___init__():
    assert docbook_XMLElement.__init__(docbook_XMLElement(''), '') == None

