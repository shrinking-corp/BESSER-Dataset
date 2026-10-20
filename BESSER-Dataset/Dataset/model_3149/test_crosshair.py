from python_code import ccore_ComputedString

def test_ccore_ComputedString___init__():
    assert ccore_ComputedString.__init__(ccore_ComputedString(''), '') == None


from python_code import ccore_ExportedContent

def test_ccore_ExportedContent___init__():
    assert ccore_ExportedContent.__init__(ccore_ExportedContent()) == None

def test_ccore_ExportedContent_hasChildren():
    assert ccore_ExportedContent.hasChildren(ccore_ExportedContent()) == None


from python_code import ccore_GenInformation

def test_ccore_GenInformation___init__():
    assert ccore_GenInformation.__init__(ccore_GenInformation(''), '') == None


from python_code import ccore_Menu
from python_code import ccore_MenuAbstract

def test_ccore_MenuAbstract___init__():
    assert ccore_MenuAbstract.__init__(ccore_MenuAbstract('', '', '\x00\x00', ccore_MenuAbstract=ccore_Menu()), '', '', '', ccore_MenuAbstract=ccore_Menu()) == None


from python_code import ccore_RuntimeItem

def test_ccore_RuntimeItem___init__():
    assert ccore_RuntimeItem.__init__(ccore_RuntimeItem('', False), '', False) == None


from python_code import ccore_StringAttribute

def test_ccore_StringAttribute___init__():
    assert ccore_StringAttribute.__init__(ccore_StringAttribute(True), False) == None


from python_code import ccore_TimeAttribute

def test_ccore_TimeAttribute___init__():
    assert ccore_TimeAttribute.__init__(ccore_TimeAttribute(True), False) == None


from python_code import ccore_View
from python_code import ccore_ViewModel

def test_ccore_View___init__():
    assert ccore_View.__init__(ccore_View('', ccore_View=set(), ccore_View161=ccore_ViewModel()), '', ccore_View=set(), ccore_View161=ccore_ViewModel()) == None

