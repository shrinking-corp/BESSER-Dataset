from python_code import documentation_Documentation

def test_documentation_Documentation___init__():
    assert documentation_Documentation.__init__(documentation_Documentation('', documentation_Documentation2=set(), documentation_Documentation=set()), '', documentation_Documentation2=set(), documentation_Documentation=set()) == None


from python_code import documentation_Link

def test_documentation_Link___init__():
    assert documentation_Link.__init__(documentation_Link(''), '') == None


from python_code import documentation_List
from python_code import documentation_ListItem

def test_documentation_ListItem___init__():
    assert documentation_ListItem.__init__(documentation_ListItem('', documentation_ListItem=documentation_List()), '', documentation_ListItem=documentation_List()) == None


from python_code import documentation_NamedElement

def test_documentation_NamedElement___init__():
    assert documentation_NamedElement.__init__(documentation_NamedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import documentation_Reference

def test_documentation_Reference___init__():
    assert documentation_Reference.__init__(documentation_Reference(''), '') == None


from python_code import documentation_TableCell
from python_code import documentation_TableHeader
from python_code import documentation_TableRow

def test_documentation_TableCell___init__():
    assert documentation_TableCell.__init__(documentation_TableCell('', 0, documentation_TableCell=documentation_TableHeader(), documentation_TableCell11=documentation_TableRow()), '', 0, documentation_TableCell=documentation_TableHeader(), documentation_TableCell11=documentation_TableRow()) == None


from python_code import documentation_Text
from python_code import documentation_TextContainer

def test_documentation_Text___init__():
    assert documentation_Text.__init__(documentation_Text('', documentation_Text=documentation_TextContainer()), '', documentation_Text=documentation_TextContainer()) == None


from python_code import documentation_XML

def test_documentation_XML___init__():
    assert documentation_XML.__init__(documentation_XML('', '', '\x00\x00'), '', '', '') == None

