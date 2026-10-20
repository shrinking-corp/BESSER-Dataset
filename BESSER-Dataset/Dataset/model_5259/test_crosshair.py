from python_code import HTML_A

def test_HTML_A___init__():
    assert HTML_A.__init__(HTML_A(''), '') == None


from python_code import HTML_DIV

def test_HTML_DIV___init__():
    assert HTML_DIV.__init__(HTML_DIV(''), '') == None


from python_code import HTML_FONT

def test_HTML_FONT___init__():
    assert HTML_FONT.__init__(HTML_FONT('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import HTML_HR

def test_HTML_HR___init__():
    assert HTML_HR.__init__(HTML_HR(''), '') == None


from python_code import HTML_IMG

def test_HTML_IMG___init__():
    assert HTML_IMG.__init__(HTML_IMG('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import HTML_P

def test_HTML_P___init__():
    assert HTML_P.__init__(HTML_P(''), '') == None


from python_code import HTML_HTMLElement
from python_code import HTML_Style

def test_HTML_Style___init__():
    assert HTML_Style.__init__(HTML_Style('', '\x00', HTML_Style=HTML_HTMLElement()), '\x00\x00', '', HTML_Style=HTML_HTMLElement()) == None


from python_code import HTML_TABLE

def test_HTML_TABLE___init__():
    assert HTML_TABLE.__init__(HTML_TABLE(0, '', '', '', '', '', HTML_TABLE=set()), 0, '', '', '', '', '', HTML_TABLE=set()) == None

