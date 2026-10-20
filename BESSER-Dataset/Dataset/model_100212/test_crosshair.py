from python_code import documentation_Documentation

def test_documentation_Documentation___init__():
    assert documentation_Documentation.__init__(documentation_Documentation('', documentation_Documentation=set(), documentation_Documentation2=set()), '', documentation_Documentation=set(), documentation_Documentation2=set()) == None


from python_code import documentation_Image

def test_documentation_Image___init__():
    assert documentation_Image.__init__(documentation_Image('', '\x00'), '\x00\x00', '') == None


from python_code import documentation_Line

def test_documentation_Line___init__():
    assert documentation_Line.__init__(documentation_Line(''), '') == None


from python_code import documentation_List
from python_code import documentation_ListItem

def test_documentation_ListItem___init__():
    assert documentation_ListItem.__init__(documentation_ListItem('', documentation_ListItem=documentation_List()), '', documentation_ListItem=documentation_List()) == None


from python_code import documentation_NamedElement

def test_documentation_NamedElement___init__():
    assert documentation_NamedElement.__init__(documentation_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import documentation_Table
from python_code import documentation_TableHeader

def test_documentation_TableHeader___init__():
    assert documentation_TableHeader.__init__(documentation_TableHeader('', documentation_TableHeader=documentation_Table()), '', documentation_TableHeader=documentation_Table()) == None


from python_code import documentation_Table
from python_code import documentation_TableRow

def test_documentation_TableRow___init__():
    assert documentation_TableRow.__init__(documentation_TableRow('', documentation_TableRow=documentation_Table()), '', documentation_TableRow=documentation_Table()) == None


from python_code import documentation_XML

def test_documentation_XML___init__():
    assert documentation_XML.__init__(documentation_XML('', '\x00'), '\x00\x00', '') == None

