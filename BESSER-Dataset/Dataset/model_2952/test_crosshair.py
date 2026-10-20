from python_code import metamodeloArquitecturaPila_Button

def test_metamodeloArquitecturaPila_Button___init__():
    assert metamodeloArquitecturaPila_Button.__init__(metamodeloArquitecturaPila_Button(''), '') == None


from python_code import metamodeloArquitecturaPila_Grid

def test_metamodeloArquitecturaPila_Grid___init__():
    assert metamodeloArquitecturaPila_Grid.__init__(metamodeloArquitecturaPila_Grid('', '\x00'), '\x00\x00', '') == None


from python_code import metamodeloArquitecturaPila_Input

def test_metamodeloArquitecturaPila_Input___init__():
    assert metamodeloArquitecturaPila_Input.__init__(metamodeloArquitecturaPila_Input(''), '') == None


from python_code import metamodeloArquitecturaPila_DropdownList
from python_code import metamodeloArquitecturaPila_ListItem

def test_metamodeloArquitecturaPila_ListItem___init__():
    assert metamodeloArquitecturaPila_ListItem.__init__(metamodeloArquitecturaPila_ListItem('', '\x00', metamodeloArquitecturaPila_ListItem=metamodeloArquitecturaPila_DropdownList()), '\x00\x00', '', metamodeloArquitecturaPila_ListItem=metamodeloArquitecturaPila_DropdownList()) == None


from python_code import metamodeloArquitecturaPila_TextArea

def test_metamodeloArquitecturaPila_TextArea___init__():
    assert metamodeloArquitecturaPila_TextArea.__init__(metamodeloArquitecturaPila_TextArea(''), '') == None

